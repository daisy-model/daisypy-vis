'''Test plot_daily'''
import pytest
from daisy_vis.plot import plot_daily

@pytest.mark.mpl_image_compare
def test_plot_daily(daily_dlf1):
    fig, ax = plot_daily({'D1' : daily_dlf1}, ['y2'], figsize=(10,10))
    fig.tight_layout()
    return fig

@pytest.mark.mpl_image_compare(filename='test_plot_daily.png')
def test_plot_daily_list(daily_dlf1):
    fig, ax = plot_daily([daily_dlf1], ['y2'], dlf_names=['D1'], figsize=(10,10))
    fig.tight_layout()
    return fig

@pytest.mark.mpl_image_compare
def test_plot_daily_line(daily_dlf1):
    fig, ax = plot_daily(daily_dlf1, ['y1', 'y2'], figsize=(15,10), plot_line=True)
    fig.tight_layout()
    return fig
