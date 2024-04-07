#!/bin/bash

set -e


source ./config.sh

docker build --build-arg CACHEBUST=$(date +%s) \
            --build-arg UID=$(id -u) \
            --build-arg GID=$(id -g) \
            --build-arg IMG_NAME={{ cookiecutter.project_slug }}-local \
            -t $DEV_IMG \
            -f .devcontainer/Dockerfile .

case "$1" in
  shell)
    echo "Starting $DEV_IMG in shell mode..."
    docker run -it --rm -v $(pwd):/workspace -w /workspace $DEV_IMG /bin/bash
    ;;
  push)
    echo "Pushing $DEV_IMG ..."
    docker push $DEV_IMG
    ;;
  *)
    echo "Usage: $0 {shell|push}"
    exit 1
    ;;
esac
