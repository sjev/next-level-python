#!/bin/bash
set -e
set -x

source config.sh
# get release of mkdocs
mkdir -p files
wget https://github.com/squidfunk/mkdocs-material/archive/refs/tags/$MATERIAL_VERSION.tar.gz -O files/mkdocs-material.tar.gz

# Build the mkdocs image
docker build -t $IMG_NAME --build-arg VERSION=$MATERIAL_VERSION .

