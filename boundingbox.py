import sys
from pyproj import Geod
import numpy as np

def print_help():
    print('Usage: boundingbox.py lat_bot lat_top lon_left lon_right')
    print('Calculate the dimensions of the bounding box, in km.')
    print('The GPS coordinates should in degrees.')

def calculate_box_dimensions(lat_bot, lat_top, lon_left, lon_right):
    wgs84_geod = Geod(ellps='WGS84')
    coordsStrings = np.array([lat_bot, lat_top, lon_left, lon_right])
    coords = coordsStrings.astype(np.float)
    lat_delta = coords[1]-coords[0]
    lon_delta = coords[3]-coords[2]
    lat = coords[0]+0.5*lat_delta
    lon = coords[2]+0.5*lon_delta
    _,_,width = wgs84_geod.inv(float(coords[2]),lat,float(coords[3]),lat)
    _,_,height = wgs84_geod.inv(lon,float(coords[0]), lon,float(coords[1]))
    print("{:.3f}".format(width/1000.0), "{:.3f}".format(height/1000.0))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_help()
        sys.exit(-1)
    lat_bot = sys.argv[1]
    lat_top = sys.argv[2]
    lon_left = sys.argv[3]
    lon_right = sys.argv[4]
    calculate_box_dimensions(lat_bot, lat_top, lon_left, lon_right)
