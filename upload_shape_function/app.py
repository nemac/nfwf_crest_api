import boto3
import os
import json

session = boto3.Session()

def lambda_handler(event, context):
  """
    AWS Lambda handler

    This method is invoked by the API Gateway: /zonal_stats/{proxy+} endpoint.
  """
  if runs_on_aws_lambda():
    geojson = json.loads(event['body'])
  else:
    geojson = event['body']

  