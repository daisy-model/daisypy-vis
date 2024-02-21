'''Test plot_annual'''
import pytest
from daisypy.vis.plot import plot_annual

@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'})
def test_plot_annual(n_annual_dlfs):
    '''Test plotting multiple dlfs with four logged variables'''
    fig, _ = plot_annual(n_annual_dlfs, ['m1', 'm2', 'm3', 'm4'])
    return fig
