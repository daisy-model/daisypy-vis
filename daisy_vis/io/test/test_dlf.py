'''Test dlf module'''
from daisy_vis.io import dlf

def test_read_dlf(dlf_path):
    '''Test that we can correctly read a dlf file'''
    dlf_file = dlf.read_dlf(dlf_path)
    assert len(dlf_file.header) > 0
    assert len(dlf_file.units) > 0
    assert len(dlf_file.units) == len(dlf_file.body.columns)


def test_read_dlf_only_header_present(only_header_path):
    '''Test that we can correctly read a file without a body'''
    only_header = dlf.read_dlf(only_header_path)
    assert len(only_header.header) > 0
    assert len(only_header.units) == 0
    assert len(only_header.body) == 0


def test_read_dlf_empty_file(empty_file_path):
    '''Test that we dont blow up when reading an empty file'''
    empty_file = dlf.read_dlf(empty_file_path)
    assert len(empty_file.header) == 0
    assert len(empty_file.units) == 0
    assert len(empty_file.body) == 0

    
