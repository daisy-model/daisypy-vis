'''Example illustrating how to make a scatter plot of daily logged variables
See the scenarios in test-data/daily
'''
import os
import sys
import matplotlib.pyplot as plt
from daisy_vis.io import dlf
from daisy_vis.plot import plot_daily


def main():
    '''Run as `python <path-to-file>`'''
    dirname = os.path.dirname(os.path.realpath(sys.argv[0]))
    datadir = os.path.join(dirname, '..', '..', 'test-data', 'daily')
    
    daily_water_flux(datadir)

def daily_water_flux(datadir):
    '''Scatter plot of daily water flux at q in {0, -51, -100, -200}
    for a single scenario
    '''
    dlfs = {
        'DailyP' : dlf.read_dlf(os.path.join(datadir, 'DailyP/DailyP-Daily-WaterFlux.dlf'))
    }
    variables = [
        'q @ 0',
        'q @ -51',
        'q @ -100',
        'q @ -200',
    ]
    plot_daily(dlfs, variables, title='Daily Water Flux')
    plt.show()    

if __name__ == '__main__':
    main()
