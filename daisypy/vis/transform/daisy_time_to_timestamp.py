# pylint: disable=missing-module-docstring
import pandas as pd
from daisypy.vis.io.dlf import Dlf

__all__ = [
    'daisy_time_to_timestamp'
]

def daisy_time_to_timestamp(dlf, time_col_name='time'):
    '''Transform daisy time to a single timestamp
    columns 'year', 'month', 'mday', 'hour' are dropped and replaced with a timestamp
    
    Parameters
    ----------
    dlf : daisy_vis.io.dlf.Dlf

    time_col_name : str
      Name of new timestamp column

    Returns
    -------
    transformed_dlf : daisy_vis.io.dlf.Dlf
    '''
    def make_timestamp(series):
        return pd.Timestamp(year=int(series['year']),
                            month=int(series['month']),
                            day=int(series['mday']),
                            hour=int(series['hour']))
    
    body = dlf.body.copy()
    body[time_col_name] = body.apply(make_timestamp, axis=1)
    time_cols = ['year', 'month', 'mday', 'hour']
    body = body.drop(columns=time_cols).sort_values(by=time_col_name)
    units = { k:v for k,v in dlf.units.items() if k not in time_cols }
    units['time'] = ''
    return Dlf(dlf.header, units, body)
