try:
  import unzip_requirements
except ImportError:
  pass
import geojson, json

def lambda_handler(event, context):

  params = event['queryStringParameters']
  response = get_geojson_data(params)

  return {
    "statusCode": 200,
    "body": json.dumps(response),
    "headers": {
      "Content-Type": 'application/json',
      "Access-Control-Allow-Origin": "*"
    }
  }


def get_geojson_data(params):
  region = params['region']
  name = params['name']
  file_to_read = params['fileToRead']
  geojson_files = {
    'atlantic_gulf_pacific_states': 'atlantic_gulf_pacific_states.geojson',
    'atlantic_gulf_pacific_counties': 'atlantic_gulf_pacific_counties.geojson'
  }
  zonalStats = ["aquatic", "asset", "crit_fac", "crit_infra", "drainage", "erosion", "exposure", "floodprone", "geostress", "hubs", "pop_dens", "slope", "slr", "soc_vuln", "stormsurge", "terrestri", "threat", "wildlife"]
  geojson_to_read = geojson_files[file_to_read]  

  with open(geojson_to_read) as f:
   gj = geojson.load(f)

  features = gj["features"]
  selectedFeature = [ft for ft in features if ft.properties["areaName"] == name][0]
  response = { "type": "Feature", "geometry": {}, "properties": { "areaName": None, "GEOID": None, "region": region, "zonalStatsData": {} }}
  response["geometry"] = selectedFeature["geometry"]
  response["properties"]["areaName"] = selectedFeature["properties"]["areaName"]
  response["properties"]["GEOID"] = selectedFeature["properties"]["GEOID"]
  for x in zonalStats:
    response["properties"]["zonalStatsData"][x] = selectedFeature["properties"][x]
  print(response)
  return response
