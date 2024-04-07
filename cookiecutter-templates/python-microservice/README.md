# Python microservice template

**Note:** this repo is currently only contains CI scripts for [gitlab](gitlab.com)

A [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) (project template) for rapidly developing Python microservices.
Lean and mean.

## Features

#### Automatic updates to the projects generated from this cookiecutter

* Powered by [cruft](https://cruft.github.io/cruft/)
* Keep your project up-to-date with best practices

#### Continuous integration

* Powered by Gitlab CI


## Usage

Make sure you have [`cruft`](https://github.com/cruft/cruft#installation) installed. Alternatively, you can use
 [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/installation.html) if you are not interested in
  getting updates to the project "boilerplate" in the future.

Create a new project:

```sh
cruft create https://gitlab.com/roxautomation/templates/python-microservice
```

The CLI interface will ask some basic questions, such the name of the project, and then generate all the goodies
 automatically.

After that you can make it a proper git repo:

```sh
cd <your-project-slug>
git init
git add .
git commit -m "Initial commit"
```

We update this cookiecutter template regularly to keep it up-to-date. You
 can get the updates into your project with:

```sh
cruft update
```
