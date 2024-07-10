'''Animate daily waterflux'''
import os
import sys
from dash import Dash, dcc, html
import daisypy.vis as dv

def main():
    '''Run as `python <path/to/animate_depth_dependent.py>`'''
    dirname = os.path.dirname(os.path.realpath(sys.argv[0]))
    path = os.path.join(
        dirname, '..', '..', 'test-data', 'daily', 'DailyP', 'DailyP-Daily-WaterFlux.dlf'
    )
    dlf = dv.read_dlf(path)
    var_name = 'q'
    fig = dv.animate_depth_timeseries(dlf, var_name, figsize=(1000,1000))
    
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
