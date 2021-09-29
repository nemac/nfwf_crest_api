try:
  import unzip_requirements
except ImportError:
  pass
import json
import util
import rasterio as rio
from pyproj import Transformer

def lambda_handler(event, context):

  params = event['queryStringParameters']
  response = get_identify(params)

  return {
    "statusCode": 200,
    "body": json.dumps(response),
    "headers": {
      "Content-Type": 'application/json',
      "Access-Control-Allow-Origin": "*"
    }
  }


def get_identify(params):
  region = params['region']
  lng = float(params['lng'])
  lat = float(params['lat'])
  config = util.get_config()
  data_source = config['vrt'][region]
  dataset_names = util.get_dataset_names(config, region)
  
  with rio.Env(GDAL_DISABLE_READDIR_ON_OPEN=True):
    with rio.open(data_source) as src:
      proj_string = src.profile['crs'].to_proj4()
      transformer = Transformer.from_crs('epsg:4326', proj_string, always_xy=True)
      x,y = transformer.transform(lng, lat)
      coords = [(x, y)]

      result_gen = src.sample(coords, list(range(1, len(dataset_names)+1)))
      result = next(result_gen)

      response = {}
      for i in range(0, len(dataset_names)):
        dataset_name = dataset_names[i]
        response[dataset_name] = str(result[i])

  return response

