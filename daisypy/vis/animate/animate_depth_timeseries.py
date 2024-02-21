# pylint: disable=missing-module-docstring
import plotly.express as px
from daisypy.vis.transform import daisy_time_to_timestamp, depth_wide_to_long

__all__ = [
    'animate_depth_timeseries'
]

def animate_depth_timeseries(dlf, var_name, *,
                             figsize=None,
                             title=None,
                             var_lim=None,
                             depth_lim=None
                             ):
    # pylint: disable=too-many-arguments
    '''
    Parameters
    ----------
    dlf : daisy_vis.io.dlf.Dlf

    var_name : str

    figsize : tuple of int, optional
      (width, height) of figure in pixels

    title : str, optional
      Title of figure

    var_lim : (float, float), optional
      Limit of `var_name` values that are plotted. If None it is set to the data limit with a 10%
      margin.

    depth_lim : (float,float), optional
      Limit of depth. If None it is set to the (lowest depth - 10, 10)    

    Returns
    -------
    plotly.graph_objs.Figure
    '''
    dlf = daisy_time_to_timestamp(dlf, 'time')
    dlf = depth_wide_to_long(dlf, var_name, 'time', 'z')
    if figsize is None:
        width, height = None, None
    else:
        width, height = figsize
    if var_lim is None:
        var_min = dlf.body[var_name].min()        
        var_max = dlf.body[var_name].max()
        var_lim = var_min - abs(var_min)*0.1, var_max + abs(var_max)*0.1
    if depth_lim is None:
        depth_lim = dlf.body['z'].min() - 10, 10
    return px.scatter(dlf.body,
                      x=var_name,
                      y='z',
                      animation_frame='time',
                      title=title,
                      width=width,
                      height=height,
                      range_x=var_lim,
                      range_y=depth_lim,)
