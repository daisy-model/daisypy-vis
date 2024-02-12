'''Test depth_wide_to_long'''
import pytest
from daisypy.vis.transform import depth_wide_to_long

def test_single_time_var(timeseries_single_time_var):
    '''Test that we can work a single time variable'''
    dlf = depth_wide_to_long(timeseries_single_time_var, 'q', 'time')
    
    actual_columns = set(dlf.body.columns)    
    expected_columns = {'time', 'q', 'z'}
    assert actual_columns <= expected_columns <= actual_columns

    actual_units = dlf.units
    expected_units = {
        'time' : '',
        'q' : 'mm',
        'z' : 'unknown-depth-unit' # It is not defined in the dlf. 
    }
    assert len(actual_units) == len(expected_units)
    for k,v in expected_units.items():
        assert actual_units[k] == v

    expected_n_rows = len(timeseries_single_time_var.body) * \
        (len(timeseries_single_time_var.body.columns) - 1)
    actual_n_rows = len(dlf.body)
    assert expected_n_rows == actual_n_rows
    

def test_multiple_time_vars(timeseries_multiple_time_vars):
    '''Test that we can work with multiple time variables'''
    dlf = depth_wide_to_long(timeseries_multiple_time_vars, 'q', ['year', 'month', 'mday', 'hour'])
    actual_columns = set(dlf.body.columns)
    expected_columns = {'year', 'month', 'mday', 'hour', 'q', 'z'}
    assert actual_columns <= expected_columns <= actual_columns

    actual_units = dlf.units
    expected_units = {
        'year' : '',
        'month' : '',
        'mday' : '',
        'hour' : '',
        'q' : 'mm',
        'z' : 'unknown-depth-unit' # It is not defined in the dlf. 
    }
    assert len(actual_units) == len(expected_units)
    for k,v in expected_units.items():
        assert actual_units[k] == v

    expected_n_rows = len(timeseries_multiple_time_vars.body) * \
        (len(timeseries_multiple_time_vars.body.columns) - 4)
    actual_n_rows = len(dlf.body)
    assert expected_n_rows == actual_n_rows
    

def test_multiple_depth_var_throws(timeseries_single_time_var):
    '''Test that passing multiple depth values throws a TypeError'''
    with pytest.raises(TypeError):
        depth_wide_to_long(timeseries_single_time_var, ['q', 'p'])

def test_extra_variables_throws(timeseries_multiple_time_vars):
    '''Test that we get a ValueError if there are variables that are neither depth variables, nor
    used as time variables
    '''
    with pytest.raises(ValueError):
        depth_wide_to_long(timeseries_multiple_time_vars, 'q', 'year')

def test_no_depth_variables_throws(timeseries_no_depth):
    '''Test that we get a ValueError if the depth variable is not a depth variable'''
    with pytest.raises(ValueError):
        depth_wide_to_long(timeseries_no_depth, 'Crop', 'time')

    
