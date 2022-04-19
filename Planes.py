from CesiumPy import Cartesian3, Plane
from geopy.distance import geodesic 
import pandas as pd
import ast
import csv
from typing import NamedTuple


# class Record(NamedTuple):
#     """ Define the fields and their types in a record. """
#     Name: str
#     Height: float
#     Coordinates: ast.literal_eval  # Handles string represenation of literals.

#     @classmethod
#     def _transform(cls: 'Record', dict_: dict) -> dict:
#         """ Convert string values in given dictionary to corresponding Record
#             field type.
#         """
#         return {name: cls.__annotations__[name](value)
#                     for name, value in dict_.items()}


# filename = 'campus_buildings_data.csv'

# with open(filename, newline='') as file:
#     for i, row in enumerate(csv.DictReader(file)):
#         row = Record._transform(row)
#         # print(f'row {i}: {row}')
        
# csvfile  = csv.reader(file)
df = pd.read_csv('campus_buildings_data.csv')
df['Coordinates']=df['Coordinates'].apply(lambda x: ast.literal_eval(x))
print(type(df['Coordinates'][0]))
print(df.info())

Coordinates = df['Coordinates']
Height = df['Height']
print(Coordinates[0][0])
# print(len(data))
# print(type(data['Coordinates'][0]))
Dimensions = []
Planes = []

for k in range(len(df)):
    Coordinates[k].append(Coordinates[k][0]) 
    size = []
    point_normal = []
    Facade_planes = []

    for i in range(len(Coordinates[k])-1):
        lat1 = Coordinates[k][i][1]
        lat2 = Coordinates[k][i+1][1]
        lon1 = Coordinates[k][i][0]
        lon2 = Coordinates[k][i+1][0]
        size.append([geodesic([lat1,lon1],[lat2,lon2]).m,Height[k]])
        coordinate_1 = Cartesian3.fromDegrees(lon1,lat1)
        coordinate_2 = Cartesian3.fromDegrees(lon2,lat2)
        # print(coordinate_2.x)
        # print(coordinate_1.x)
        headway = Cartesian3.subtract(coordinate_2,coordinate_1)
        # print(headway.x)
        # print(headway.y)
        normal = Cartesian3(x=(-headway.y), y= headway.x, z=0)
        # print(normal.x)
        # print(normal.y)
        point_normal  = Cartesian3()
        point_normal.x = (coordinate_2.x+coordinate_1.x)/2
        point_normal.y = (coordinate_2.y+coordinate_1.y)/2
        point_normal.z = Height[k]/2
        Facade_planes.append(Plane.fromPointNormal(point_normal,normal))
    
    Dimensions.append(size)
    Planes.append(Facade_planes)
# print(Dimensions)
df['Dimensions'] = Dimensions
df['Planes'] = Planes
print(df.info())
df.to_csv('campus_building_data.csv', index= False)

     
