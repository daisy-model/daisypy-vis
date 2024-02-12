'''Test bar plot'''
# It seems pointless with docstrings on these functions, so we just disable the warnings
# pylint: disable=missing-function-docstring
import pytest
import matplotlib.pyplot as plt
from daisypy.vis.plot import bar

def test_bar_no_dlf():
    with pytest.raises(ValueError):
        bar([], 'year', 'm1')
    plt.close('all')

def test_bar_dlf_dict_names_given(annual_dlf1):
    with pytest.warns(UserWarning):
        bar({'d1' : annual_dlf1}, 'year', 'm1', dlf_names=['d2'])
    plt.close('all')

def test_bar_wrong_len_dlf_names(annual_dlf1):
    with pytest.raises(ValueError):
        bar(annual_dlf1, 'year', 'm1', dlf_names=['d1', 'd2'])
    plt.close('all')
        
@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'})
def test_bar_single_var_single_dlf(annual_dlf1):
    fig, _ = bar(annual_dlf1, 'year', ['m1'], dlf_names=['Test dlf'], title='Test plot')
    return fig

@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'},
                               filename='test_bar_single_var_single_dlf.png')
def test_bar_single_var_single_dlf_dict(annual_dlf1):
    fig, _ = bar({'Test dlf' : annual_dlf1}, 'year', 'm1', title='Test plot')
    return fig


@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'})
def test_bar_two_vars_single_dlf(annual_dlf1):
    fig, _ = bar(annual_dlf1, 'year', ['m1', 'm2'])
    return fig

@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'})
def test_bar_two_vars_two_dlfs(annual_dlf1, annual_dlf2):    
    fig, _ = bar([annual_dlf1, annual_dlf2],
                 'year',
                 ['m1', 'm2'],
                 dlf_names=['d1', 'd2'],
                 title='Test plot')
    return fig

@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'},
                               filename='test_bar_two_vars_two_dlfs.png')
def test_bar_two_vars_two_dlfs_dict(annual_dlf1, annual_dlf2):    
    fig, _ = bar({'d1':annual_dlf1, 'd2':annual_dlf2},
                 'year',
                 ['m1', 'm2'],
                 title='Test plot')
    return fig
