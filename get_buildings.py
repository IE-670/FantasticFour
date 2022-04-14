'''
This script can be used to download OSMbuilding data.

You'll need to know the min/max x/y coordinates for the tiles.

See https://osmbuildings.org/documentation/data/ 
for more info.

NOTE:  This assumes that the appropriate subdirectories within 
       `json_data/` (e.g., `buffaloDowntown` or `buffaloUBnorth`)
       have already been created.  If those directories don't yet
       exist, python will complain.
'''

import urllib.request, json 
import time


locations = {
	'buffaloDowntown': {
		'minX': 9202,
		'maxX': 9211,
		'minY': 12051,
		'maxY': 12061
	},
	'buffaloUBnorth': {
		'minX': 9211,
		'maxX': 9214,
		'minY': 12039,
		'maxY': 12040
	}
}

for loc in locations:
	for x in range(locations[loc]['minX'], locations[loc]['maxX']+1):
		for y in range(locations[loc]['minY'], locations[loc]['maxY']+1):
			print('x = ', x, ' | y = ', y)
			myURL = f'https://data.osmbuildings.org/0.2/anonymous/tile/15/{x}/{y}.json')
			with urllib.request.urlopen(myURL) as url:
				try:
					data = json.loads(url.read().decode())
					
					# Cesium complains if single quotes are used.
					# json.dumps converts our data into the 
					# correct format. 
					newData = json.dumps(data)
				
					# print(newData)
				
					# See note at top of file if you get errors here.
					f = open("json_data/%s/%d-%d.json" % (loc, x, y), "w")
					f.write(str(newData))
					f.close()
					
					# OSMbuildings doesn't want you to do bulk downloading.
					# Sleeping for 1 second seems to be sufficient to
					# avoid getting blocked by their server.
					time.sleep(1.0)
				except:
					print('\t failed to load')
		