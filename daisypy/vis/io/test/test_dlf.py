'''Test dlf module'''
from daisypy.vis.io.dlf import read_dlf

def test_read_dlf(dlf_path):
    '''Test that we can correctly read a dlf file'''
    dlf_file = read_dlf(dlf_path)
    assert len(dlf_file.header) > 0
    assert len(dlf_file.units) > 0
    assert len(dlf_file.units) == len(dlf_file.body.columns)


def test_read_dlf_only_header_present(only_header_path):
    '''Test that we can correctly read a file without a body'''
    only_header = read_dlf(only_header_path)
    assert len(only_header.header) == 8
    assert isinstance(only_header.header['LOG'], list)
    assert len(only_header.header['LOG']) == 3
    assert len(only_header.units) == 0
    assert len(only_header.body) == 0


def test_read_dlf_empty_file(empty_file_path):
    '''Test that we dont blow up when reading an empty file'''
    empty_file = read_dlf(empty_file_path)
    assert len(empty_file.header) == 0
    assert len(empty_file.units) == 0
    assert len(empty_file.body) == 0

    
def test_read_dlf_units(dlf_path):
    '''Test that we read units correctly'''
    dlf = read_dlf(dlf_path)
    time_cols = ['year', 'month', 'mday', 'hour']
    for k in time_cols:
        # Time columns does not have an explicit unit
        assert dlf.units[k] == ''

    for k in dlf.body.columns:
        if k not in time_cols:
            # There are only 'q @ depth' columns besided time columns, and they are all in mm
            assert dlf.units[k] == 'mm'
