# Mkdocs container

Used for building and serving docs

## Usage

mount folder containing `mkdocs.yml` to `/docs` inside container and run.

example:

    docker run --rm -it -p 8010:8000 -v ${PWD}/test_docs:/docs local/mkdocs
