
from fiona import collection
import sys, json, pdb

old_shapefile_path = sys.argv[1]
new_shapefile_path = sys.argv[2]

def diff_shp(old_shapefile_path, new_shapefile_path):
    old_shp = collection(old_shapefile_path, "r")
    new_shp = collection(new_shapefile_path, "r")
    for old_feature in old_shp:
        for new_feature in new_shp:
            if old_feature['id'] == new_feature['id']:
                if old_feature['properties'] != new_feature['properties']:
    	            print old_shapefile_path+': Properties: '+json.dumps(old_feature['properties'])
                    print new_shapefile_path+': Properties: '+json.dumps(new_feature['properties'])
                if old_feature['geometry']['coordinates'] != new_feature['geometry']['coordinates']:
                    pdb.set_trace()
                    for i in old_feature['geometry']['coordinates']:
                        pass
                        
	        


diff_shp(old_shapefile_path, new_shapefile_path)

