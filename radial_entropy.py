import sys
import math
import numpy as np
from scipy.stats import entropy
import argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument("delimiter", help="delimiter separating data in a row")
    parser.add_argument("skiprows", type=int, help="number of rows to skip")
    parser.add_argument("filename", help="name of the data file")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        print_help()
        sys.exit(-1)
    delimiter = args.delimiter
    skiprows = args.skiprows
    filename = args.filename
    try:
        k, psd= np.loadtxt(filename, usecols = (0,1), unpack=True, delimiter=delimiter, skiprows=skiprows)
        calculate_entropy(k, psd)
    except Exception as e:
        print(f'Error: {e}.')
