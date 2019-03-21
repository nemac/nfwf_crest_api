from collections import OrderedDict
from fiona.crs import from_epsg

ID_FIELD = 'OBJECTID'

HUBS_DONE_DIR = '/home/mgeiger/Projects/nfwf-meta/nfwf-tool-api/assets/hubs_done_01022019/'

ZONAL_STATS_ENDPOINT = 'https://lg0njzoglg.execute-api.us-east-1.amazonaws.com/Prod/zonal_stats'

SCHEMA_FOR_NEW_SHPFILE = OrderedDict({
    'geometry': 'Polygon',
    'properties': {
        'id': 'str',
        'Join_Count': 'int',
        'TARGET_FID': 'int',
        'hub_rnk': 'int',
        'acres': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'aquatic': 'float',
        'terrestri': 'float',
        'hubs': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'drainage': 'float',
        'erosion': 'float',
        'floodprone': 'float',
        'geostress': 'float',
        'slr': 'float',
        'slope': 'float',
        'stormsurge': 'float'
    }
})

FIELD_MAPS = {
    'terrestrial': 'terrestri',
    'crit_facilities': 'crit_fac',
    'pop_density': 'pop_dens',
    'social_vuln': 'soc_vuln',
    'floodprone_areas': 'floodprone',
    'sea_level_rise': 'slr',
    'storm_surge': 'stormsurge'
}


