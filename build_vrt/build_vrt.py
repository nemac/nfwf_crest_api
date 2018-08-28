#!/usr/bin/env python

import os
import os.path
import click
import yaml
import sys
import xml.etree.ElementTree as ET

GDAL_DRIVER = 'vsis3'

vrtnodata_arg = '-vrtnodata {0}'
extent_arg = '-te {0}'
band_arg = '-b {0}'

with open('../config.yml') as f:
  config = yaml.safe_load(f)

dataset_bucket = config['dataset_bucket']
bands = config['datasets']

@click.command()
@click.option('-te',
  default='-4954548.0 -2178809.0 4771843.0 3632558.0',
  show_default=True,
  type=click.STRING,
  help=(
    'Extent of VRT mosaic. The default value covers the continental U.S. '
    'String of the form xmin ymin xmax ymax. '
    'The values must be expressed in georeferenced units.')
)
@click.option('-b', default='1', show_default=True, type=click.STRING, help='Band number to fetch for each dataset.')
@click.option('-vrtnodata', default='255', show_default=True, help=('Value to set for NODATA on vrt band.'))
def build_full_vrt(te, b, vrtnodata):
  main_tree = None
  main_root = None
  for i in range(0, len(bands)):
    band_num = str(i+1)
    band = bands[i]
    vrt_path = build_intermediate_vrt(band, te, b, vrtnodata)
    if band_num == '1':
      main_tree = ET.parse(vrt_path)
      main_root = main_tree.getroot()
    else:
      tree = ET.parse(vrt_path)
      root = tree.getroot()
      bandElement = root.find('VRTRasterBand')
      bandElement.attrib['band'] = band_num
      main_root.append(bandElement)
  main_tree.write('ALL_DATASETS_CONUS.vrt')


def build_intermediate_vrt(band, te, b, vrtnodata):
  try:
    folder = band['folder']
  except:
    folder = ''
  vrt_path = '{0}.vrt'.format(os.path.join('.', band['name']))
  command_pieces = [
    'gdalbuildvrt',
    vrtnodata_arg.format(vrtnodata),
    extent_arg.format(te),
    band_arg.format(b),
    '-overwrite',
    "{0}".format(vrt_path),
  ]
  input_files = list(map(
    lambda f: os.path.join('/', GDAL_DRIVER, dataset_bucket, folder, f),
    band['input_files'])
  )
  command_pieces.extend(input_files)
  c = ' '.join(command_pieces)
  click.echo(c)
  os.system(c)
  return vrt_path

if __name__ == '__main__':
  build_full_vrt()
