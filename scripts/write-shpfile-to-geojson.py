#! /usr/bin/env python

import fiona
import sys, os, os.path
import click
import pyproj
import json
import subprocess
import requests
from fiona.crs import from_epsg

@click.command()
@click.option('-dir_out', type=click.Path(resolve_path=True))
@click.option('-id_field', type=str)
@click.argument('shpfile_path', type=click.Path(exists=True, resolve_path=True))
def main(shpfile_path, dir_out, id_field):
  with fiona.Env():
    with fiona.open(shpfile_path) as shpfile_read:
      for feature in shpfile_read:
        try:
          filename = '{0}.geojson'.format(feature['properties'][id_field])
          geojson = json.dumps(feature)
          file_path = os.path.join(dir_out, filename)
          with open(file_path, 'w') as f:
            print(geojson, file=f)
            print('Wrote file {0}...'.format(filename))
        except Exception as e:
          print('Error writing file for feature:')
          print(feature['properties'])
          print('Exception:\n  {0}'.format(e))

if __name__ == '__main__':
  main()
