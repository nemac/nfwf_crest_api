#! /usr/bin/env sh

set -e

TEMPLATE_NAME='template.yaml'
PACKAGED_TEMPLATE='packaged.yaml'
BUCKET_NAME='nemac-cloudformation'

case $1 in "dev")
  STACK_NAME='nfwf-tool-api-dev'
  STAGE_NAME='Dev'
  ;;
"prod")
  STACK_NAME='nfwf-tool-api'
  STAGE_NAME='Prod'
  ;;
*)
  echo "You must provide a stage to deploy to as an argument to this script (either 'dev' or 'prod')"
  exit 1
  ;;
esac

echo "Updating cloudformation resources..."
echo "Stage name: $STAGE_NAME"
echo "Cloudformation stack: $STACK_NAME"

docker run --rm -it -v $PWD:/var/task lambci/lambda:build-python3.6 /bin/bash -c './build-deps.sh; ./cp-config.sh'

aws cloudformation package \
  --template-file $TEMPLATE_NAME \
  --output-template-file $PACKAGED_TEMPLATE \
  --s3-bucket $BUCKET_NAME

aws cloudformation deploy \
  --template-file $PACKAGED_TEMPLATE \
  --stack-name $STACK_NAME \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides Stage=$STAGE_NAME
