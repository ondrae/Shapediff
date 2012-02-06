
from fiona import collection
import sys, json, pdb

old_shapefile_path = sys.argv[1]
new_shapefile_path = sys.argv[2]

def diff_shp(old_shapefile_path, new_shapefile_path):
    old_shp = collection(old_shapefile_path, "r")
    for old_feature in old_shp:
        #pdb.set_trace()
        new_shp = collection(new_shapefile_path, "r")
        for new_feature in new_shp:
            if old_feature['id'] == new_feature['id']:
                if old_feature['properties'] != new_feature['properties']:
    	            print old_shapefile_path+': Properties: '+json.dumps(old_feature['properties'])

                    print new_shapefile_path+': Properties: '+json.dumps(new_feature['properties'])
	        


diff_shp(old_shapefile_path, new_shapefile_path)

