'''Example illustrating how to make a scatter plot of daily logged variables
See the scenarios in test-data/daily
'''
import os
import sys
import matplotlib.pyplot as plt
import daisypy.vis as dv

def main():
    '''Run as `python <path/to/plot_daily_values.py>`'''
    dirname = os.path.dirname(os.path.realpath(sys.argv[0]))
    datadir = os.path.join(dirname, '..', '..', 'test-data', 'hourly')
    
    daily_soil_chemical(datadir)

def daily_soil_chemical(datadir):
    '''Scatter plot of daily soil chemical for a single scenario
    '''
    dlfs = {
        'P2D' : dv.io.read_dlf(os.path.join(datadir, 'P2D-Daily-Soil Chemical_110cm.dlf'))
    }
    variables = [
        'Leak-Matrix',
        'Leak-Biopores',
        'Uptake',
        'Transform'
    ]
    hour = 12
    dv.plot_daily(dlfs, variables, hour=hour, title=f'Soil chemical @ hour {hour}', plot_line=True)
    hour = 0
    dv.plot_daily(dlfs, variables, hour=hour, title=f'Soil chemical @ hour {hour}')
    plt.show()    

if __name__ == '__main__':
    main()
