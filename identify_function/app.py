import boto3
import json
import rasterio as rio
import lib
from rasterio.crs import CRS
from rasterio.vrt import WarpedVRT

session = boto3.Session()

def lambda_handler(event, context):
  """
    AWS Lambda handler

    This method is invoked by the API Gateway: /identify/{proxy+} endpoint.
  """

  arn = context.invoked_function_arn
  stage = lib.get_stage(arn)
  params = event['queryStringParameters']

  response = get_identify(params, stage)

  return {
    "statusCode": 200,
    "body": json.dumps(response),
    "headers": {
      "Content-Type": 'application/json',
      "Access-Control-Allow-Origin": "*"
    }
  }


def get_identify(params, stage):

  config = lib.get_config(stage)
  data_source = lib.get_vrt_path(stage)

  dataset_names = lib.get_dataset_names(config)
  
  print(data_source)

  with rio.Env(GDAL_DISABLE_READDIR_ON_OPEN=True):
    with rio.open(data_source) as src:
      with WarpedVRT(src, crs='EPSG:4326') as vrt:

        if lib.runs_on_aws_lambda():
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
