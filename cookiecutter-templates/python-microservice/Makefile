.PHONY: list clean ci test

SHELL := /bin/bash



list:
	@cat Makefile

clean:
	rm -rf temp venv

ci:
	# run gitlab ci locally
	gitlab-runner exec docker test

venv:
	python -m venv venv
	source venv/bin/activate && pip install cookiecutter pyyaml pytest

test: venv
	@echo "creating example project in temp folder"
	mkdir -p temp
	rm -rf temp/*
	source venv/bin/activate && python tests/test_project_generation.py temp
