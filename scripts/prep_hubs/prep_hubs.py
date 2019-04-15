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

IDS_DONE = []

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
            print('Finished writing feature: ', ID)
            with open(path, 'w') as f:
                f.write(json.dumps(updated_feature))
        else:
            print("Non-OK status code {0} for ID {1}".format(r.status_code, ID))
            print(fc_str)
            print(ZONAL_STATS_ENDPOINT)
            import pdb; pdb.set_trace()
    except Exception as e:
        print(e)
        print(f_str)


def getFieldMappedKey(key):
    new_key = FIELD_MAPS[key] if key in FIELD_MAPS else key
    return new_key


def conform_feature(path):
    with fiona.open(path) as fc:
        feature = fc[0]
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
        if new_key != key:
            props[new_key] = value
            props.pop(key, None)
    return new_feature


def write_new_shpfile(shpfile_path_out):
    with fiona.open(shpfile_path_out, 'w',
                    crs=from_epsg('4326'),
                    driver='ESRI Shapefile',
                    schema=SCHEMA_FOR_NEW_SHPFILE) as shp:
        for filename in os.listdir(HUBS_DONE_DIR):
            path = os.path.join(HUBS_DONE_DIR, filename)
            f = conform_feature(path)
            shp.write(f)


@click.command()
@click.argument('shpfile_path_in',
    type=click.Path(exists=True, resolve_path=True)
)
@click.argument('shpfile_path_out',
    type=click.Path(exists=False, resolve_path=True)
)
def main(shpfile_path_in, shpfile_path_out):

    # Skip any hub features that may already be processed
#    for filename in os.listdir(HUBS_DONE_DIR):
#        IDS_DONE.append(''.join(filename.split('.')[:-1]))
#    with fiona.Env():
#        with fiona.open(shpfile_path_in) as shpfile_read:
#            for feature in shpfile_read:
#                get_stats_for(feature)

    write_new_shpfile(shpfile_path_out)


if __name__ == '__main__':
    main()

