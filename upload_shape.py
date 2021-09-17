try:
  import unzip_requirements
except ImportError:
  pass
import boto3, os, json, hashlib, os.path
import util

def handler(event, context):

	session = boto3.Session()
	s3_client = boto3.client('s3')
	config = util.get_config()

	# The event body is either str or dict depending on runtime context
	try:
		request_body = json.loads(event['body'])
	except:
		request_body = event['body']

	geojson = json.dumps(request_body)
	geobytes = geojson.encode('utf-8')

	bucket = config['user_shapes_bucket']
	params = event['queryStringParameters']

	hash_id = hashlib.md5(geobytes).hexdigest()
	stage = os.environ['STAGE']
	object_key = os.path.join(stage, hash_id)

	s3_client.put_object(
		Body=geobytes,
		Bucket=bucket,
		Key=object_key,
		ContentType='application/json',
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

