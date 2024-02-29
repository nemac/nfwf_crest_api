import json
import boto3

def lambda_handler(event, context):
  s3 = boto3.client('s3')
  # Parse the JSON body
  body = json.loads(event['body'])
  state = body['state']
  location = body['location']
    
  s3.put_object(
    Body=json.dumps(state).encode(),
    Bucket='crest-v2-share-link',
    Key=location
  )

  return {
    'statusCode': 200,
    'body': 'Write to S3 successful: ' + location,
    "headers": {
      "Content-Type": '*/*',
      "Access-Control-Allow-Origin": "*"
    }
  }
