[![pytest](https://github.com/daisy-model/daisy-vis/actions/workflows/pytest.yml/badge.svg)](https://github.com/daisy-model/daisy-vis/actions/workflows/pytest.yml)
[![Pylint](https://github.com/daisy-model/daisy-vis/actions/workflows/pylint.yml/badge.svg)](https://github.com/daisy-model/daisy-vis/actions/workflows/pylint.yml)
[![codecov](https://codecov.io/gh/daisy-model/daisy-vis/graph/badge.svg?token=F8625GT0A8)](https://codecov.io/gh/daisy-model/daisy-vis)

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

Note that image comparison tests can fail between different version of matplotlib and freetype. You can force test against images generated with a specific version of matplotlib with

    pytest --mpl-baseline-path=test-data/baseline/matplotlib-<matplotlib-version-number>
    
If no baseline images are available for a specific version, you can generate with

    pytest --mpl-generate-path=test-data/baseline/matplotlib-<matplotlib-version-number>
    
and compare manually.

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
