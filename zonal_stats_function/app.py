import boto3
import os
import json
import pyproj
from rasterio import Env, open
from rasterio.mask import mask
from numpy.ma import masked_outside
from numpy import isnan
from copy import deepcopy
from lib import lib

session = boto3.Session()

def lambda_handler(event, context):
  """
    AWS Lambda handler

    This method is invoked by the API Gateway: /zonal_stats/{proxy+} endpoint.
  """

  try:
    geojson = json.loads(event['body'])
  except:
    geojson = event['body']

  arn = context.invoked_function_arn
  stage = lib.get_stage(arn)

  response = get_response(geojson, stage)

  return {
    "statusCode": 200,
    "body": json.dumps(response),
    "headers": {
      "Content-Type": 'application/json',
      "Access-Control-Allow-Origin": "*"
    }
  }


def get_zonal_stat(arr):
  result = arr.mean()
  if isnan([result]):
    result = "NaN"
  else:
    result = float(result)
  return result


def get_response(geojson, stage):

  config = lib.get_config(stage)
  data_source = lib.get_vrt_path(stage)
  print(data_source)

  dataset_names = lib.get_dataset_names(config)

  with Env(GDAL_DISABLE_READDIR_ON_OPEN=True):
    with open(data_source) as src:
      for feature in geojson['features']:
        geom_latlng = deepcopy(feature['geometry'])
        geom_albers = lib.transform_geom(geom_latlng)
        geom = [ geom_albers ]
        out_image, out_transform = mask(src, geom, pad=True, crop=True)
        arr = masked_outside(out_image, 0.0, 100.0)
        if 'properties' not in feature:
          feature['properties'] = {}
        feature['properties']['mean'] = {}
        for i in range(0, len(arr)):
          index_name = dataset_names[i]
          mean = get_zonal_stat(arr[i])
          feature['properties']['mean'][index_name] = mean

  return geojson

