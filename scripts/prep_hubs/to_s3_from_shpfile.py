#! /usr/bin/env python

import fiona
import sys, os, os.path
import click
import pyproj
import json
import subprocess
import boto3
from fiona.crs import from_epsg

sys.path.insert(1, '.')
from upload_shape_function import app


class LambdaContext:
  def __init__(self):
    self.invoked_function_arn = 'hi'

context = LambdaContext()


@click.command()
@click.argument('shpfile_path',
  type=click.Path(exists=True, resolve_path=True)
)
def main(shpfile_path):
  with fiona.Env():
    with fiona.open(shpfile_path) as shpfile_read:
      for feature in shpfile_read:
        event = { 'body': feature }
        # Hack to make sure stage is 'prod'
        os.environ['LAMBDA_TASK_ROOT'] = 'hi'
        try:
          ret = app.lambda_handler(event, context)
          print('Status={0}'.format(ret['statusCode']))
        except Exception as e:
          print(ret)


if __name__ == '__main__':
  main()

