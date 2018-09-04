#!/usr/bin/env python

'''
A CLI utility for building the VRT raster that points to S3-hosted NFWF model datasets.

Relies on a config file in the root directory.
'''

import os
import os.path
import click
import yaml
import sys
import xml.etree.ElementTree as ET

# Move up one directory
_dir = os.path.dirname(os.path.abspath(os.path.join('..',__file__)))
os.chdir(_dir)

vrtnodata_arg = '-vrtnodata {0}'
extent_arg = '-te {0}'
band_arg = '-b {0}'

def get_config(stage):
  with open('config-{0}.yml'.format(stage)) as f:
    config = yaml.safe_load(f)
  return config

@click.command()
@click.option('-stage',
  default='dev',
  show_default=True,
  type=click.Choice(['dev', 'test', 'prod']),
  help='The stage to generate.'
)
@click.option('-te',
  type=click.STRING,
  help=(
    'Extent of VRT mosaic. To cover the continental US, try "-4954548.0 -2178809.0 4771843.0 3632558.0" (albers equal area). '
    'String of the form xmin ymin xmax ymax. '
    'The values must be expressed in georeferenced units.')
)
@click.option('-b', default='1', show_default=True, type=click.STRING, help='Band number to fetch for each dataset.')
@click.option('-vrtnodata', default='255', show_default=True, help=('Value to set for NODATA on vrt band.'))
@click.option('-vsi', type=click.Choice(['s3', 'tar', 'curl']),
  help=('Use a GDAL Virtual File System for component dataset paths -- see https://www.gdal.org/gdal_virtual_file_systems.html')
)
def build_full_vrt(stage, te, b, vrtnodata, vsi):
  config = get_config(stage)
  if 'dataset_bucket' in config:
    dataset_bucket = config['dataset_bucket']
  else:
    dataset_bucket = None
  bands_config = config['datasets']
  main_tree = None
  main_root = None
  for i in range(0, len(bands_config)):
    band_num = str(i+1)
    band_config = bands_config[i]
    vrt_path = build_intermediate_vrt(band_config, te, b, vrtnodata, vsi, dataset_bucket)
    if band_num == '1':
      main_tree = ET.parse(vrt_path)
      main_root = main_tree.getroot()
    else:
      tree = ET.parse(vrt_path)
      root = tree.getroot()
      bandElement = root.find('VRTRasterBand')
      bandElement.attrib['band'] = band_num
      main_root.append(bandElement)
    os.remove(vrt_path)
  big_vrt_name = 'ALL_DATASETS_CONUS_{0}.vrt'.format(stage.upper())
  main_tree.write(big_vrt_name)
  if stage == 'test':
    os.rename(big_vrt_name, './tests/data/{0}'.format(big_vrt_name))
  else:
    os.rename(big_vrt_name, './{0}'.format(big_vrt_name))


def build_intermediate_vrt(band_config, te, b, vrtnodata, vsi, dataset_bucket):
  path = ''
  if vsi:
    path += '/vsi{0}'.format(vsi)
    if dataset_bucket:
      path += '/{0}/'.format(dataset_bucket)
  if 'folder' in band_config:
    path += '{0}'.format(band_config['folder'])
  vrt_path = '{0}.vrt'.format(os.path.join('./tests/data/', band_config['name']))
  command_pieces = [
    'gdalbuildvrt',
    vrtnodata_arg.format(vrtnodata),
    extent_arg.format(te),
    band_arg.format(b),
    '-overwrite',
    "{0}".format(vrt_path),
  ]

  input_files = list(map(
    lambda f: os.path.join(path, f),
    band_config['input_files'])
  )
  command_pieces.extend(input_files)
  c = ' '.join(command_pieces)
  click.echo(c)
  os.system(c)
  return vrt_path

if __name__ == '__main__':
  build_full_vrt()
