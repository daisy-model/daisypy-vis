'''Test daisy_time_to_timestamp'''
from daisypy.vis.transform import daisy_time_to_timestamp

def test_no_rows_are_dropped_correct(timeseries_multiple_time_vars):
    # pylint: disable=missing-function-docstring
    dlf = daisy_time_to_timestamp(timeseries_multiple_time_vars, 'time')
    assert len(dlf.body) == len(timeseries_multiple_time_vars.body)

def test_units_are_correct(timeseries_multiple_time_vars):
    '''Test that units are updated correctly'''
    dlf = daisy_time_to_timestamp(timeseries_multiple_time_vars, 'time')
    assert dlf.units['time'] == ''
    
    time_vars = {'year', 'month', 'mday', 'hour'}
    for k in time_vars:
        assert k in timeseries_multiple_time_vars.units
        assert k not in dlf.units
        
    for k,v in timeseries_multiple_time_vars.units.items():
        if k not in time_vars:
            assert dlf.units[k] == v

def test_times_are_correct(timeseries_multiple_time_vars):
    '''Test that timestamps are one day apart'''
    dlf = daisy_time_to_timestamp(timeseries_multiple_time_vars, 'time')
    times = sorted(dlf.body['time'])
    expected_time_diff = 60*60*24 # The values are logged daily
    expected_total_time_diff = expected_time_diff*(len(dlf.body)-1)
    assert (times[-1] - times[0]).total_seconds() == expected_total_time_diff
    for i, time in enumerate(times[1:]):
        assert (time - times[i]).total_seconds() == expected_time_diff
