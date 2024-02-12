'''Test data for tests in the transform module'''
import pytest
from daisypy.vis.io.dlf import read_dlf
from daisypy.vis.transform import daisy_time_to_timestamp

@pytest.fixture
def timeseries_single_time_var():
    '''A depth time series with a single time variable'''
    return daisy_time_to_timestamp(
        read_dlf('test-data/daily/DailyP/DailyP-Daily-WaterFlux.dlf'),
        'time')

@pytest.fixture
def timeseries_multiple_time_vars():
    '''A depth time series with multiple time variables'''
    return read_dlf('test-data/daily/DailyP/DailyP-Daily-WaterFlux.dlf')

@pytest.fixture
def timeseries_no_depth():
    '''A time series without depth variables and a single time variable'''
    return daisy_time_to_timestamp(
        read_dlf('test-data/annual/Annual-FN/HourlyP-Annual-FN-2.2b.dlf'),
        'time')

