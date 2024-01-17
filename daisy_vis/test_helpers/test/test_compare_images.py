'''Test compare_images'''
#pylint: disable=missing-function-docstring
import os
from daisy_vis.test_helpers import compare_image_files

def test_non_existing_dirs(base_error_dir):
    match, mismatch, error = compare_image_files(
        'dir1',
        'dir2',
        ['f1'],
        os.path.join(base_error_dir, 'compare_images', 'non_existing_dirs')
    )
    assert len(match) == 0
    assert len(mismatch) == 0
    assert error == ['f1']


def test_mismatch(base_error_dir):
    match, mismatch, error = compare_image_files(
        'test-data/animate/png_rendering_is_the_same_ref',
        'test-data/animate/png_rendering_is_the_same_with_params_ref',
        ['frame-00.png'],
        os.path.join(base_error_dir, 'compare_images', 'mismatch')
    )
    assert len(match) == 0
    assert len(error) == 0
    assert mismatch == ['frame-00.png']
    

def test_missing_file(base_error_dir):
    match, mismatch, error = compare_image_files(
        'test-data/animate/png_rendering_is_the_same_ref',
        'test-data/animate',
        ['frame-00.png'],
        os.path.join(base_error_dir, 'compare_images', 'missing_file')
    )
    assert len(match) == 0
    assert len(mismatch) == 0
    assert error == ['frame-00.png']
    
