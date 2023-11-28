'''Example illustrating how to make a bar plot of annualy logged variables for multiple scenarios
See the scenarios in test-data/annual
'''
import os
import sys
import matplotlib.pyplot as plt
from daisy_vis.io import dlf
from daisy_vis.plot import plot_annual


def main():
    '''Run as `python <path-to-file>`'''
    dirname = os.path.dirname(os.path.realpath(sys.argv[0]))
    datadir = os.path.join(dirname, '..', '..', 'test-data', 'annual')
    annual_field_nitrogen(datadir)
    annual_tracer(datadir)


def annual_field_nitrogen(datadir):
    '''Bar plot of annual field nitrogen variables:
    Matrix-Leaching, Crop-Uptake, Soil-Drain and Surface-Loss
    for four scenarios

    Biopore-Leaching is not included as it is zero in all scenarios.
    '''
    dlfs = [
        dlf.read_dlf(p) for p in [
            os.path.join(datadir, 'Annual-FN/HourlyP-Annual-FN-2.2b.dlf'),
            os.path.join(datadir, 'Annual-FN/HourlyP-Annual-FN-2.3b.dlf'),
            os.path.join(datadir, 'Annual-FN/HourlyP-Annual-FN-2.4b.dlf'),
            os.path.join(datadir, 'Annual-FN/HourlyP-Annual-FN-2.5b.dlf')
        ]
    ]
    dlf_names = ['2.2b', '2.3b', '2.4b', '2.5b']
    variables = [
        'Matrix-Leaching',
        #'Biopore-Leaching',
        'Crop-Uptake',
        'Soil-Drain',
        'Surface-Loss'
    ]
    plot_annual(dlfs, variables, dlf_names=dlf_names, title='Annual Field Nitrogen')
    plt.show()


def annual_tracer(datadir):
    '''Bar plot of annual tracer variables:
    Leak matrix, Uptake, Soil drain and Runoff
    for four scenarios

    Leak biopores is not included as it is zero in all scenarios.
    '''
    dlfs = [
        dlf.read_dlf(p) for p in [
            os.path.join(datadir, 'Annual-Tracer/HourlyP-Annual-Tracer-2.2b.dlf'),
            os.path.join(datadir, 'Annual-Tracer/HourlyP-Annual-Tracer-2.3b.dlf'),
            os.path.join(datadir, 'Annual-Tracer/HourlyP-Annual-Tracer-2.4b.dlf'),
            os.path.join(datadir, 'Annual-Tracer/HourlyP-Annual-Tracer-2.5b.dlf')
        ]
    ]
    variables = [
        'Leak matrix',
        #'Leak biopores',
        'Uptake',
        'Soil drain',
        'Runoff'
    ]
    dlf_names = ['2.2b', '2.3b', '2.4b', '2.5b']
    plot_annual(dlfs, variables, dlf_names=dlf_names, title='Annual Tracer')
    plt.show()
    

if __name__ == '__main__':
    main()
