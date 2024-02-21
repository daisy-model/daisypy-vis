'''Plot variables from daisy_vis.io.dlf.Dlf in a bar plot'''
# pylint: disable=disallowed-name; 'bar' is a valid name in this context
from daisypy.vis.plot.base_plotter import plot_many, plot_many_docstring

__all__ = [
    'bar'
]

def bar(dlfs, x_var, y_vars, *,
        dlf_names=None,
        figsize=None,
        title=None,
        sharex=False,
        sharey=False):   
    # pylint: disable=too-many-arguments, missing-function-docstring
    # docstring is added after the function definition.
    def plotter(df, x_var, ax):
        df.plot.bar(x=x_var, ax=ax)
    # pylint: disable=duplicate-code        
    return plot_many(dlfs,
                     x_var,
                     y_vars,
                     plotter,
                     dlf_names=dlf_names,
                     figsize=figsize,
                     title=title,
                     sharex=sharex,
                     sharey=sharey)

bar.__doc__ = plot_many_docstring('Bar')
