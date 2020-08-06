#! /usr/bin/env python

import argparse, os
import util

config = util.get_config()


def download_region(region, dir_path):
  bucket = config['dataset_bucket']
  datasets = config['datasets'][region]
  for d in datasets:
    dataset_path = f's3://{bucket}/{d["path"]}'
    c = f'aws s3 cp {dataset_path} {dir_path}'
    print(c)
    os.system(c)
  

def setup_argparser():
  parser = argparse.ArgumentParser()
  parser.add_argument('--dir', required=True)
  parser.add_argument('--region')
  return parser


def main():
  parser = setup_argparser()
  args = parser.parse_args()
  dir_path = args.dir
  region = args.region
  download_region(region, dir_path)


if __name__ == '__main__':
  main()
