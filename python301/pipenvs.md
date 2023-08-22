# PipEnv

A pip environment for managing pip packages as well as your python version. To
manage python versions it requires pyenv.

## Installation

First you need to install pipenv itself.

```bash
pip install pipenv
```
Install (pyenv)[https://github.com/pyenv/pyenv#installation] if you want to manage python versions.

Then you will need to generate an environment inside your project directory.

```bash
pipenv install
```

## Usage

To use your pipenv:

```bash
pipenv shell
```

To remove your pipenv environment:

```bash
pipenv --rm
```

To install a package like django 2 inside your pipenv from outside of the shell:
```bash
pipenv install django==2.*
```

While inside the shell you can simply use:
```bash
pip install django==2.*
```
