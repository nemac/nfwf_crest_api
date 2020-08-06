<<<<<<< HEAD
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
* Update `.env` with your AWS api keys to the .env file
* You may have to change the certs to the Operating System specific cert directory
* You may have to update the `LC_ALL` and `LANG` to `en_US.UTF-8` depending on OS (mac vs linux)
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
=======
# CREST API
>>>>>>> update-spring-2020

The serverless API powering the National Fish and Wildlife Foundation's [Coastal Resilience Evaluation and Siting Tool (CREST)](https://resilientcoasts.org).

## Setting up the environment

This repository uses the Serverless Framework to build, run, and test a serverless HTTP API that runs on AWS Lambda on the Python 3.8 runtime. In order to test locally you will need to install Python 3.8.


<<<<<<< HEAD
* consider installing [pyenv](https://github.com/pyenv/pyenv#installation) and installing a [local](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-local) version of [python](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-install) 

* Add a subdirectory called `build` to the function folder
=======
### Installing Python 3.8 using pyenv (Optional)
>>>>>>> update-spring-2020

We recommend using pyenv to manage Python installations.

- Install [pyenv](https://github.com/pyenv/pyenv#installation).

- Follow any instructions at the end of the install logs.

- Restart your terminal.

- Run `pyenv install 3.8.2` in your terminal to install Python 3.8.2. Now when you run `pyenv versions` you should see `3.8.2` in your list of Python installations. Try `pyenv install -l` to see a full list of versions you can install. Check out the full pyenv README for more information.

<<<<<<< HEAD
Before we can run our function locally, we need to bundle all of its code and dependencies into the function's `build` folder.

* Build all function packages: `pipenv run build --deps`
=======

### Set up a virtual environment (Recommended)
>>>>>>> update-spring-2020

A virtual environment is a Python abstraction that allows you to create an isolated Python environment.

There are several ways to set up virtual environments. Here are a few options:

- [Pipenv](https://pipenv.pypa.io/en/latest/) is a well-supported environment manager. It plays nicely with pyenv as well. Once Pipenv is installed run `pipenv install -r requirements.txt` to set up your virtual environment and install dependencies.

<<<<<<< HEAD
We can use the SAM CLI to invoke a function in a docker container that mimics a Python Lambda execution environment.
=======
- If you're using pyenv on Linux or macOS, you can use the [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv#pyenv-virtualenv) pyenv plugin.
>>>>>>> update-spring-2020

- Python 3's built-in module [venv](https://docs.python.org/3/library/venv.html).

- There's always the classic [virtualenv](https://virtualenv.pypa.io/en/latest/) library. If you go this route you might want to check out the popular tool [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/stable/).


<<<<<<< HEAD
# Get zonal statistics for a MultiPolygon
echo '{ "body": { "type": "FeatureCollection", "name": "charleston-multi-poly", "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } }, "features": [{ "type": "Feature", "properties": { "id": null }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [-79.744316416802718, 32.918307771183919], [-79.758743269652271, 32.880394658156938], [-79.827024159455647, 32.910824100458811], [-79.793686860877372, 32.942719190317831], [-79.744316416802718, 32.918307771183919] ] ], [ [ [-79.662208557128906, 32.920664249232836], [-79.685039520263672, 32.930174118010605], [-79.717311859130845, 32.906541649538447], [-79.691219329833984, 32.895299602872463], [-79.676971435546875, 32.902362080894527], [-79.675083160400391, 32.909568110575655], [-79.662208557128906, 32.920664249232836] ] ] ] } }] }}' | sam local invoke ZonalStatsFunction

# Florida Keys Multipolygon (TIMING OUT)
echo '{ "body": {  "type": "FeatureCollection",  "name": "keys_multi",  "crs": {  "type": "name",  "properties": {  "name": "urn:ogc:def:crs:OGC:1.3:CRS84"  }  },  "features": [{  "type": "Feature",  "properties": {  "EZG_ID": 62145,  "prg_name": "Mote Marine Laboratory, Inc.",  "proj_name": "Florida Keys Coral Disease Response & Restoration Initiative",  "region": "Gulf",  "name": "Florida Keys Coral Disease Response & Restoration Initiative",  "id": 62145,  "area": 391374264.7,  "nfwf_proje": null,  "nfwf_pro_1": null,  "asset": null,  "threat": null,  "exposure": null,  "aquatic": null,  "terrestria": null,  "hubs": null,  "crit_infra": null,  "crit_facil": null,  "pop_densit": null,  "social_vul": null,  "drainage": null,  "erosion": null,  "floodprone": null,  "geostress": null,  "sea_level_": null,  "slope": null,  "storm_surg": null  },  "geometry": {  "type": "MultiPolygon",  "coordinates": [  [  [  [-81.302133056890256, 24.60695607607207],  [-81.808877441885357, 24.499532477742999],  [-81.815743897117486, 24.54326248601156],  [-81.306252930209197, 24.650648613252887],  [-81.302133056890256, 24.60695607607207]  ]  ],  [  [  [-80.10747716193147, 25.690925958783847],  [-80.167901966716897, 25.391066939726667],  [-80.209100697211582, 25.410915452360324],  [-80.155542347658283, 25.658745696291859],  [-80.10747716193147, 25.690925958783847]  ]  ]  ]  }  }] }}' | sam local invoke ZonalStatsFunction
=======
### Install dependencies

- Install [nodejs](https://nodejs.org/en/) if you don't have it already. Make sure to choose the LTS version.
>>>>>>> update-spring-2020

- Install the [Serverless Framework](https://serverless.com/framework/docs/getting-started/) using npm: `npm install -g serverless`.

- Unless you're using Pipenv, you'll need to activate your virtual environment (see the documentation for your virtual environment manager). Once you've activated your environment, run `pip install -r requirements.txt`. If you're using pipenv the install command you used above does this for you.

- Install serverless dependencies: `npm install`


## Run a local API

You can use Serverless Offline to spin up a local API that you can use while you're developing:

```bash
<<<<<<< HEAD
# Send a POST request to get zonal stats for geojson features.

curl -v -X POST \
'http://localhost:3000/zonal_stats' \
-H 'Content-Type: application/json' \
-d '{"type": "FeatureCollection","name": "charleston-poly","features": [{ "type": "Feature", "geometry": { "type": "Polygon", "coordinates": [ [ [ -79.662208557128906, 32.920664249232836 ], [ -79.685039520263672, 32.930174118010605 ], [ -79.717311859130845, 32.906541649538447 ], [ -79.691219329833984, 32.895299602872463 ], [ -79.676971435546875, 32.902362080894527 ], [ -79.675083160400391, 32.909568110575655 ], [ -79.662208557128906, 32.920664249232836 ] ] ] } }]}'
=======
serverless offline
>>>>>>> update-spring-2020
```

You should see something like this:

```
offline: Starting Offline: dev/us-east-1.
offline: Offline [http for lambda] listening on http://localhost:3002

   ┌───────────────────────────────────────────────────────────────────────────────┐
   │                                                                               │
   │   GET  | http://localhost:3000/dev/identify                                   │
   │   POST | http://localhost:3000/2015-03-31/functions/identify/invocations      │
   │   POST | http://localhost:3000/dev/zonal_stats                                │
   │   POST | http://localhost:3000/2015-03-31/functions/zonal_stats/invocations   │
   │                                                                               │
   └───────────────────────────────────────────────────────────────────────────────┘

offline: [HTTP] server ready: http://localhost:3000 🚀
offline:
offline: Enter "rp" to replay the last request
```

Test your local API with curl:

```bash
# Identify example
curl http://localhost:3000/dev/identify/\?lng\=-82.8\&lat\=35.8\&region=conus

<<<<<<< HEAD
* Note when deploying you **must** build the vrt, build the the dependencies, and finish with the deploy.  The order is important

* example for building and deploying the api to dev: **The order is important!**
```bash
pipenv run build_vrt -stage dev
pipenv run build --deps
pipenv run deploy dev
```

* Deploy API updates: `pipenv run deploy <stage>` where `<stage>` is either `dev` or `prod`.
=======
# CNMI
curl http://localhost:3000/dev/identify/\?lng\=-145.72\&lat\=15.2\&region=cnmi
>>>>>>> update-spring-2020




# Zonal stats example (polygon)
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"type": "FeatureCollection","name": "test-ar","features": [{"type": "Feature","properties": {"id": null},"geometry": {"type": "Polygon","coordinates": [[[-80.01149654388428, 32.887677980874706],[-80.01911401748657, 32.88337138447869],[-80.01553058624268, 32.87764094428261],[-80.00417947769165, 32.882578515468],[-80.01149654388428, 32.887677980874706]]]}}]}' \
  http://localhost:3000/dev/zonal_stats?region=continental_us

# Northern Mariana Islands (CNMI)
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":[[[145.77878952026367,15.228125499059319],[145.77394008636475,15.225475339228003],[145.7759141921997,15.221707085774053],[145.78372478485107,15.222328231095478],[145.78308105468747,15.226013655644088],[145.77878952026367,15.228125499059319]]]}}]}' \
  http://localhost:3000/dev/zonal_stats?region=northern_mariana_islands




# Zonal stats example (multipolygon)
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"type": "FeatureCollection","name": "test-ar","features": [{"type": "Feature","properties": {"id": null},"geometry": {"type": "Polygon","coordinates": [[[-80.01149654388428, 32.887677980874706],[-80.01911401748657, 32.88337138447869],[-80.01553058624268, 32.87764094428261],[-80.00417947769165, 32.882578515468],[-80.01149654388428, 32.887677980874706]]]}}]}' \
  http://localhost:3000/dev/zonal_stats?region=conus

# Upload shape example
curl \
  --header 'Content-Type: application/json' \
  --data '{"type": "FeatureCollection","name": "charleston-poly","features": [{ "type": "Feature", "geometry": { "type": "Polygon", "coordinates": [ [ [ -79.662208557128906, 32.920664249232836 ], [ -79.685039520263672, 32.930174118010605 ], [ -79.717311859130845, 32.906541649538447 ], [ -79.691219329833984, 32.895299602872463 ], [ -79.676971435546875, 32.902362080894527 ], [ -79.675083160400391, 32.909568110575655 ], [ -79.662208557128906, 32.920664249232836 ] ] ] } }]}' \
  http://localhost:3000/beta/upload_shape
```

## Deploy the API

We use two API stages: *beta* and *prod*. When you're ready to deploy, run `serverless deploy --stage stage-name`.

Deploy to beta:

```bash
serverless deploy --stage beta
```

Deploy to prod:

<<<<<<< HEAD
### Running Unit Tests

* Build the [Virtual Raster Table](https://www.gdal.org/gdal_vrttut.html) used for local testing: `pipenv run test_prep`
* Run local tests with [Pytest](https://docs.pytest.org/en/latest/): `pipenv run tests`
=======
```bash
serverless deploy --stage prod
```
>>>>>>> update-spring-2020

## To Do

- Test VRT integrity by cross-referencing VRT-based results with results from individual datasets using `gdallocationinfo`

