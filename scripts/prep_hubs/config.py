from collections import OrderedDict
from fiona.crs import from_epsg

ID_FIELD_IN = 'OBJECTID'
ID_FIELD_OUT = 'TARGET_FID'

SCHEMA_FOR_NEW_SHPFILE = OrderedDict({
    'geometry': 'Polygon',
    'properties': {
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
    'OBJECTID': 'TARGET_FID',
    'terrestrial': 'terrestri',
    'crit_facilities': 'crit_fac',
    'pop_density': 'pop_dens',
    'social_vuln': 'soc_vuln',
    'floodprone_areas': 'floodprone',
    'sea_level_rise': 'slr',
    'storm_surge': 'stormsurge'
}


