'''Test points and lines plot'''
import matplotlib as mpl
import pytest
from daisypy.vis.plot import points_and_lines

       
@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'})
def test_points_and_lines_no_kwargs(annual_dlf1):
    '''Test plotting a single variables in a single dlf and mostly default keyword arguments'''
    fig, _ = points_and_lines(annual_dlf1,
                              'year',
                              ['m1'],
                              dlf_names=['Test dlf'],
                              title='Test plot')
    return fig

@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'})
def test_points_and_lines_all_kwargs(n_annual_dlfs):
    '''Test plotting four variables in four dlfs and all keyword arguments used'''
    fig, _ = points_and_lines(n_annual_dlfs,
                              'year',
                              ['m1', 'm2', 'm3', 'm4'],
                              dlf_names=['d1', 'd2', 'd3', 'd4'],
                              cmap=mpl.colormaps['Dark2'],
                              markers=['$\\Delta$', 'o', '.', 'v'],
                              linestyles=['--', ':', '-'],
                              title='Test plot')
    return fig
