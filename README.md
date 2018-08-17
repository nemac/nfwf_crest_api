# NFWF Tool API

GIS microservices build on AWS services. 

(Forked from https://github.com/aws-samples/cookiecutter-aws-sam-python)

## Requirements

* AWS CLI already configured with at least PowerUser permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Pipenv installed](https://github.com/pypa/pipenv)
    - `pip install pipenv`
* [Docker installed](https://www.docker.com/community-edition)
* [SAM Local installed](https://github.com/awslabs/aws-sam-local) 

Provided that you have requirements above installed, proceed by installing the application dependencies and development dependencies:

```bash
docker run --rm -v $PWD:/var/task -it lambci/lambda:build-python3.6 /bin/bash -c './build.sh'
```

## Testing

(There aren't any tests right now.)

`Pytest` is used to discover tests created under `tests` folder - Here's how you can run tests our initial unit tests:

```bash
pipenv run python -m pytest tests/ -v
```

## Packaging

AWS Lambda Python runtime requires a flat folder with all dependencies including the application. To facilitate this process, the pre-made SAM template expects this structure to be under `<src>/<function>/build/`:

```yaml
...
    FunctionName:
        Type: AWS::Serverless::Function
        Properties:
            CodeUri: folder_function/build/
            ...
```


### Local development

Given that you followed Packaging instructions then run one of the following options to invoke your function locally:

**Invoking function locally without API Gateway**

```bash
echo '{ "body": { "type": "FeatureCollection","name": "charleston-poly","features": [{ "type": "Feature", "properties": { "id": null }, "geometry": { "type": "Polygon", "coordinates": [ [ [ -79.662208557128906, 32.920664249232836 ], [ -79.685039520263672, 32.930174118010605 ], [ -79.717311859130845, 32.906541649538447 ], [ -79.691219329833984, 32.895299602872463 ], [ -79.676971435546875, 32.902362080894527 ], [ -79.675083160400391, 32.909568110575655 ], [ -79.662208557128906, 32.920664249232836 ] ] ] } }]} }' | sam local invoke ZonalStatsFunction

# MultiPolygon

echo '{ "body": { "type": "FeatureCollection", "name": "charleston-multi-poly", "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } }, "features": [{ "type": "Feature", "properties": { "id": null }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [-79.744316416802718, 32.918307771183919], [-79.758743269652271, 32.880394658156938], [-79.827024159455647, 32.910824100458811], [-79.793686860877372, 32.942719190317831], [-79.744316416802718, 32.918307771183919] ] ], [ [ [-79.662208557128906, 32.920664249232836], [-79.685039520263672, 32.930174118010605], [-79.717311859130845, 32.906541649538447], [-79.691219329833984, 32.895299602872463], [-79.676971435546875, 32.902362080894527], [-79.675083160400391, 32.909568110575655], [-79.662208557128906, 32.920664249232836] ] ] ] } }] }}' | sam local invoke ZonalStatsFunction

echo '{ "body": { "type": "FeatureCollection", "name": "char9", "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } }, "features": [ { "type": "Feature", "properties": { "FID": 0, "it": 1, "_mean": 9.0 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -79.935407638549805, 32.773635858629468 ], [ -79.931888580322266, 32.77406886435805 ], [ -79.93201732635498, 32.772156406494297 ], [ -79.935021400451646, 32.772228575461689 ], [ -79.935407638549805, 32.773635858629468 ] ] ] ] } } ] } }' | sam local invoke ZonalStatsFunction

# Florida Keys Multipolygon (TIMING OUT)
echo '{ "body": {  "type": "FeatureCollection",  "name": "keys_multi",  "crs": {  "type": "name",  "properties": {  "name": "urn:ogc:def:crs:OGC:1.3:CRS84"  }  },  "features": [{  "type": "Feature",  "properties": {  "EZG_ID": 62145,  "prg_name": "Mote Marine Laboratory, Inc.",  "proj_name": "Florida Keys Coral Disease Response & Restoration Initiative",  "region": "Gulf",  "name": "Florida Keys Coral Disease Response & Restoration Initiative",  "id": 62145,  "area": 391374264.7,  "nfwf_proje": null,  "nfwf_pro_1": null,  "asset": null,  "threat": null,  "exposure": null,  "aquatic": null,  "terrestria": null,  "hubs": null,  "crit_infra": null,  "crit_facil": null,  "pop_densit": null,  "social_vul": null,  "drainage": null,  "erosion": null,  "floodprone": null,  "geostress": null,  "sea_level_": null,  "slope": null,  "storm_surg": null  },  "geometry": {  "type": "MultiPolygon",  "coordinates": [  [  [  [-81.302133056890256, 24.60695607607207],  [-81.808877441885357, 24.499532477742999],  [-81.815743897117486, 24.54326248601156],  [-81.306252930209197, 24.650648613252887],  [-81.302133056890256, 24.60695607607207]  ]  ],  [  [  [-80.10747716193147, 25.690925958783847],  [-80.167901966716897, 25.391066939726667],  [-80.209100697211582, 25.410915452360324],  [-80.155542347658283, 25.658745696291859],  [-80.10747716193147, 25.690925958783847]  ]  ]  ]  }  }] }}' | sam local invoke ZonalStatsFunction
```

**Invoking function locally through local API Gateway**

```bash
sam local start-api
```

If the previous command run successfully you should now be able to hit the following local endpoint to invoke your function. For example, to test the identify function go to the following URL: `http://localhost:3000/identify?lat=80&lng=-30`.

## Deployment


First and foremost, we need a S3 bucket where we can upload our Lambda functions packaged as ZIP before we deploy anything - If you don't have a S3 bucket to store code artifacts then this is a good time to create one:

```bash
aws s3 mb s3://BUCKET_NAME
```

Provided you have a S3 bucket created, run the following command to package our Lambda function to S3:

```bash
aws cloudformation package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket nemac-cloudformation
```

Next, the following command will create a Cloudformation Stack and deploy your SAM resources.

```bash
# Dev
aws cloudformation deploy \
    --template-file packaged.yaml \
    --stack-name nfwf-tool-api-dev \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides Stage=Dev

# Prod
aws cloudformation deploy \
    --template-file packaged.yaml \
    --stack-name nfwf-tool-api \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides Stage=Prod

```

> **See [Serverless Application Model (SAM) HOWTO Guide](https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md) for more details in how to get started.**


After deployment is complete you can run the following command to retrieve the API Gateway Endpoint URL:

```bash
aws cloudformation describe-stacks \
    --stack-name nfwf-tool-api \
    --query 'Stacks[].Outputs'
``` 



# Appendix

## Makefile

(The supplied Makefile should only be considered as reference material as the build processes have slightly changed.)

It is important that the Makefile created only works on OSX/Linux but the tasks above can easily be turned into a Powershell or any scripting language you may want too.

The following make targets will automate that we went through above:

* Find all available targets: `make`
* Install all deps and clone (OS hard link) our lambda function to `/build`: `make build SERVICE="first_function"`
    - `SERVICE="first_function"` tells Make to start the building process from there
    - By creating a hard link we no longer need to keep copying our app over to Build and keeps it tidy and clean
* Run `Pytest` against all tests found under `tests` folder: `make test`
* Install all deps and builds a ZIP file ready to be deployed: `make package SERVICE="first_function"`
    - You can also build deps and a ZIP file within a Docker Lambda container: `make package SERVICE="first_function" DOCKER=1`
    - This is particularly useful when using C-extensions that if built on your OS may not work when deployed to Lambda (different OS)



## AWS CLI commands

AWS CLI commands to package, deploy and describe outputs defined within the cloudformation stack:

```bash
aws cloudformation package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket nemac-cloudformation

# Dev
aws cloudformation deploy \
    --template-file packaged.yaml \
    --stack-name nfwf-tool-api-dev \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides Stage=Dev

# Prod
aws cloudformation deploy \
    --template-file packaged.yaml \
    --stack-name nfwf-tool-api-dev \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides Stage=Dev

aws cloudformation describe-stacks \
    --stack-name nfwf-tool-api --query 'Stacks[].Outputs'
```
