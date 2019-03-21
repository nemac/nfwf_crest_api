#! /usr/bin/env python

import fiona
import sys, os, os.path
import click
import pyproj
import json
import subprocess
import requests
from fiona.crs import from_epsg

# Helper methods for transforming geometries

from config import *

WGS84 = pyproj.Proj(init='epsg:4326')
AEA = pyproj.Proj(proj='aea', lat_1=29.5, lat_2=45.5, lat_0=37.5, lon_0=-96, x_0=0, y_0=0, datum='NAD83', units='m')


def transform_polygon(coords):
    new_coords = []
    for coord in coords:
        new_coord = list(pyproj.transform(AEA, WGS84, coord[0], coord[1]))
        new_coords.append(new_coord)
    return new_coords


def transform_geom(geom):
    if geom['type'] == 'Polygon':
        coords = geom['coordinates'][0]
        geom['coordinates'] = [ transform_polygon(coords) ]
    elif geom['type'] == 'MultiPolygon':
        new_polys = []
        for poly in geom['coordinates']:
            new_coords = []
            for coords in poly:
                new_coords.append(transform_polygon(coords))
            new_polys.append(new_coords)
        geom['coordinates'] = new_polys
    else:
        print("Geometry type must be MultiPolygon or Polygon")
        raise
    return geom


def convert_shpfile_to_WGS84(file_path):
    shpfile = fiona.open(file_path)
    new_file_path = file_path.rstrip('.shp') + ".WGS84.shp"

    new_crs = from_epsg('4326')
    new_driver = shpfile.driver
    new_schema = shpfile.schema

    with fiona.open(
            new_file_path,
            'w',
            crs=new_crs,
            driver=new_driver,
            schema=new_schema) as shp:
        for f in shpfile:
            f['geometry'] = transform_geom(f['geometry'])
            shp.write(f)

    return new_file_path


def get_stats_for(feature):
    ID = str(feature['properties'][ID_FIELD])
    
    path = os.path.join(HUBS_DONE_DIR, ID+'.geojson')
    
    if ID in IDS_DONE:
        print('Skipping {0}...'.format(feature['properties'][ID_FIELD]))
        return 

    f_str = json.dumps(feature)

    fc = { "type": "FeatureCollection", "features": [ feature ] }
    fc_str = json.dumps(fc)
    try:
        r = requests.post(ZONAL_STATS_ENDPOINT, data=fc_str)
        if r.status_code == 200:
            try:
                os.remove(path)
            except:
                pass 
            updated_feature = r.json()['features'][0]
            # Write out the result
            with open(path, 'w') as f:
                f.write(json.dumps(updated_feature))
    except Exception as e:
        print(e)
        print(f_str)


def conform_feature(path):
    with fiona.open(path) as fc:
        feature = fc[0]
    new_feature = feature.copy()
    props = new_feature['properties']
    means = props['mean'].copy()
    props.pop('sum')
    props.pop('mean')
    for dataset_id in means:
        key = FIELD_MAPS[dataset_id] if dataset_id in FIELD_MAPS else dataset_id
        value = means[dataset_id]
        props[key] = value
    return new_feature


def write_new_shpfile(dryrun, shpfile_path_out):
    with fiona.open(shpfile_path_out, 'w',
                    crs=from_epsg('4326'),
                    driver='ESRI Shapefile',
                    schema=SCHEMA_FOR_NEW_SHPFILE) as shp:
        for filename in os.listdir(HUBS_DONE_DIR)
            path = os.path.join(HUBS_DONE_DIR, filename)
            f = conform_feature(path)
            shp.write(f)


@click.command()
@click.option('--dryrun', is_flag=True)
@click.argument('shpfile_path_in',
    type=click.Path(exists=True, resolve_path=True)
)
@click.argument('shpfile_path_out',
    type=Click.Path(exists=False, resolve_path=True)
)
def main(dryrun, shpfile_path_in, shpfile_path_out):
    # Convert to WGS84
    shpfile_WGS84_path = convert_shpfile_to_WGS84(shpfile_path)

    # Skip any hub features that may already be processed
    IDS_DONE = []
    for filename in os.listdir(HUBS_DONE_DIR):
        IDS_DONE.append(''.join(filename.split('.')[:-1]))
    shpfile_read = fiona.open(shpfile_WGS84_path)
    for feature in shpfile_read:
        get_stats_for(feature)

    write_new_shpfile(shpfile_path_out)


if '__name__' == '__main__':
    main()

