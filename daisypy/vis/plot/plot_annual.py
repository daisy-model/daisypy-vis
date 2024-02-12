'''Functions for plotting annually logged variables'''
from daisypy.vis.plot import bar

__all__ = [
    'plot_annual',
]

def plot_annual(dlfs, variables, *, dlf_names=None, figsize=None, title=None):
    '''Bar plot of annually logged variables

    Creates a subplot for each variable. Bars are grouped by year.

    In the following let Dlf = daisy_vis.io.dlf.Dlf
    
    Parameters
    ----------
    dlfs : Dlf OR sequence of Dlf or dict of Dlf
      Dlf object containing the data to plot

    variables : sequence of str
      Names of variables to plot

    dlf_names : sequence of str
      Names of the dlfs to display in the plot legend.
      If not None then len(dlf_names) == len(dlf).
      Ignored if dlfs is a dict.

    figsize : tuple of int
      Size of figure

    title : str
      Title of plot

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes or numpy.ndarray of matplotlib.axes.Axes
    '''
    return bar(dlfs, 'year', variables,
               dlf_names=dlf_names,
               figsize=figsize,
               title=title,
               sharex=True)

    

