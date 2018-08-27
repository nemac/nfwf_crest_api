#! /usr/bin/env sh

set -ev

STACK_NAME='nfwf-tool-api-dev'

TEMPLATE_NAME='template.yaml'
PACKAGED_TEMPLATE='packaged.yaml'
BUCKET_NAME='nemac-cloudformation'
STAGE_NAME='Dev'

aws cloudformation package \
  --template-file $TEMPLATE_NAME \
  --output-template-file $PACKAGED_TEMPLATE \
  --s3-bucket $BUCKET_NAME

aws cloudformation deploy \
  --template-file $PACKAGED_TEMPLATE \
  --stack-name $STACK_NAME \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides Stage=$STAGE_NAME
