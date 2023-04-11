# bulletproof-python

A magic-free, understandable python project template using tox, ruff, pytest and
pip-tools. This template requires you to manage your own virtual environment,
but the configuration is explicit and easy to understand.

This is not production ready, but it's a good starting point. Requirements
should be specified in pyproject.toml and then pinned using pip-tools in
`requirements.txt`. The `requirements.txt` file is used by tox.

## Usage

1. Install tox
1. Clone this repository
1. Create and activate a virtual environment
1. Install the requirements (optionally update the pins with pip-tools:
   `pip-compile --all-extras --resolver=backtracking --upgrade pyproject.toml`)
1. Install the package in editable mode: `pip install -e .`
1. Install the pre-commit hooks: `pre-commit install`
1. Run the test suite with tox: `tox`
1. Replace the name bulletproof_python/bulletproof-python with your project name
1. Update project metadata in pyproject.toml and README.md
1. Write some code and lint it: `tox -e fix`.

## Note

Once this stabilizes, I'll create a cookiecuttter template to make it easier.
