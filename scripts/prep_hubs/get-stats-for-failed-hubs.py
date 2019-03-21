import json
import boto3
from zonal_stats_function import app

p = '/home/mgeiger/Projects/nfwf-meta/nfwf-tool-api/assets/hubs_failed_01042019/failed-hubs.v2.WGS84.geojson'
#p = '/home/mgeiger/Projects/nfwf-meta/nfwf-tool-api/assets/features/charleston-poly.geojson'
#p = '/home/mgeiger/Projects/nfwf-meta/nfwf-tool-api/9.geojson'

class LambdaContext:
  def __init__(self):
    self.invoked_function_arn = 'hi'

context = LambdaContext()

with open(p, 'r') as f:
    fc = json.loads(f.read())

def get_stats():
    event = { 'body': fc }
    ret = app.lambda_handler(event, context)
    print(ret)

get_stats()

