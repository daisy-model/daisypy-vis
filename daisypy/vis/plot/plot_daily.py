'''Functions for plotting daily logged variables'''
import pandas as pd
from daisypy.vis.io import dlf
from daisypy.vis.plot import points_and_lines

__all__ = [
    'plot_daily',
]

COL_NAME_FOR_PLOT = 'daily-plot-date'

def plot_daily(dlfs, variables, *,
               hour=0,
               dlf_names=None,
               figsize=None,
               title=None,
               plot_line=False):
    # pylint: disable=too-many-arguments
    '''Scatter plot of daily logged variables

    Creates a subplot for each variable. 

    In the following let Dlf = daisy_vis.io.dlf.Dlf
    
    Parameters
    ----------
    dlfs : Dlf OR sequence of Dlf or dict of Dlf
      Dlf object containing the data to plot

    variables : sequence of str
      Names of variables to plot

    hour : int
      Hour of the day to plot.

    dlf_names : sequence of str
      Names of the dlfs to display in the plot legend.
      If not None then len(dlf_names) == len(dlf).
      Ignored if dlfs is a dict.

    figsize : tuple of int
      Size of figure

    title : str
      Title of plot

    plot_line : bool
      If True add a line plot

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes or numpy.ndarray of matplotlib.axes.Axes
    '''
    # Filter so we only plot those at the correct hour and add a date field so we get nice labels
    if isinstance(dlfs, dlf.Dlf):
        dlfs = prepare_dlf(dlfs, hour)
    elif isinstance(dlfs, dict):
        dlfs = {k : prepare_dlf(dlf_, hour) for k,dlf_ in dlfs.items()}
    else:
        dlfs = [prepare_dlf(dlf_, hour) for dlf_ in dlfs]
    linestyles = ['-'] if plot_line else None
    fig, axs = points_and_lines(dlfs, COL_NAME_FOR_PLOT, variables,
                                dlf_names=dlf_names,
                                figsize=figsize,
                                title=title,
                                linestyles=linestyles,
                                sharex=True)
    for ax in axs.flatten():
        ax.tick_params(axis='x', labelrotation=90)
    return fig, axs

    
def prepare_dlf(dlf_, hour):
    '''Transform a dlf so it can be plotted as a daily value
    Remove all time points except those at the given hour, and make a nice date field

    dlf_ : dlf.Dlf

    hour : int (0 <= hour <= 23)

    Returns
    -------
    transformed_dlf : dlf.Dlf
    '''
    def make_timestamp(series):
        return pd.Timestamp(year=int(series['year']),
                            month=int(series['month']),
                            day=int(series['mday']),
                            hour=hour)
    # We need to ensure that we are working on a copy of the data and not on a view. Otherwise we
    # might end up changing the original data, and we dont want that,
    body = dlf_.body[dlf_.body['hour'] == hour].copy()
    body[COL_NAME_FOR_PLOT] = body.apply(make_timestamp, axis=1)
    body = body.sort_values(by=COL_NAME_FOR_PLOT)
    return dlf.Dlf(dlf_.header, dlf_.units, body)
