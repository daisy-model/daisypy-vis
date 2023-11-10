[![pytest](https://github.com/daisy-model/daisy-vis/actions/workflows/pytest.yml/badge.svg)](https://github.com/daisy-model/daisy-vis/actions/workflows/pytest.yml)
[![Pylint](https://github.com/daisy-model/daisy-vis/actions/workflows/pylint.yml/badge.svg)](https://github.com/daisy-model/daisy-vis/actions/workflows/pylint.yml)

# daisy-vis
Visualisation library and tools for Daisy model output

See [doc](doc) for examples.

## Installation
On linux

	git clone git@github.com:daisy-model/daisy-vis.git
	cd daisy-vis
	pip install .

## Testing
To install test dependencies

    pip install -e .[test]

To run tests

    pytest

## Development
Install package as editable

    pip install -e .

### pylint
Use `pyproject.toml` for package-wide settings, e.g. `ignore-trailing-whitespace`.

	pylint daisy_vis


### Tests
Use pytest-mpl to compare images. Generate baselines images by running

    pytest --mpl-generate-path=test-data/baseline

and inspect the output...
