'''Functions for arcgis online'''

from arcgis.gis import GIS
import arcgis


'''Basics'''
def get_layer_by_id(item_id:str, layer_number: int = 0):
    
    item = gis.content.get(item_id)
    
    layer = item.layers[layer_number]
    
    return layer

'''Domains'''
def remove_domain_from_field(layer, field_name):
    update_dict = {
        "fields": [
            {
                "name": "{}".format(field_name),
                "domain": None
            }
        ]
    }
        
    return layer.manager.update_definition(json_dict=update_dict)
