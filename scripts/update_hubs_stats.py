#! /usr/bin/env python

import pickle
import fiona
import sys, os
import json
import subprocess
import requests
import os.path
from collections import OrderedDict
from shapely.strtree import STRtree
from shapely.geometry import shape

# This only works if this script is called from the top level directory
sys.path.insert(0, os.path.abspath('.'))
from lib import lib

config = lib.get_config('prod')

# Local API must be started first: sam local start-api
zonal_stats_endpoint = 'http://127.0.0.1:3000/zonal_stats'

# Get the hubs shapefile
hubs_shp_filename = '/home/mgeiger/Projects/nfwf-tool-api/assets/hubs_test_082218/hubs_082218_matt.shp_WGS84.shp'

hubs_done_dir = '/home/mgeiger/Projects/nfwf-tool-api/assets/hubs_test_082218_with_stats/hubs_done/'

fc_template = '/home/mgeiger/Projects/nfwf-tool-api/assets/hubs_test_082218_with_stats/fc_template.geojson'

hubs_shp = fiona.open(hubs_shp_filename)

TARGET_FIDS = []

for filename in os.listdir(hubs_done_dir):
    TARGET_FIDS.append(''.join(filename.split('.')[:-1]))

def process(feature):
    ID = str(feature['properties']['TARGET_FID'])
    
    path = os.path.join(hubs_done_dir, ID+'.geojson')
    
    if ID in TARGET_FIDS:
        print('Skipping {0}...'.format(feature['properties']['TARGET_FID']))
        return 

    f_str = json.dumps(feature)

    fc = { "type": "FeatureCollection", "features": [ feature ] }
    fc_str = json.dumps(fc)
    try:
        r = requests.post(zonal_stats_endpoint, data=fc_str)
        if r.status_code == 200:
            try:
                os.remove(path)
            except:
                pass 
            updated_feature = r.json()['features'][0]
            with open(path, 'w') as f:
                f.write(json.dumps(updated_feature))
    except Exception as e:
        print(e)
        print(f_str)

for feature in hubs_shp:
    process(feature)

