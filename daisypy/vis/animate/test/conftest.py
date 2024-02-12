'''Test data for tests in the amimate module'''
import pytest
from daisy_vis.io.dlf import read_dlf

@pytest.fixture
def depth_timeseries():
    '''A depth time series'''
    return  read_dlf('test-data/daily/DailyP/DailyP-Daily-WaterFlux.dlf')
