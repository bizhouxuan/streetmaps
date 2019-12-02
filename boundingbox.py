from pyproj import Geod
import numpy as np

wgs84_geod = Geod(ellps='WGS84')
coordsStrings = np.array(['40.63', '40.8009249', '-73.9626879', '-73.7001809'])
coords = coordsStrings.astype(np.float)
lat_delta = coords[1]-coords[0]
lon_delta = coords[3]-coords[2]
lat = coords[0]+0.5*lat_delta
lon = coords[2]+0.5*lon_delta
_,_,width = wgs84_geod.inv(float(coords[2]),lat,float(coords[3]),lat)
_,_,height = wgs84_geod.inv(lon,float(coords[0]), lon,float(coords[1]))
print("{:.3f}".format(width/1000.0), "{:.3f}".format(height/1000.0))
