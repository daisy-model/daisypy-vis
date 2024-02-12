'''Plot variables from daisy_vis.io.dlf.Dlf using points and lines'''
import matplotlib as mpl
from daisypy.vis.plot.base_plotter import plot_many, plot_many_docstring

__all__ = [
    'points_and_lines'
]

def points_and_lines(dlfs, x_var, y_vars, *,
            dlf_names=None,
            figsize=None,
            title=None,
            sharex=False,
            sharey=False,
            cmap=None,
            markers=None,
            linestyles=None
            ):
    # pylint: disable=too-many-arguments, missing-function-docstring
    # docstring is added after the function definition.
    if cmap is None:
        cmap = mpl.colormaps['tab10']
    if markers is None:
        markers = ['<', '>', 'x', 'o', '+', 's', 'p']
    if linestyles is None:
        linestyles = ['']
    def plotter(df, x_var, ax):
        y_vars = (col for col in df.columns if col != x_var)
        handles = []
        for i,y_var in enumerate(y_vars):
            handles.append(
                ax.plot(df[x_var],
                        df[y_var],
                        color=cmap(i % cmap.N),
                        marker=markers[i % len(markers)],
                        fillstyle='none',
                        linestyle=linestyles[i % len(linestyles)],
                        label=y_var
                        )[0] # ax.plot returns a list with an element for each pair of x,y 
            )
        ax.legend(handles=handles)
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

points_and_lines.__doc__ = plot_many_docstring('Points and line')
