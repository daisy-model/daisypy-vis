'''Test dlf module'''
from daisy_vis.io import dlf

def test_read_dlf_only_header_present(only_header_path):
    '''Test that we can correctly read a file without a body'''
    soil_tracer = dlf.read_dlf(only_header_path)
    assert len(soil_tracer.header) > 0
    assert len(soil_tracer.units) == 0
    assert len(soil_tracer.body) == 0


def test_read_dlf_empty_file(empty_file_path):
    '''Test that we dont blow up when reading an empty file'''
    soil_tracer = dlf.read_dlf(empty_file_path)
    assert len(soil_tracer.header) == 0
    assert len(soil_tracer.units) == 0
    assert len(soil_tracer.body) == 0

    
