import requests


# locations = {
#     'buffaloUBnorth': {
#         'minX': 9211,
#         'maxX': 9214,
#         'minY': 12039,
#         'maxY': 12040
#     }
# }

x = 9211
y = 12039

university_campus = []

for l in range(4):
    for m in range(2):
        # print(x+l, y+m)
        response = requests.get(f'https://data.osmbuildings.org/0.2/anonymous/tile/15/{x+l}/{y+m}.json')
        response_data = response.json()
        for i in range(len(response_data['features'])):
            if 'type' in response_data['features'][i]['properties'].keys():
                if response_data['features'][i]['properties']['type'] == 'university':
                    if 'name' in response_data['features'][i]['properties'].keys():
                        location = {
                        'Name': response_data['features'][i]['properties']['name'],
                        'Height': response_data['features'][i]['properties']['height'],
                        'Coordinates': response_data['features'][i]['geometry']['coordinates']
                        }
                    university_campus.append(location)

# print((university_campus[0]))
# print((university_campus[0]['Coordinates']))
# print((university_campus[0]['Coordinates'][0]))
# print((university_campus[0]['Coordinates'][0][0]))

print(university_campus)

# Cartesian to Cartographic

# for i in range(len(university_campus)):
#     print(university_campus[i]['Name'])

# 2 places without name


# response = requests.get(f'https://data.osmbuildings.org/0.2/anonymous/tile/15/9211/12040.json')
#
# response_data = response.json()
#
# for i in range(len(response_data['features'])):
#     if 'type' in response_data['features'][i]['properties'].keys():
#         if response_data['features'][i]['properties']['type'] == 'university':
#             print(response_data['features'][i]['geometry']['coordinates'])

