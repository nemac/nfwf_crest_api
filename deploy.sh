#! /usr/bin/env bash

source '.env'

BUCKET_NAME='nemac-cloudformation'

TEMPLATE_NAME='template.yaml'

DATA_BUCKET='nfwf-tool'

case $1 in "dev")
  STACK_NAME='nfwf-tool-api-dev'
  STAGE_NAME='Dev'
  PACKAGED_TEMPLATE='packaged-dev.yaml'
  VRT_FILE=$VRT_FILE_DEV
  ;;
"prod")
  STACK_NAME='nfwf-tool-api'
  STAGE_NAME='Prod'
  PACKAGED_TEMPLATE='packaged-prod.yaml'
  VRT_FILE=$VRT_FILE_PROD
  ;;
*)
  echo "You must provide a stage to deploy to as an argument to this script (either 'dev' or 'prod')"
  exit 1
  ;;
esac

echo "Updating cloudformation resources..."
echo "Stage name: $STAGE_NAME"
echo "Cloudformation stack: $STACK_NAME"

aws cloudformation package \
  --template-file $TEMPLATE_NAME \
  --output-template-file $PACKAGED_TEMPLATE \
  --s3-bucket $BUCKET_NAME

aws cloudformation deploy \
  --template-file $PACKAGED_TEMPLATE \
  --stack-name $STACK_NAME \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides Stage=$STAGE_NAME

# Upload the VRT to S3
aws s3 cp $VRT_FILE s3://$DATA_BUCKET/$VRT_FILE
