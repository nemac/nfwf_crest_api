#! /usr/bin/env bash

set -ev

case $1 in "dev")
  STACK_NAME='nfwf-tool-api-dev'
  ;;
"prod")
  STACK_NAME='nfwf-tool-api'
  ;;
*)
  echo "You must provide a stage to deploy to as an argument to this script (either 'dev' or 'prod')"
  exit 1
  ;;
esac

