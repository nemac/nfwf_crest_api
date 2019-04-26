from collections import OrderedDict
from fiona.crs import from_epsg

ID_FIELD = 'hub_id'

HUBS_DONE_DIR = '/home/mgeiger/Projects/nfwf-meta/nfwf-tool-api/assets/natureserve/hubs_done_03272019/'

ZONAL_STATS_ENDPOINT = 'https://dm3kiccxv2.execute-api.us-east-1.amazonaws.com/Prod/zonal_stats'

SCHEMA_FOR_NEW_SHPFILE = OrderedDict({
    'geometry': 'Polygon',
    'properties': {
        'TARGET_FID': 'int',
        'hub_rnk': 'int',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'fishwild' : 'float',
        'hubs': 'float'
    }
})

FIELD_MAPS = {
    'hub_id' : 'TARGET_FID',
    'hub_rank' : 'hub_rnk',
    'fishandwildlife': 'fishwild',
}


