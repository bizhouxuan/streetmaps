import sys
import math
import numpy as np
from scipy.stats import entropy

def print_help():
    print('Usage: radial_entropy.py FILE')
    print('Calculate the spatial freguency entropy of a city\'s street network.')
    print('The FILE argument is the path to the file containing the two-col k distribution date.')
    print('e.g., 0.12527823  0.012408118')
    print('where, the first column is the wave vector k in 1/m and the second is the PSD (power spectral density).')

def calculate_entropy(k, psd):
    bin_size = k[1]-k[0]
    print('Bin size (1/m): ',bin_size)
    #For radial distribution, may NOT need to subtract the background from the PSDF curve before calculating entropy.
    orientation_entropy = entropy(psd)+math.log(bin_size)
    print(orientation_entropy)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_help()
        sys.exit(-1)
    filename = sys.argv[1]
    try:
        k=np.loadtxt(filename)[:, 0]
        psd=np.loadtxt(filename)[:, 1]
        calculate_entropy(k, psd)
    except Exception as e:
        print(f'Error: {e}.')
