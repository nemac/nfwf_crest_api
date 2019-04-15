# NFWF Tool API

GIS microservices built on the [AWS Serverless Application Model](https://docs.aws.amazon.com/lambda/latest/dg/serverless_app.html). 

### Requirements

* AWS CLI already configured with at least PowerUser permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Pipenv installed](https://github.com/pypa/pipenv)
    - `pip install pipenv`
* [Docker installed](https://www.docker.com/community-edition)
* [SAM Local installed](https://github.com/awslabs/aws-sam-local) 


### Getting Started

* Clone or fork this repository 
* Make a copy of the file `sample.env` called `.env`.  
* Initialize a local development environment: `pipenv install --dev`


### Add a new function

Let's say we have a function called `getData`.

* Create a new folder called "get_data_function"

* Add API endpoint settings to `template.yaml`

```yaml
Resources:
  ApiGatewayApi:
    Properties:
      ... 
      DefinitionBody:
        ... 
        paths:
          /get_data: # The endpoint URL path
            get: # The HTTP method to use
              produces:
              - application/json
              responses: {}
              x-amazon-apigateway-integration:
                uri: 
                  !Sub "arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${GetData.Arn}/invocations"
                httpMethod: GET
                type: aws_proxy
 
``` 

* Add function settings to `template.yaml`

```yaml
Resources:
  ...

  GetData: # Note that this identifier is referenced in the uri entry of the API settings above
    Type: AWS::Serverless::Function
    Properties:
  
      Policies:
        - AmazonS3ReadOnlyAccess
        - IAMReadOnlyAccess
      CodeUri: get_data_function/build/
      Handler: app.lambda_handler # This assumes there is a file called app.py with a function lambda_handler
      Runtime: python3.6 
      Events:
        PostApi:
          Type: Api
          Properties:
            Path: /get_data
            Method: POST
            RestApiId: !Ref ApiGatewayApi



```

* Add any new python dependencies to the Pipfile

* Add a subdirectory called `build` to the function folder

* Make a new file `app.py` in the `get_data_function` folder

* Import the utility library with `from lib import lib`

* Add a function called `lambda_handler` to `app.py`


### Packaging Functions  

Before we can run our function locally, we need to bundle all of its code and dependencies into the function's `build` folder. 

* Build all function packages: `pipenv run build_packages`

You don't need to re-package a function every time you change its `app.py` file. Simply copy `app.py` to the function's `build` folder when you are ready to test any changes.


### Invoke a Function Locally

We can use the SAM CLI to invoke a function in a docker container that mimics a Python Lambda execution environment. 

For example, we can mimic a POST method requesting zonal statistics for a polygonal region by supplying a geojson feature collection as a string through standard input:

```bash

# Get zonal statistics for a Polygon
echo '{ "body": { "type": "FeatureCollection","name": "charleston-poly","features": [{ "type": "Feature", "properties": { "id": null }, "geometry": { "type": "Polygon", "coordinates": [ [ [ -79.662208557128906, 32.920664249232836 ], [ -79.685039520263672, 32.930174118010605 ], [ -79.717311859130845, 32.906541649538447 ], [ -79.691219329833984, 32.895299602872463 ], [ -79.676971435546875, 32.902362080894527 ], [ -79.675083160400391, 32.909568110575655 ], [ -79.662208557128906, 32.920664249232836 ] ] ] } }]} }' | sam local invoke ZonalStatsFunction

# Get zonal statistics for a MultiPolygon 
echo '{ "body": { "type": "FeatureCollection", "name": "charleston-multi-poly", "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } }, "features": [{ "type": "Feature", "properties": { "id": null }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [-79.744316416802718, 32.918307771183919], [-79.758743269652271, 32.880394658156938], [-79.827024159455647, 32.910824100458811], [-79.793686860877372, 32.942719190317831], [-79.744316416802718, 32.918307771183919] ] ], [ [ [-79.662208557128906, 32.920664249232836], [-79.685039520263672, 32.930174118010605], [-79.717311859130845, 32.906541649538447], [-79.691219329833984, 32.895299602872463], [-79.676971435546875, 32.902362080894527], [-79.675083160400391, 32.909568110575655], [-79.662208557128906, 32.920664249232836] ] ] ] } }] }}' | sam local invoke ZonalStatsFunction

# Florida Keys Multipolygon (TIMING OUT)
echo '{ "body": {  "type": "FeatureCollection",  "name": "keys_multi",  "crs": {  "type": "name",  "properties": {  "name": "urn:ogc:def:crs:OGC:1.3:CRS84"  }  },  "features": [{  "type": "Feature",  "properties": {  "EZG_ID": 62145,  "prg_name": "Mote Marine Laboratory, Inc.",  "proj_name": "Florida Keys Coral Disease Response & Restoration Initiative",  "region": "Gulf",  "name": "Florida Keys Coral Disease Response & Restoration Initiative",  "id": 62145,  "area": 391374264.7,  "nfwf_proje": null,  "nfwf_pro_1": null,  "asset": null,  "threat": null,  "exposure": null,  "aquatic": null,  "terrestria": null,  "hubs": null,  "crit_infra": null,  "crit_facil": null,  "pop_densit": null,  "social_vul": null,  "drainage": null,  "erosion": null,  "floodprone": null,  "geostress": null,  "sea_level_": null,  "slope": null,  "storm_surg": null  },  "geometry": {  "type": "MultiPolygon",  "coordinates": [  [  [  [-81.302133056890256, 24.60695607607207],  [-81.808877441885357, 24.499532477742999],  [-81.815743897117486, 24.54326248601156],  [-81.306252930209197, 24.650648613252887],  [-81.302133056890256, 24.60695607607207]  ]  ],  [  [  [-80.10747716193147, 25.690925958783847],  [-80.167901966716897, 25.391066939726667],  [-80.209100697211582, 25.410915452360324],  [-80.155542347658283, 25.658745696291859],  [-80.10747716193147, 25.690925958783847]  ]  ]  ]  }  }] }}' | sam local invoke ZonalStatsFunction 

```

### Run a Local API

We can use the SAM CLI to spin up a local API: `sam local start-api`

Now that our local API is running we can test our `getData` function by hitting its API endpoint in a browser: `http://localhost:3000/get_data?config1=key1&config2=key2`. Since `getData` is a GET request, the only way we can pass configuration to the function is through the URL query string.

For POST requests, we can use cURL to pass function parameters via the body of the HTTP request:

```bnd 1 Block=128x128 Type=Byte, ColorInterp=Gray
  Min=1.000 Max=5.000
  Minimum=1.000, Maximum=5.000, Mean=1.441, StdDev=0.671
  NoData Value=255
  Metadata:
    STATISTICS_MAXIMUM=5
    STATISTICS_MEAN=1.4409758871493
    STATISTICS_MINIMUM=1
 ash
# Send a POST request to get zonal stats for geojson features.
 
curl -v -X POST \
'http://localhost:3000/zonal_stats' \
-H 'Content-Type: application/json' \
-d '{"type": "FeatureCollection","name": "charleston-poly","features": [{ "type": "Feature", "geometry": { "type": "Polygon", "coordinates": [ [ [ -79.662208557128906, 32.920664249232836 ], [ -79.685039520263672, 32.930174118010605 ], [ -79.717311859130845, 32.906541649538447 ], [ -79.691219329833984, 32.895299602872463 ], [ -79.676971435546875, 32.902362080894527 ], [ -79.675083160400391, 32.909568110575655 ], [ -79.662208557128906, 32.920664249232836 ] ] ] } }]}'
```


### Deployment

Instead of manually zipping function folders and uploading to S3, we'll use the SAM CLI `package` command to do it for us and generate a final "packaged" template. The packaged template is then used by [AWS CloudFormation](https://aws.amazon.com/cloudformation/) to create or update AWS resources for the API.

* Deploy API updates: `pipenv run deploy <stage>` where `<stage>` is either `dev` or `prod`.


### Testing the Live API

Once we've deployed our API, we can use cURL to quickly see the results of our API functions.

* Get the URLs of all of our API functions:

```bash
# Retrieve a json object with outputs defined in template.yaml
# For the production API use the stack name 'nfwf-tool-api' instead.

aws cloudformation describe-stacks --stack-name nfwf-tool-api-dev --query 'Stacks[].Outputs'
```

* Send the request with cURL:

```bash
curl -v -X POST \
'https://lg0njzoglg.execute-api.us-east-1.amazonaws.com/Dev/zonal_stats' \
-H 'Content-Type: application/json' \
-d '{"type": "FeatureCollection","name": "charleston-poly","features": [{ "type": "Feature", "geometry": { "type": "Polygon", "coordinates": [ [ [ -79.662208557128906, 32.920664249232836 ], [ -79.685039520263672, 32.930174118010605 ], [ -79.717311859130845, 32.906541649538447 ], [ -79.691219329833984, 32.895299602872463 ], [ -79.676971435546875, 32.902362080894527 ], [ -79.675083160400391, 32.909568110575655 ], [ -79.662208557128906, 32.920664249232836 ] ] ] } }]}'
```


### Running Unit Tests

* Build the [Virtual Raster Table](https://www.gdal.org/gdal_vrttut.html) used for local testing: `pipenv run test_prep`
* Run local tests with [Pytest](https://docs.pytest.org/en/latest/): `pipenv run tests` 


### Notes

- This repository was built with the help of [this project template](https://github.com/aws-samples/cookiecutter-aws-sam-python).
- Take a look at the `[scripts]` section of the Pipfile to see how commands used in this document are defined.
