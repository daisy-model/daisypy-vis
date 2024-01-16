'''Animate daily waterflux'''
import os
import sys
from dash import Dash, dcc, html
from daisy_vis.io.dlf import read_dlf
from daisy_vis.animate import animate_depth_timeseries

def main():
    '''Run as `python <path/to/animate_depth_dependent.py>`'''
    dirname = os.path.dirname(os.path.realpath(sys.argv[0]))
    path = os.path.join(
        dirname, '..', '..', 'test-data', 'daily', 'DailyP', 'DailyP-Daily-WaterFlux.dlf'
    )
    dlf = read_dlf(path)
    var_name = 'q'
    fig = animate_depth_timeseries(var_name, dlf)
    
    app = Dash(__name__)
    app.layout = html.Div(children=[
        html.H1(children='DailyP'),
        html.Div(children='Daily logged waterflux'),
        dcc.Graph(
            id='daily-waterflux',
            figure=fig
        )
    ])        
    app.run(debug=True)

if __name__ == '__main__':
    main()
