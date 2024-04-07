#!/bin/bash


export APP_IMG="registry.gitlab.com/{{ cookiecutter.gitlab_path }}/{{ cookiecutter.project_slug }}"
export DEV_IMG=$APP_IMG:dev

echo APP_IMG=$APP_IMG
echo DEV_IMG=$DEV_IMG
