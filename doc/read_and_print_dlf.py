import os
import sys
from daisy_vis.io import dlf

def main():
    dirname = os.path.dirname(os.path.realpath(sys.argv[0]))
    path = os.path.join(dirname, 'example-data', 'DailyP-Daily-WaterFlux.dlf')
    soil_tracer = dlf.read_dlf(path)
    for k,v in soil_tracer.header.items():
        print(f'{k} : {v}')
    print('--------------------')
    for col, unit in soil_tracer.units.items():
        print(f'{col} : {unit}')
    print('--------------------')
    print(soil_tracer.body)


if __name__ == '__main__':
    main()
