'''Test animate_depth_timeseries'''
import os
import pytest
from daisypy.vis.animate import animate_depth_timeseries
from daisypy.vis.test_helpers import compare_image_files, save_animation

def render_and_compare_animation(fig, out_dir, ref_dir, error_dir, rms_tolerance=2):
    '''Save animated timeseries as a series of png files and compare with an existing reference'''
    # Remove all text, otherwise we end up failing because we got another font
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    fig.layout['sliders'][0]['currentvalue']['prefix'] = ''
    for i in range(len(fig.layout['sliders'][0]['steps'])):
        fig.layout['sliders'][0]['steps'][i]['label'] = ''
    fig.layout['xaxis']['title']['text'] = ''
    fig.layout['yaxis']['title']['text'] = ''

    actual_files = save_animation(fig, out_dir)
    ref_files = { entry.name for entry in os.scandir(ref_dir) if entry.is_file() }
    assert actual_files <= ref_files
    assert ref_files <= actual_files
    match, mismatch, error = compare_image_files(out_dir,
                                                 ref_dir,
                                                 ref_files,
                                                 error_dir,
                                                 rms_tolerance=rms_tolerance)
    assert len(error) == 0
    assert len(mismatch) == 0
    assert len(match) == len(ref_files)


# From kaleido
@pytest.mark.filterwarnings(r'ignore:setDaemon\(\) is deprecated, set the daemon attribute instead')
# From pandas via plotly
@pytest.mark.filterwarnings(r'ignore:When grouping with a length-1 list-like')
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
    fig = animate_depth_timeseries(depth_timeseries, 'q')
    render_and_compare_animation(fig, out_dir, ref_dir, error_dir, rms_tolerance=2.18)

# From kaleido
@pytest.mark.filterwarnings(r'ignore:setDaemon\(\) is deprecated, set the daemon attribute instead')
# From pandas via plotly
@pytest.mark.filterwarnings(r'ignore:When grouping with a length-1 list-like')
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
    fig = animate_depth_timeseries(depth_timeseries,
                                   'q',
                                   figsize=(200,200),
                                   var_lim=(-1,-1),
                                   depth_lim=(-100,-5))
    render_and_compare_animation(fig, out_dir, ref_dir, error_dir)
