#!/usr/bin/env python

import boto3
import os
import os.path
import yaml
import sys
import rasterio as rio
import glob
from copy import deepcopy
from rasterio.features import geometry_window
from rasterio.windows import transform as win_transform

# Import utility functions
sys.path.insert(0, os.path.abspath('.'))
from lib import lib

DATA_DIR = os.path.join('.', 'tests', 'data')

session = boto3.Session()

geometry = {
  "type": "Polygon",
  "coordinates": [
    [
      [
        -80.01149654388428,
        32.887677980874706
      ],
      [
        -80.01911401748657,
        32.88337138447869
      ],
      [
        -80.01553058624268,
        32.87764094428261
      ],
      [
        -80.00417947769165,
        32.882578515468
      ],
      [
        -80.01149654388428,
        32.887677980874706
      ]
    ]
  ]
}


with open('config-prod.yml', 'r') as stream:
  config = yaml.safe_load(stream)

data_source = './ALL_DATASETS_CONUS_PROD.vrt'

dataset_names = lib.get_dataset_names(config)

with rio.Env(GDAL_DISABLE_READDIR_ON_OPEN=True):
  with rio.open(data_source) as src:
    geom_latlng = deepcopy(geometry)
    geom_albers = lib.transform_geom(geom_latlng)
    geom = [ geom_albers ]
    out_meta = src.meta.copy()
    window = geometry_window(src, geom)
    out_shape = (int(window.height), int(window.width))
    out_transform = src.window_transform(window)
    out_meta.update({"driver": "GTiff",
                     "height": window.height,
                     "width": window.width,
                     "transform": win_transform(window, src.transform),
                     "count": 1,
                    })
    for i in range(0, len(dataset_names)):
      band_num = i+1
      index_name = dataset_names[i]
      out = src.read(indexes=band_num, window=window)
      file_handle = os.path.join(DATA_DIR, '{0}_sample.tif'.format(index_name))
      os.remove(file_handle)
      with rio.open(file_handle, 'w', **out_meta) as dest:
        dest.write(out, indexes=1)

