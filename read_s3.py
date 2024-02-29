import json
import boto3

def lambda_handler(event, context):
    try:
        params = event['queryStringParameters']
        s3 = boto3.resource('s3')
        s3ObjectLocation = params['shareUrl'] + '.json'
        s3Object = s3.Object('crest-v2-share-link', s3ObjectLocation)
        file_content = s3Object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        return {
            'statusCode': 200,
            'body': json.dumps(json_content),
            "headers": {
                "Content-Type": '*/*',
                "Access-Control-Allow-Origin": "*"
            }
        }
    except:
        return {
            'statusCode': 400,
            'body': 'could not find ' + params['shareUrl'] + ' share url.',
            "headers": {
                "Content-Type": '*/*',
                "Access-Control-Allow-Origin": "*"
            }
        }
