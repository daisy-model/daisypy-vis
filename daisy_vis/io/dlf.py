'''Module for reading Daisy log files'''
from collections import namedtuple
import pandas as pd

__all__ = [
    'Dlf',
    'read_dlf'
]

Dlf = namedtuple('Dlf', ['header', 'units', 'body'])
Dlf.__doc__ += ': Daisy model output log'
Dlf.header.__doc__ = 'Information describing log'
Dlf.units.__doc__ = 'dict mapping value names to units'
Dlf.body.__doc__ = 'pandas.DataFrame containing the logged values'

def read_dlf(path):
    '''Read a daisy log file

    Parameters
    ----------
    path : str
      Path to daisy log file

    Returns
    -------
    Dlf object
    '''
    # TODO: Parse header and return a dict
    header_body_sep = '--------------------'
    with open(path, encoding='utf-8') as infile:
        header = []
        for row in infile:
            if row.startswith(header_body_sep):
                break
            row = row.strip()
            if len(row) > 0:
                header.append(row)
        try:
            csv_header = next(infile).strip('\n').split('\t')
            units = dict(zip(csv_header, next(infile).strip('\n').split('\t')))
            body = pd.read_csv(infile, sep='\t', names=csv_header)
        except StopIteration:
            units = {}
            body = pd.DataFrame()
    return Dlf(header, units, body)
        
