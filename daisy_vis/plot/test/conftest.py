import pytest
import pandas as pd
from daisy_vis.io.dlf import Dlf

@pytest.fixture
def annual_dlf1():
    header = {}
    body = pd.DataFrame({
        'year' : list(range(1990, 2000)),
        'm1' : [4.77, 1.55, 4.19, 8.17, 7.36, 0.16, 2.09, 5.77, 7.34, 0.58],
        'm2' : [5.32, 7.27, 5.39, 7.80, 9.06, 2.89, 3.54, 6.86, 2.25, 3.65],
        'm3' : [103.62, 111.2, 109.06, 119.22, 102.62, 116.95, 120.63, 107.1, 104.45, 100.36],
        'm4' : [123.91, 124.14, 95.26, 131.78, 53.87, 70.55, 107.52, 119.9, 125.07, 75.8],
    })
    units = {'m1' : 'mm', 'm2' : 'mm', 'm3' : 'g', 'm4' : 'liter'}
    return Dlf(header, units, body)

@pytest.fixture
def annual_dlf2():
    header = {}
    body = pd.DataFrame({
        'year' : list(range(1990, 2000)),
        'm1' : [8.79, 5.46, 5.79, 6.95, 3.90, 3.23, 5.99, 2.52, 1.37, 2.00],
        'm2' : [5.53, 8.32, 6.25, 2.72, 5.12, 4.62, 3.81, 4.41, 9.51, 2.33],
        'm3' : [110.39, 124.53, 106.08, 122.5, 100.11, 113.93, 110.15, 101.6, 110.32, 110.87],
        'm4' : [119.93, 109.28, 74.56, 110.11, 88.26, 77.04, 93.08, 113.95, 98.78, 95.23],
    })
    units = {'m1' : 'mm', 'm2' : 'mm', 'm3' : 'g', 'm4' : 'liter'}
    return Dlf(header, units, body)


@pytest.fixture
def annual_dlf3():
    header = {}
    body = pd.DataFrame({
        'year' : list(range(1990, 2000)),
        'm1' : [0.08, 7.26, 9.98, 8.74, 6.08, 1.70, 6.80, 8.29, 7.41, 5.05],
        'm2' : [2.08, 7.55, 5.27, 8.20, 5.06, 7.77, 9.61, 8.37, 1.04, 0.70],
        'm3' : [110.62, 121.71, 116.68, 107.99, 117.37, 108.62, 115.48, 105.76, 115.81, 105.17],
        'm4' : [128.91, 62.31, 97.32, 103.31, 123.09, 90.9, 75.74, 143.52, 77.54, 103.4],
    })
    units = {'m1' : 'mm', 'm2' : 'mm', 'm3' : 'g', 'm4' : 'liter'}
    return Dlf(header, units, body)


@pytest.fixture
def annual_dlf4():
    header = {}
    body = pd.DataFrame({
        'year' : list(range(1990, 2000)),
        'm1' : [0.71, 9.31, 8.63, 1.97, 0.26, 6.51, 9.01, 2.16, 4.84, 1.19],
        'm2' : [7.91, 3.47, 9.86, 9.97, 3.22, 5.37, 5.71, 1.44, 1.16, 1.88],
        'm3' : [117.07, 107.59, 124.78, 105.62, 109.47, 114.51, 103.89, 115.17, 100.56, 103.93],
        'm4' : [129.36, 67.39, 89.52, 160.24, 87.78, 75.51, 71.29, 104.27, 99.07, 153.83],
    })
    units = {'m1' : 'mm', 'm2' : 'mm', 'm3' : 'g', 'm4' : 'liter'}
    return Dlf(header, units, body)

@pytest.fixture
def n_annual_dlfs(annual_dlf1, annual_dlf2, annual_dlf3, annual_dlf4):
    return [
        annual_dlf1,
        annual_dlf2,
        annual_dlf3,
        annual_dlf4,
    ]
        
