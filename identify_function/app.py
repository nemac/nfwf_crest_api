import boto3
import json
import os
import rasterio as rio
from rasterio.crs import CRS
from rasterio.vrt import WarpedVRT

session = boto3.Session()

def runs_on_aws_lambda():
  """
    Returns True if this function is executed on AWS Lambda service.
  """
  return 'AWS_SAM_LOCAL' not in os.environ and 'LAMBDA_TASK_ROOT' in os.environ


def lambda_handler(event, context):
  """
    AWS Lambda handler

    This method is invoked by the API Gateway: /identify/{proxy+} endpoint.
  """

  params = event['queryStringParameters']

  response = get_identify(params)

  return {
    "statusCode": 200,
    "body": json.dumps(response),
    "headers": {
      "Content-Type": 'application/json',
      "Access-Control-Allow-Origin": "*"
    }
  }


def get_identify(params):

  dataset_names = [ 'exposure', 'asset', 'threat', 'aquatic', 'terrestrial', 'hubs',
      'crit_infra', 'crit_facilities', 'pop_density', 'social_vuln', 'drainage',
      'erosion', 'floodprone_areas', 'geostress', 'sea_level_rise', 'slope',
      'storm_surge'
  ]

  data_source = "s3://nfwf-tool/ALL_DATASETS_CONUS.vrt"

  with rio.Env(GDAL_DISABLE_READDIR_ON_OPEN=True):
    with rio.open(data_source) as src:
      with WarpedVRT(src, crs='EPSG:4326') as vrt:

        if runs_on_aws_lambda():
          x = float(params['lng'])
          y = float(params['lat'])
        else:
          x = float(params['lng'][0])
          y = float(params['lat'][0])

        coords = [(x, y)]
        response = {}
        result_gen = vrt.sample(coords, list(range(1, len(dataset_names)+1)))
        result = next(result_gen)
        for i in range(0, len(dataset_names)):
          dataset_name = dataset_names[i]
          response[dataset_name] = str(result[i])

  return response
