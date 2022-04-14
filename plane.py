from CesiumPy import Cartesian3, Plane
from geopy.distance import geodesic 
from building_data import *

data = building_data()
#print(data)
#print(type(data))
Coordinates  = data['Coordinates'][0]
Height = data['Height']
#print(len(Coordinates))
size = []
point_normal = []
Facade_planes = []
for i in range(len(Coordinates)-1):
    lat1 = Coordinates[i][1]
    lat2 = Coordinates[i+1][1]
    lon1 = Coordinates[i][0]
    lon2 = Coordinates[i+1][0]
    size.append([geodesic([lat1,lon1],[lat2,lon2]).m,Height])
    coordinate_1 = Cartesian3.fromDegrees(lon1,lat1)
    coordinate_2 = Cartesian3.fromDegrees(lon2,lat2)
    print(coordinate_2.x)
    print(coordinate_1.x)
    headway = Cartesian3.subtract(coordinate_2,coordinate_1)
    print(headway.x)
    print(headway.y)
    normal = Cartesian3(x=(-headway.y), y= headway.x, z=0)
    print(normal.x)
    print(normal.y)
    point_normal  = Cartesian3()
    point_normal.x = (coordinate_2.x+coordinate_1.x)/2
    point_normal.y = (coordinate_2.y+coordinate_1.y)/2
    point_normal.z = Height/2
    Facade_planes.append(Plane.fromPointNormal(point_normal,normal))



     
