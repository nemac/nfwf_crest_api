import boto3
import json
import os


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
    message = get_message()


    return {
        "statusCode": 200,
        "body": json.dumps(message)
    }


def get_message():
    return { "hello": "world" }
