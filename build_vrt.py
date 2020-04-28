#!/usr/bin/env python

'''
A CLI utility for building the VRT raster that points to S3-hosted NFWF model datasets.

Relies on a config file in the root directory.
'''

import os, os.path, sys
import click, yaml
import rasterio as rio
import xml.etree.ElementTree as ET

vrtnodata_arg = '-vrtnodata {0}'
extent_arg = '-te {0}'
band_arg = '-b {0}'

def get_config(file_path):
  with open(file_path) as f:
    config = yaml.safe_load(f)
  return config

@click.command()
@click.option('-f',
  default='config.yml',
  type=click.STRING,
  help=('Path to the config file')
)
@click.option('-region',
  default='continental_us',
  type=click.STRING,
  help=('Region to build VRT for')
)
@click.option('-b', default='1', show_default=True, type=click.STRING, help='Band number to fetch for each dataset.')
@click.option('-vrtnodata', default='255', show_default=True, help=('Value to set for NODATA on vrt band.'))
@click.option('-vsi', default='s3', type=click.Choice(['s3', 'tar', 'curl']),
  help=('Prepend a GDAL Virtual File System identifier to component dataset paths (vsis3, vsicurl, etc) -- see https://www.gdal.org/gdal_virtual_file_systems.html')
)
@click.option('-loc', type=click.Path(),
  help='If building a VRT for local datasets, use this option to supply the location of the data')
def build_full_vrt(f, region, b, vrtnodata, vsi, loc):
  config = get_config(f)
  if 'dataset_bucket' in config:
    dataset_bucket = config['dataset_bucket']
  else:
    dataset_bucket = None
  bands_config = config['datasets'][region]
  check_same_proj(bands_config, vsi, dataset_bucket, loc)
  bounds = get_largest_extent(bands_config, vsi, dataset_bucket, loc)
  main_tree = None
  main_root = None
  big_vrt_name = config['vrt'][region]
  for i in range(0, len(bands_config)):
    band_num = str(i+1)
    band_config = bands_config[i]
    temp_vrt = build_intermediate_vrt(band_config, bounds, b, vrtnodata, vsi, dataset_bucket, loc)
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


def check_same_proj(bands_config, vsi, dataset_bucket, loc):
  paths = [ get_dataset_path(c, vsi, dataset_bucket, loc) for c in bands_config ]
  proj_strings = []
  for p in paths:
    with rio.open(p) as src:
      proj_strings.append(src.profile['crs'].to_proj4())
  proj_last = proj_strings[0]
  for proj in proj_strings:
    if proj_last != proj:
      raise TypeError('All datasets must have the exact same projection!')


def get_largest_extent(bands_config, vsi, dataset_bucket, loc):
  def max_by_key(iterable, key):
    return max([ getattr(obj, key) for obj in iterable ])
  paths = [ get_dataset_path(c, vsi, dataset_bucket, loc) for c in bands_config ]
  bounds = []
  for p in paths:
    with rio.open(p) as src:
      bounds.append(src.bounds)
  max_bounds = [ max_by_key(bounds, key) for key in ('left', 'bottom', 'right', 'top') ]
  return max_bounds


def get_dataset_path(band_config, vsi, dataset_bucket, loc):
  path_pieces = []
  if loc:
    path_pieces.append(loc)
  elif vsi:
    path_pieces.append('/vsi{0}'.format(vsi))
    if dataset_bucket:
      path_pieces.append('{0}'.format(dataset_bucket))
  path_pieces.append(band_config['path'])
  full_path = os.path.join(*path_pieces)
  return full_path


def build_intermediate_vrt(band_config, bounds, b, vrtnodata, vsi, dataset_bucket, loc):
  command_pieces = [
    'gdalbuildvrt',
    vrtnodata_arg.format(vrtnodata),
    band_arg.format(b),
    '-overwrite'
  ]
  dataset_path = get_dataset_path(band_config, vsi, dataset_bucket, loc)
  temp_vrt = '{0}.vrt'.format(os.path.join('./', band_config['name']))
  bounds_string = ' '.join([ str(num) for num in bounds ])
  command_pieces.append(extent_arg.format(bounds_string))
  command_pieces.append("{0}".format(temp_vrt))
  command_pieces.append(dataset_path)
  c = ' '.join(command_pieces)
  click.echo(c)
  os.system(c)
  return temp_vrt


if __name__ == '__main__':
  build_full_vrt()
