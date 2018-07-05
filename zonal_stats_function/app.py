import boto3
import rasterio
import rasterio.mask
import numpy.ma as ma
import json
from rasterio.vrt import WarpedVRT

session = boto3.Session()

def runs_on_aws_lambda():
  """
    Returns True if this function is executed on AWS Lambda service.
  """
  return 'AWS_SAM_LOCAL' not in os.environ and 'LAMBDA_TASK_ROOT' in os.environ


def lambda_handler(event, context):
  """
    AWS Lambda handler

    This method is invoked by the API Gateway: /zonal_stats/{proxy+} endpoint.
  """

  geojson = json.loads(event['body'])
  response = get_response(geojson)

  return {
    "statusCode": 200,
    "body": json.dumps(response),
    "headers": {
      "Content-Type": 'application/json',
      "Access-Control-Allow-Origin": "*"
    }
  }


def get_response(geojson):

  index_names = [ 'asset', 'threat', 'exposure', 'aquatic', 'terrestrial', 'hubs' ]
  
  data_source = "s3://nfwf-tool/ALL_INDICES_CONUS.vrt"

  with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN=True):
    with rasterio.open(data_source) as src:
      with WarpedVRT(src, crs='EPSG:4326') as vrt:
        for feature in geojson['features']:
          geom = [ feature['geometry'] ]
          out_image, out_transform = rasterio.mask.mask(vrt, geom, crop=True)
          arr = ma.masked_outside(out_image, 0.0, 10.0)
          feature['mean'] = {}
          for i in range(0, len(arr)):
            index_name = index_names[i]
            mean = arr[i].mean()
            feature['mean'][index_name] = float(mean)

  return geojson
