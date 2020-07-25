# CREST API

The serverless API powering the National Fish and Wildlife Foundation's [Coastal Resilience Evaluation and Siting Tool (CREST)](https://resilientcoasts.org).

## Setting up the environment

This repository uses the Serverless Framework to build, run, and test a serverless HTTP API that runs on AWS Lambda on the Python 3.8 runtime. In order to test locally you will need to install Python 3.8.


### Installing Python 3.8 using pyenv (Optional)

We recommend using pyenv to manage Python installations.

- Install [pyenv](https://github.com/pyenv/pyenv#installation).

- Follow any instructions at the end of the install logs.

- Restart your terminal.

- Run `pyenv install 3.8.2` in your terminal to install Python 3.8.2. Now when you run `pyenv versions` you should see `3.8.2` in your list of Python installations. Try `pyenv install -l` to see a full list of versions you can install. Check out the full pyenv README for more information.


### Set up a virtual environment (Recommended)

A virtual environment is a Python abstraction that allows you to create an isolated Python environment.

There are several ways to set up virtual environments. Here are a few options:

- [Pipenv](https://pipenv.pypa.io/en/latest/) is a well-supported environment manager. It plays nicely with pyenv as well. Once Pipenv is installed run `pipenv install -r requirements.txt` to set up your virtual environment and install dependencies.

- If you're using pyenv on Linux or macOS, you can use the [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv#pyenv-virtualenv) pyenv plugin.

- Python 3's built-in module [venv](https://docs.python.org/3/library/venv.html).

- There's always the classic [virtualenv](https://virtualenv.pypa.io/en/latest/) library. If you go this route you might want to check out the popular tool [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/stable/).


### Install dependencies

- Install [nodejs](https://nodejs.org/en/) if you don't have it already. Make sure to choose the LTS version.

- Install the [Serverless Framework](https://serverless.com/framework/docs/getting-started/) using npm: `npm install -g serverless`.

- Unless you're using Pipenv, you'll need to activate your virtual environment (see the documentation for your virtual environment manager). Once you've activated your environment, run `pip install -r requirements.txt`. If you're using pipenv the install command you used above does this for you.

- Install serverless dependencies: `npm install`


## Run a local API

You can use Serverless Offline to spin up a local API that you can use while you're developing:

```bash
serverless offline
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

# CNMI
curl http://localhost:3000/dev/identify/\?lng\=-145.72\&lat\=15.2\&region=cnmi




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

```bash
serverless deploy --stage prod
```

## To Do

- Test VRT integrity by cross-referencing VRT-based results with results from individual datasets using `gdallocationinfo`

