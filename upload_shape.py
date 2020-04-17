import boto3
import os
import json
import hashlib
import os.path
from lib import lib

session = boto3.Session()

def lambda_handler(event, context):
  # The event body is either str or dict depending on runtime context
  try:
    request_body = json.loads(event['body'])
  except:
    request_body = event['body']

  s3_client = boto3.client('s3')

  geojson = json.dumps(request_body)
  config = util.get_config()

  content_type = 'application/json'
  bucket = config['user_shapes_bucket']

  geobytes = geojson.encode('utf-8')

  hash_id = hashlib.md5(geobytes).hexdigest()
  object_key = os.path.join('prod', hash_id)

  s3_client.put_object(
    Body=geobytes,
    Bucket=bucket,
    Key=object_key,
    ContentType=content_type,
    ACL='public-read'
  )

  metadata = {
    'key' : object_key,
    'bucket' : bucket
  }

  return {
    "statusCode": 200,
    "body": json.dumps(metadata),
    "headers": {
      "Content-Type": 'application/json',
      "Access-Control-Allow-Origin": "*"
    }
  }

