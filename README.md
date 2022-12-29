# practical-python

A practical python project template using tox, pytest and pip-tools.

This is not production ready, but it's a good starting point. Requirements
should be specified in pyproject.toml and then pinned using pip-tools in
requirements.txt. The requirements.txt file is used by tox.

## Usage

1. Install tox
1. Clone this repository
1. Create and activate a virtual environment
1. Install the requirements (optionally update the pins with pip-tools:
   `pip-compile --all-extras --resolver=backtracking pyproject.toml`)
1. Install the package in editable mode: `pip install -e .`
1. Install the pre-commit hooks: `pre-commit install`
1. Run the test suite with tox: `tox`
1. Replace the name practical_python/practical-python with your project name
1. Update project metadata in pyproject.toml and README.md
1. Write some code and lint it: `tox -e fix`.

## Note

Once this stabilizes, I'll create a cookiecuttter template to make it easier.
