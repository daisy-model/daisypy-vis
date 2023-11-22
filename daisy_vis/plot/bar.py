'''Plot variables from daisy_vis.io.dlf.Dlf in a bar plot'''
# pylint: disable=disallowed-name; 'bar' is a valid name in this context
import math
import warnings
import matplotlib.pyplot as plt
from daisy_vis.io import dlf

__all__ = [
    'bar'
]

def bar(x_var, y_vars, dlfs, *,
        dlf_names=None,
        figsize=None,
        title=None,
        sharex=False,
        sharey=False):
    # pylint: disable=too-many-arguments
    '''Bar plot of dlf variables

    Creates a subplot for each variable. Bars are grouped by x_var

    In the following let Dlf = daisy_vis.io.dlf.Dlf
    
    Parameters
    ----------
    x_var : str
      Variable to use as x variable

    y_vars : str of sequence of str
      Variable(s) to use as y values. 
    
    dlfs : Dlf OR sequence of Dlf or dict of Dlf
      Dlf object containing the data to plot

    dlf_names : sequence of str
      Names of the dlfs to display in the plot legend.
      If not None then len(dlf_names) == len(dlf).
      Ignored if dlfs is a dict.

    figsize : tuple of int
      Size of figure

    title : str
      Title of plot

    sharex : Bool
      If True subplots share x-axis

    sharey : Bool
      If True subplots share y-axis

    Returns
    -------
    fig : matplotlib.figure.Figure
    axs : matplotlib.axes.Axes or numpy.ndarray of matplotlib.axes.Axes
    '''
    if isinstance(y_vars, str):
        y_vars = [y_vars]
    rows = math.floor(math.sqrt(len(y_vars)))
    cols = math.ceil(len(y_vars) / rows)
    if figsize is None:
        figsize = cols*6, rows*5
    fig, axs = plt.subplots(
        rows,
        cols,
        figsize=figsize,
        sharex=sharex,
        sharey=sharey,
        squeeze=False
    )
    for n, y_var in enumerate(y_vars):
        single_var_bar(x_var, y_var, dlfs, axs[n//cols,n%cols], dlf_names=dlf_names)
    if title is not None:
        plt.suptitle(title)
    if not sharex:
        plt.subplots_adjust(hspace=0.3) 
    return fig, axs


def single_var_bar(x_var, y_var, dlfs, ax, *, dlf_names=None):
    '''Bar plot of a single dlf variable

    In the following let Dlf = daisy_vis.io.dlf.Dlf
    
    Parameters
    ----------
    x_var : str
      Variable to use as x variable

    y_var : str 
      Variable to use as y values. 
    
    dlfs : Dlf OR sequence of Dlf or dict of Dlf
      Dlf object containing the data to plot

    ax : matplotlib.axes.Axes
      axes to plot to. If None a new figure with a single axes is created.

    dlf_names : sequence of str
      Names of the dlfs to display in the plot legend.
      If not None then len(dlf_names) == len(dlf).
      Ignored if dlfs is a dict.

    Returns
    -------
    ax : matplotlib.axes.Axes
    '''    
    if isinstance(dlfs, dlf.Dlf):
        dlfs = [dlfs]
        
    if len(dlfs) == 0:
        raise ValueError('Must provide at least one dlf object')

    if isinstance(dlfs, dict):
        if dlf_names is not None:
            warnings.warn('dlf_names supplied but dlfs is a dict. Ignoring dlf_names')
    else:
        if dlf_names is not None:
            if len(dlfs) != len(dlf_names):
                raise ValueError('Length of dlf_names must match length of dlfs')
            dlfs = dict(zip(dlf_names, dlfs))
        else:
            dlfs = dict(enumerate(dlfs, start=1))

    df = None
    unit = None
    for name, (_,units,body) in dlfs.items():
        df0 = body[[x_var, y_var]].rename(columns={y_var : name})
        if df is None:
            df =  df0
            unit = units[y_var]
        else:
            df = df.merge(df0, on=x_var)
    df.plot.bar(x=x_var, ax=ax)
    ax.set_title(y_var)
    ax.set_ylabel(unit)
    return ax
    
