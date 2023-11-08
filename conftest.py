import pytest

@pytest.fixture
def dlf_path():
    return 'test-data/DailyP-Daily-WaterFlux.dlf'

@pytest.fixture
def only_header_path():
    return 'test-data/DailyP-Soil-Tracer.dlf'

@pytest.fixture
def empty_file_path():
    return 'test-data/empty-file.dlf'
