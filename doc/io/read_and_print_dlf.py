'''Read a dlf file and print
info
header
body
'''
import os
import sys
from daisypy.vis import read_dlf

def main():
    '''Run as `python <path/to/read_and_print.dlf>`'''
    dirname = os.path.dirname(os.path.realpath(sys.argv[0]))
    path = os.path.join(
        dirname, '..', '..', 'test-data', 'daily', 'DailyP', 'DailyP-Daily-WaterFlux.dlf'
    )
    soil_tracer = read_dlf(path)
    for k,v in soil_tracer.header.items():
        print(f'{k} : {v}')
    print('--------------------')
    for col, unit in soil_tracer.units.items():
        print(f'{col} : {unit}')
    print('--------------------')
    print(soil_tracer.body)


if __name__ == '__main__':
    main()
