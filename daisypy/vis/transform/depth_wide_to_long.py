# pylint: disable=missing-module-docstring
import pandas as pd
from daisypy.vis.io.dlf import Dlf

__all__ = [
    'depth_wide_to_long'
]

def depth_wide_to_long(dlf, var_name, time_name='time', depth_name='z'):
    '''Transform wide format time series to a long format time series

    It is assumed that dlf.body only contains `time_name` columns and depth columns with the
    format
      'var_name @ depth-below-surface'
    
    Parameters
    ----------
    dlf : daisy_vis.io.dlf.Dlf

    time_name : str OR sequence of str
      Name(s) of time column(s)

    depth_name : str
      Name to use for depth column

    Returns
    -------
    transformed_dlf : daisy_vis.io.dlf.Dlf
    '''
    body = pd.wide_to_long(
        dlf.body, [var_name], i=time_name, j=depth_name, sep=' @ ', suffix=r'-?\d+(\.\d*)?'
    ).reset_index(depth_name).reset_index(time_name) # By splitting depth_name and time_name in two
                                                     # calls we allow time_name to be either string
                                                     # or sequence of string.
    units = {
        depth_name : 'unknown-depth-unit'
    }
    if isinstance(time_name, str):        
        units[time_name] = dlf.units[time_name] if time_name in dlf.units else ''
    else:
        for k in time_name:
            units[k] = dlf.units[k] if k in dlf.units else ''
    for k, v in dlf.units.items():
        if k.startswith(var_name):
            units[var_name] = v
            break
    
    return Dlf(dlf.header, units, body)
