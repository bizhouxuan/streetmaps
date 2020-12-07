import sys
import math
import numpy as np
from scipy.stats import entropy
import argparse

def print_help():
    print('Usage: entropy.py FILE')
    print('Calculate the orientation entropy of a city\'s street network.')
    print('The FILE argument is the path to the file containing the two-col orientation distribution date.')
    print('e.g., 0.12527823  0.012408118')
    print('where, the first column is the orientation in radian and the second is the unnormalized probability.')

def calculate_entropy(orientations, frequencies, unit):
    bin_size = orientations[1]-orientations[0]
    if unit == 'deg':
        bin_size = bin_size*math.pi/180
    print('Bin size (radian): ',bin_size)
    orientation_entropy = entropy(frequencies)+math.log(bin_size)
    #orientation_entropy = entropy(frequencies-min(frequencies))+math.log(bin_size)
    print(orientation_entropy)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("delimiter", help="delimiter separating data in a row")
    parser.add_argument("skiprows", type=int, help="number of rows to skip")
    parser.add_argument("unit", help="Unit of angle (rad|deg)")
    parser.add_argument("filename", help="name of the data file")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        print_help()
        sys.exit(-1)
    delimiter = args.delimiter
    skiprows = args.skiprows
    unit = args.unit
    filename = args.filename
    try:
        orientations, frequencies= np.loadtxt(filename, usecols = (0,1), unpack=True, delimiter=delimiter, skiprows=skiprows)
        calculate_entropy(orientations, frequencies, unit)
    except Exception as e:
        print(f'Error: {e}.')
