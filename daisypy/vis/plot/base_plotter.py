'''Plot variables from daisy_vis.io.dlf.Dlf using a supplied plotter function with the following
signature

  plotter : (pandas.DataFrame, x_var, ax) -> ()

'''
import math
import warnings
import matplotlib.pyplot as plt
from daisypy.vis.io import Dlf

__all__ = [
    'plot_many'
]

def plot_many_docstring(name=None):
    '''Get a docstring for a plot function

    Parameters
    ----------
    name : str
      If not None the name is used in the docstring

    Returns
    -------
    docstring : str
    '''
    return f'''{'Plot' if name is None else name + ' plot'} dlf variables

    Creates a subplot for each variable.

    In the following let Dlf = daisy_vis.io.dlf.Dlf
    
    Parameters
    ----------
    dlfs : Dlf OR sequence of Dlf or dict of Dlf
      Dlf object containing the data to plot

    x_var : str
      Variable to use as x variable

    y_vars : str of sequence of str
      Variable(s) to use as y values. 
    
    plotter : callable : (pandas.DataFrame, x_var, ax) -> ()
      Function that plots a dataframe on a given axes

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

def plot_many(dlfs, x_var, y_vars, plotter, *,
        dlf_names=None,
        figsize=None,
        title=None,
        sharex=False,
        sharey=False):
    # pylint: disable=too-many-arguments, missing-function-docstring
    # docstring is added after the function definition.
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
        plot_single(dlfs, x_var, y_var, plotter, axs[n//cols,n%cols], dlf_names=dlf_names)
    if title is not None:
        plt.suptitle(title)
    if not sharex:
        plt.subplots_adjust(hspace=0.3) 
    return fig, axs

plot_many.__doc__ = plot_many_docstring()


def plot_single(dlfs, x_var, y_var, plotter, ax, *, dlf_names=None):
    # pylint: disable=too-many-arguments
    '''Plot a single dlf variable

    In the following let Dlf = daisy_vis.io.dlf.Dlf
    
    Parameters
    ----------
    dlfs : Dlf OR sequence of Dlf or dict of Dlf
      Dlf object containing the data to plot

    x_var : str
      Variable to use as x variable

    y_var : str 
      Variable to use as y values. 

    plotter : callable : (pandas.DataFrame, x_var, ax) -> ()
      Function that plots a dataframe on a given axes

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
    if isinstance(dlfs, Dlf):
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
    plotter(df, x_var, ax)
    ax.set_title(y_var)
    ax.set_ylabel(unit)
    return ax
    
