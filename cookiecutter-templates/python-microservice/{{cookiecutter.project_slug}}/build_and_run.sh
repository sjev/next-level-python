#!/bin/bash

# steps:

# 1. build package in container using dev image
# 2. build app image using package

set -e

source ./config.sh


# 1. build package in container
echo "Building package in container..."
rm -rf ./dist ./docker/dist
docker run --rm -v $(pwd):/workspace -w /workspace $DEV_IMG make build
cp -r ./dist ./docker/dist


# 2. build docker image
echo "Building app image..."
docker build -t $APP_IMG -f ./docker/Dockerfile  ./docker

# # run docker image
echo "Running app image..."
docker run --rm -it -p 8000:8000 $APP_IMG
