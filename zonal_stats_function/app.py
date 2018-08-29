import boto3
import os
import json
import pyproj
import lib
from rasterio import Env, open
from rasterio.mask import mask
from numpy.ma import masked_outside
from numpy import isnan
from copy import deepcopy

session = boto3.Session()

def lambda_handler(event, context):
  """
    AWS Lambda handler

    This method is invoked by the API Gateway: /zonal_stats/{proxy+} endpoint.
  """

  if lib.runs_on_aws_lambda():
    geojson = json.loads(event['body'])
  else:
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


def transform_polygon(coords):
  new_coords = []
  proj = lib.get_proj()
  for coord in coords:
    coord = list(proj(*coord))
    new_coords.append(coord)
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


def get_zonal_stat(arr, statistic):
  if statistic == 'mean':
    result = arr.mean()
  elif statistic == 'sum':
    result = arr.sum()

  if isnan([result]):
    result = "NaN"
  else:
    result = float(result)
  return result


def get_response(geojson, stage):

  config = lib.get_config(stage)
  data_source = lib.get_vrt_path(stage)

  dataset_names = lib.get_dataset_names(config)

  with Env(GDAL_DISABLE_READDIR_ON_OPEN=True):
    with open(data_source) as src:
      for feature in geojson['features']:
        geom_latlng = deepcopy(feature['geometry'])
        geom_albers = transform_geom(geom_latlng)
        geom = [ geom_albers ]
        out_image, out_transform = mask(src, geom, pad=True, crop=True)
        arr = masked_outside(out_image, 0.0, 100.0)
        feature['properties']['mean'] = {}
        feature['properties']['sum'] = {}
        for i in range(0, len(arr)):
          index_name = dataset_names[i]
          mean = get_zonal_stat(arr[i], 'mean')
          total = get_zonal_stat(arr[i], 'sum')
          feature['properties']['mean'][index_name] = mean
          feature['properties']['sum'][index_name] = total

  return geojson

