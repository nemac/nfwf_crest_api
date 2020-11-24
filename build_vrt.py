#!/usr/bin/env python

'''
A CLI utility for building the VRT raster that points to S3-hosted NFWF model datasets.

Relies on a config file in the root directory.
'''

import os, os.path, sys, argparse
import yaml
import rasterio as rio
import xml.etree.ElementTree as ET

vrtnodata_arg = '-vrtnodata {0}'
extent_arg = '-te {0}'
band_arg = '-b {0}'


def get_config(file_path):
  with open(file_path) as f:
    config = yaml.safe_load(f)
  return config


def build_full_vrt(f, region, b, vrtnodata, vsi, dir_path, is_local):
  config = get_config(f)
  if 'dataset_bucket' in config:
    dataset_bucket = config['dataset_bucket']
  else:
    dataset_bucket = None
  bands_config = config['datasets'][region]
  check_same_proj(bands_config, vsi, dataset_bucket, dir_path, is_local)
  bounds = get_largest_extent(bands_config, vsi, dataset_bucket, dir_path, is_local)
  main_tree = None
  main_root = None
  big_vrt_name = config['vrt'][region]
  for i in range(0, len(bands_config)):
    band_num = str(i+1)
    band_config = bands_config[i]
    temp_vrt = build_intermediate_vrt(band_config, bounds, b, vrtnodata, vsi, dataset_bucket, dir_path, is_local)
    if band_num == '1':
      main_tree = ET.parse(temp_vrt)
      main_root = main_tree.getroot()
    else:
      tree = ET.parse(temp_vrt)
      root = tree.getroot()
      bandElement = root.find('VRTRasterBand')
      bandElement.attrib['band'] = band_num
      main_root.append(bandElement)
    os.remove(temp_vrt)
  main_tree.write(big_vrt_name)


def check_same_proj(bands_config, vsi, dataset_bucket, dir_path, is_local):
  paths = [ get_dataset_path(c, vsi, dataset_bucket, dir_path, is_local) for c in bands_config ]
  proj_strings = []
  for p in paths:
    with rio.open(p) as src:
      proj_strings.append(src.profile['crs'].to_proj4())
  proj_last = proj_strings[0]
  for proj in proj_strings:
    if proj_last != proj:
      raise TypeError('All datasets must have the exact same projection!')


def get_largest_extent(bands_config, vsi, dataset_bucket, dir_path, is_local):
  def max_by_key(iterable, key):
    return max([ getattr(obj, key) for obj in iterable ])
  paths = [ get_dataset_path(c, vsi, dataset_bucket, dir_path, is_local) for c in bands_config ]
  bounds = []
  for p in paths:
    with rio.open(p) as src:
      bounds.append(src.bounds)
  max_bounds = [ max_by_key(bounds, key) for key in ('left', 'bottom', 'right', 'top') ]
  return max_bounds


def get_dataset_path(band_config, vsi, dataset_bucket, dir_path, is_local):
  path_pieces = []
  if not is_local:
    path_pieces.append('{0}'.format(vsi))
    if dataset_bucket:
      path_pieces.append('{0}'.format(dataset_bucket))
  if dir_path:
    path_pieces.append(dir_path)
  path_pieces.append(band_config['path'])
  full_path = os.path.join(*path_pieces)
  return full_path


def build_intermediate_vrt(band_config, bounds, b, vrtnodata, vsi, dataset_bucket, dir_path, is_local):
  command_pieces = [
    'gdalbuildvrt',
    vrtnodata_arg.format(vrtnodata),
    band_arg.format(b),
    '-overwrite'
  ]
  dataset_path = get_dataset_path(band_config, vsi, dataset_bucket, dir_path, is_local)
  temp_vrt = '{0}.vrt'.format(os.path.join('./', band_config['name']))
  bounds_string = ' '.join([ str(num) for num in bounds ])
  command_pieces.append(extent_arg.format(bounds_string))
  command_pieces.append("{0}".format(temp_vrt))
  command_pieces.append(dataset_path)
  c = ' '.join(command_pieces)
  print(c)
  os.system(c)
  return temp_vrt


def setup_arg_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', '--config',
    metavar='config.yml', default='config.yml',
    help='Path to the config file'
  )
  parser.add_argument('-b', '--band',
    dest='target_raster_band', metavar='1', default='1',
    help='Band number to use for each raster'
  )
  parser.add_argument('--vrtnodata', default='255', metavar='255',
    help='Value to set for NODATA in the VRT'
  )
  parser.add_argument('--region', '-r',
    help='Region to build VRT for as defined in config file.'
  )
  parser.add_argument('--vsistring', default='/vsis3/', metavar='/vsis3/',
    help='Chain of GDAL VSI drivers to use for accessing source data.'
  )
  parser.add_argument('--local', action='store_true',
    help='Use local datasets instead of cloud-hosted datasets. The value of --vsistring will not be used if this flag is used. The default config file will change to config.local.yml, which can be overridden by the -c flag.'
  )
  # TODO make sure this works for cloud and disk
  #  - vrt driver string needs to come first in cloud case
  parser.add_argument('--path', '-p',
    help='Folder path to prepend to any file paths defined in the config file.'
  )
  return parser


# TODO tests
# TODO don't overwrite files unless told to
# TODO license
if __name__ == '__main__':
  parser = setup_arg_parser()
  args = parser.parse_args()
  f = args.config if not args.local else 'config.local.yml'
  b = args.target_raster_band
  vsi = args.vsistring if not args.local else None
  build_full_vrt(f, args.region, b, args.vrtnodata, vsi, args.path, args.local)
