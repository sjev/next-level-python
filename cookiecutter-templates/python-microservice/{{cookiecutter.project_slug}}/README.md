# {{ cookiecutter.project_name }}



{{ cookiecutter.project_short_description}}


This repository can be used both as a python package and as a microservice.


1. *python package*  - a normal package hosted in the package repository.
2. *microservice* - package is installed inside a docker container.

## Quick start

Build and run locally

`build_and_run.sh`

See script for more details.


## Development


1. develop and test in devcontainer (VSCode)
2. trigger ci builds by bumping version with a tag. (see `.gitlab-ci.yml`)

## Tooling

* Verisoning : `bump2version`
* Linting and formatting : `ruff`
* Typechecking: `mypy`

## What goes where
* `src/{{ cookiecutter.package_name }}` app code. `pip install .` .
* `docker` folder contains dockerfiles for app images.
* `.gitlab-ci.yml` takes care of the building steps.


