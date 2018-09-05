'''
Utility functions used by many or all of the functions in the API.

The master copy of this file lives in the lib/ folder.
This is the only copy which should be edited directly, as it is then copied
into lambda function folders by a build script. Do not edit these copies!
'''

import os
import os.path
import boto3
import yaml
import pyproj


def get_proj():
  proj = pyproj.Proj(proj='aea', lat_1=29.5, lat_2=45.5, lat_0=37.5, lon_0=-96, x_0=0, y_0=0, datum='NAD83', units='m')
  return proj


def transform_polygon(coords):
  new_coords = []
  proj = get_proj()
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


def runs_on_aws_lambda():
  """
    Returns True if this function is executed on AWS Lambda service.
  """
  return 'AWS_SAM_LOCAL' not in os.environ and 'LAMBDA_TASK_ROOT' in os.environ


def get_stage(arn):
  if 'pytest' in arn:
    return 'test'
  elif not runs_on_aws_lambda() or 'dev' in arn or 'test' in arn:
    return 'dev'
  return 'prod'


def get_dataset_names(config):
  names = list(map(lambda dataset: dataset['name'], config['datasets']))
  return names


def get_vrt_path(stage):
  if stage == 'dev':
    filename = os.environ['VRT_FILE_DEV']
  elif stage == 'test':
    filename = os.environ['VRT_FILE_TEST']
  else:
    filename = os.environ['VRT_FILE_PROD']
  return os.path.abspath(filename)


def get_config(stage):
  if stage == 'dev':
    file_path = os.environ['CONFIG_FILE_DEV']
  elif stage == 'test':
    file_path = os.environ['CONFIG_FILE_TEST']
  else:
    file_path = os.environ['CONFIG_FILE_PROD']
  with open(file_path, 'r') as stream:
    config = yaml.safe_load(stream)
  return config
