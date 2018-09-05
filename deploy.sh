#! /usr/bin/env sh


set -e

BUCKET_NAME='nemac-cloudformation'

TEMPLATE_NAME='template.yaml'

case $1 in "dev")
  STACK_NAME='nfwf-tool-api-dev'
  STAGE_NAME='Dev'
  PACKAGED_TEMPLATE='packaged-dev.yaml'
  ;;
"prod")
  STACK_NAME='nfwf-tool-api'
  STAGE_NAME='Prod'
  PACKAGED_TEMPLATE='packaged-prod.yaml'
  ;;
*)
  echo "You must provide a stage to deploy to as an argument to this script (either 'dev' or 'prod')"
  exit 1
  ;;
esac

./build.sh

echo "Updating cloudformation resources..."
echo "Stage name: $STAGE_NAME"
echo "Cloudformation stack: $STACK_NAME"

#docker run --rm -it -v $PWD:/var/task lambci/lambda:build-python3.6 /bin/bash -c './build-deps.sh; ./cp-config.sh'

aws cloudformation package \
  --template-file $TEMPLATE_NAME \
  --output-template-file $PACKAGED_TEMPLATE \
  --s3-bucket $BUCKET_NAME

aws cloudformation deploy \
  --template-file $PACKAGED_TEMPLATE \
  --stack-name $STACK_NAME \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides Stage=$STAGE_NAME
