'''Test animate_depth_timeseries'''
import os
import filecmp
import shutil
import pytest
import plotly
from daisy_vis.animate import animate_depth_timeseries

@pytest.mark.filterwarnings(r'ignore:setDaemon\(\) is deprecated, set the daemon attribute instead')
def test_png_rendering_is_the_same(depth_timeseries,
                                   depth_timeseries_outdir,
                                   depth_timeseries_expected_dir,
                                   base_error_dir):
    '''Save animated timeseries as a series of png files and compare with an existing reference'''
    os.makedirs(depth_timeseries_outdir, exist_ok=True)
    fig = animate_depth_timeseries('q', depth_timeseries)
    actual_files = set()
    for frame in range(len(fig.frames)):
        fig.layout['sliders'][0]['active'] = frame
        fig = plotly.graph_objects.Figure(data=fig['frames'][frame]['data'],
                                          frames=fig['frames'],
                                          layout=fig.layout)
        fname = f'frame-{frame:02d}.png'
        fig.write_image(os.path.join(depth_timeseries_outdir, fname))
        actual_files.add(fname)

    expected_files = {
        entry.name for entry in os.scandir(depth_timeseries_expected_dir) if entry.is_file()
    }
    assert actual_files <= expected_files <= actual_files
    
    match, mismatch, errors = filecmp.cmpfiles(depth_timeseries_outdir,
                                               depth_timeseries_expected_dir,
                                               expected_files,
                                               shallow=False)
    if len(mismatch) > 0 or len(errors) > 0:
        error_dir = os.path.join(base_error_dir, 'animate_depth_timeseries')
        os.makedirs(error_dir, exist_ok=True)
        for fname in mismatch + errors:
            shutil.copy(os.path.join(depth_timeseries_outdir, fname),
                        os.path.join(error_dir, f'actual_{fname}'))
            shutil.copy(os.path.join(depth_timeseries_expected_dir, fname),
                        os.path.join(error_dir, f'expected_{fname}'))
    assert len(mismatch) == 0
    assert len(errors) == 0
    assert len(match) == len(expected_files)
