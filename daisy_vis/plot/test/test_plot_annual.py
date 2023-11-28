'''Test plot_annual'''
import pytest
from daisy_vis.plot import plot_annual

@pytest.mark.mpl_image_compare
def test_plot_annual(n_annual_dlfs):
    fig, ax = plot_annual(n_annual_dlfs, ['m1', 'm2', 'm3', 'm4'])
    return fig
