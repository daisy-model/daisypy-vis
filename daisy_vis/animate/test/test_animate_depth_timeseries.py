'''Test animate_depth_timeseries'''
import os
import pytest
from daisy_vis.animate import animate_depth_timeseries
from daisy_vis.test_helpers import compare_image_files, save_animation

def render_and_compare_animation(fig, out_dir, ref_dir, error_dir, rms_tolerance=2):
    '''Save animated timeseries as a series of png files and compare with an existing reference'''
    actual_files = save_animation(fig, out_dir)
    ref_files = { entry.name for entry in os.scandir(ref_dir) if entry.is_file() }
    assert actual_files <= ref_files <= actual_files
    match, mismatch, error = compare_image_files(out_dir,
                                                 ref_dir,
                                                 ref_files,
                                                 error_dir,
                                                 rms_tolerance=rms_tolerance)
    assert len(error) == 0
    assert len(mismatch) == 0
    assert len(match) == len(ref_files)

@pytest.mark.filterwarnings(r'ignore:setDaemon\(\) is deprecated, set the daemon attribute instead')
def test_png_rendering_is_the_same(depth_timeseries, base_out_dir, baseline_dir, base_error_dir):
    '''Save animated timeseries as a series of png files and compare with an existing reference'''
    out_dir = os.path.join(base_out_dir,
                           'animate_depth_timeseries',
                           'png_rendering_is_the_same')
    ref_dir = os.path.join(baseline_dir,
                           'animate_depth_timeseries',
                           'png_rendering_is_the_same_ref')
    error_dir = os.path.join(base_error_dir,
                             'animate_depth_timeseries',
                             'png_rendering_is_the_same')
    fig = animate_depth_timeseries('q', depth_timeseries)
    render_and_compare_animation(fig, out_dir, ref_dir, error_dir, rms_tolerance=2.18)

@pytest.mark.filterwarnings(r'ignore:setDaemon\(\) is deprecated, set the daemon attribute instead')
def test_png_rendering_is_the_same_with_params(depth_timeseries,
                                               base_out_dir,
                                               baseline_dir,
                                               base_error_dir):
    '''Save animated timeseries as a series of png files and compare with an existing reference'''
    out_dir = os.path.join(base_out_dir,
                           'animate_depth_timeseries',
                           'png_rendering_is_the_same_with_params')
    ref_dir = os.path.join(baseline_dir,
                           'animate_depth_timeseries',
                           'png_rendering_is_the_same_with_params_ref')
    error_dir = os.path.join(base_error_dir,
                             'animate_depth_timeseries',
                             'png_rendering_is_the_same_with_params')
    fig = animate_depth_timeseries('q',
                                   depth_timeseries,
                                   figsize=(200,200),
                                   var_lim=(-1,-1),
                                   depth_lim=(-100,-5))
    render_and_compare_animation(fig, out_dir, ref_dir, error_dir)
