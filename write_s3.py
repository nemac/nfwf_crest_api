import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    json_data = event['state']
    
    s3.put_object(
        Body=json.dumps(json_data),
        Bucket='crest-v2-share-link',
        Key=event['location']
    )
