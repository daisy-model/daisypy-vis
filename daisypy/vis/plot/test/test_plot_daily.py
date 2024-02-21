'''Test plot_daily'''
import pytest
from daisypy.vis.plot import plot_daily

@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'})
def test_plot_daily(daily_dlf1):
    '''Test plot_daily with dict of dlfs'''
    fig, _ = plot_daily({'D1' : daily_dlf1}, ['y2'], figsize=(10,10))
    fig.tight_layout()
    return fig

@pytest.mark.mpl_image_compare(style="default",
                               savefig_kwargs={'bbox_inches' : 'tight'},
                               filename='test_plot_daily.png')
def test_plot_daily_list(daily_dlf1):
    '''Test plot_daily with list of dlfs and list of dlf_names'''
    fig, _ = plot_daily([daily_dlf1], ['y2'], dlf_names=['D1'], figsize=(10,10))
    fig.tight_layout()
    return fig

@pytest.mark.mpl_image_compare(style="default", savefig_kwargs={'bbox_inches' : 'tight'})
def test_plot_daily_line(daily_dlf1):
    '''Test plot_daily with unnamed dlf'''
    fig, _ = plot_daily(daily_dlf1, ['y1', 'y2'], figsize=(15,10), plot_line=True)
    fig.tight_layout()
    return fig
