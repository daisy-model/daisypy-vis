'''Test bar plot'''
# It seems pointless with docstrings on these functions, so we just disable the warnings
# pylint: disable=missing-function-docstring
import pytest
from daisy_vis.plot import bar

def test_bar_no_dlf():
    with pytest.raises(ValueError):
        bar('year', 'm1', [])

def test_bar_dlf_dict_names_given(annual_dlf1):
    with pytest.warns(UserWarning):
        bar('year', 'm1', {'d1' : annual_dlf1}, dlf_names=['d2'])

def test_bar_wrong_len_dlf_names(annual_dlf1):
    with pytest.raises(ValueError):
        bar('year', 'm1', annual_dlf1, dlf_names=['d1', 'd2'])
        
@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'})
def test_bar_single_var_single_dlf(annual_dlf1):
    fig, _ = bar('year', ['m1'], annual_dlf1, dlf_names=['Test dlf'], title='Test plot')
    return fig

@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'},
                               filename='test_bar_single_var_single_dlf.png')
def test_bar_single_var_single_dlf_dict(annual_dlf1):
    fig, _ = bar('year', 'm1', {'Test dlf' : annual_dlf1}, title='Test plot')
    return fig


@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'})
def test_bar_two_vars_single_dlf(annual_dlf1):
    fig, _ = bar('year', ['m1', 'm2'], annual_dlf1)
    return fig

@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'})
def test_bar_two_vars_two_dlfs(annual_dlf1, annual_dlf2):    
    fig, _ = bar(
        'year',
        ['m1', 'm2'],
        [annual_dlf1, annual_dlf2],
        dlf_names=['d1', 'd2'],
        title='Test plot'
    )
    return fig

@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'},
                               filename='test_bar_two_vars_two_dlfs.png')
def test_bar_two_vars_two_dlfs_dict(annual_dlf1, annual_dlf2):    
    fig, _ = bar(
        'year',
        ['m1', 'm2'],
        {'d1':annual_dlf1, 'd2':annual_dlf2},
        title='Test plot'
    )
    return fig
