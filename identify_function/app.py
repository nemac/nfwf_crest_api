import boto3
import json
import os
import rasterio as rio

def runs_on_aws_lambda():
    """
        Returns True if this function is executed on AWS Lambda service.
    """
    return 'AWS_SAM_LOCAL' not in os.environ and 'LAMBDA_TASK_ROOT' in os.environ

session = boto3.Session()


def lambda_handler(event, context):
    """
        AWS Lambda handler

        This method is invoked by the API Gateway: /Prod/first/{proxy+} endpoint.
    """

    response = get_identify(event)

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }


def get_identify(event):

    data_source = "s3://nfwf-tool/NA_AssetThreatIndexAsBands.tif"

    # coords = [ (1745727, 451980) ]
    coords = [ (float(event['x']), float(event['y'])) ]

    # Band 1 = Asset Index
    # Band 2 = Threat Index

    bands = (1, 2)

    response = {}

    with rio.open(data_source) as src:
        result_gen = src.sample(coords, bands)
        result = next(result_gen)
        response['asset'] = str(result[0])
        response['threat'] = str(result[1])
        response['exposure'] = str(result[0] * result[1])

    return response
