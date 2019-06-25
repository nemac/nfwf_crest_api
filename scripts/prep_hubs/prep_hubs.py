#! /usr/bin/env python

'''
Prep a hubs shapefile to be uploaded as an AGOL Feature Service.

NOTE: The provided shapefile MUST have a CRS of EPSG:4326!

THIS FILE MUST BE RUN FROM THE ROOT OF THE REPOSITORY OR IT WILL FAIL
Example:
pipenv shell
./scripts/prephubs.py path/to/4326.shp path/to/new.4326.with_stats.shp
'''

import fiona
import sys, os, os.path
import click
import pyproj
import json
import subprocess
import requests
from fiona.crs import from_epsg

from config import *

sys.path.append('.')

from zonal_stats_function import app

IDS_DONE = []

def get_stats_for(feature):
    ID = str(feature['properties'][ID_FIELD_IN])
    
    f_str = json.dumps(feature)

    fc = { "type": "FeatureCollection", "features": [ feature ] }
    try:
        geojson = app.get_response(fc, 'local')
        return geojson['features'][0]
        #r = requests.post(ZONAL_STATS_ENDPOINT, data=fc_str)
        #if r.status_code == 200:
        #    updated_feature = r.json()['features'][0]
        #    return updated_feature
        #else:
        #    print("Non-OK status code {0} for ID {1}".format(r.status_code, ID))

    except Exception as e:
        print('Failed:', ID)
        print(e)


def getFieldMappedKey(key):
    new_key = FIELD_MAPS[key] if key in FIELD_MAPS else key
    return new_key


def conform_feature(feature):
    new_feature = feature.copy()
    props = new_feature['properties']
    means = props['mean'].copy()
    props.pop('mean')
    for key in means:
        new_key = getFieldMappedKey(key)
        value = means[key]
        props[new_key] = value
    for key in props.copy():
        new_key = getFieldMappedKey(key)
        value = props[key]
        if new_key in SCHEMA_FOR_NEW_SHPFILE['properties']:
            if new_key != key:
                props[new_key] = value
                props.pop(key, None)
        else:
            props.pop(new_key, None)
    return new_feature


def get_shp_out_at(shp_path, append=False):
    if append:
        return fiona.open(shp_path, 'a')
    else:
        return fiona.open(shp_path, 'w', crs=from_epsg('4326'), driver='ESRI Shapefile', schema=SCHEMA_FOR_NEW_SHPFILE)



@click.command()
@click.argument('shpfile_path_in',
    type=click.Path(exists=True, resolve_path=True)
)
@click.argument('shpfile_path_out',
    type=click.Path(resolve_path=True)
)
def main(shpfile_path_in, shpfile_path_out):
    with fiona.Env():
        with fiona.open(shpfile_path_in) as shpfile_read:
            ids_done = []
            # Try opening in append mode first
            try:
                with fiona.open(shpfile_path_out) as shp_out_read:
                    for f in shp_out_read:
                        ids_done.append(f['properties'][ID_FIELD_OUT])
                shp_out = get_shp_out_at(shpfile_path_out, True)
                print('WARNING: shapefile to write features to already exists, opening in \'append\' mode...')
            except:
                shp_out = get_shp_out_at(shpfile_path_out)
            skipped_recently = False
            for feature in shpfile_read:
                f_id = feature['properties'][ID_FIELD_IN]
                if f_id in ids_done:
                    if not skipped_recently:
                        print('Skipping some features that already exist...')
                        skipped_recently = True
                else:
                    skipped_recently = False
                    try:
                        feature_with_stats = get_stats_for(feature)
                        feature_with_stats_conformed = conform_feature(feature_with_stats)
                        shp_out.write(feature_with_stats_conformed)
                        print('Success:', feature_with_stats_conformed['properties'][ID_FIELD_OUT])
                    except Exception as e:
                        print('Failed to write', f_id)
                        print(e)


if __name__ == '__main__':
    main()

