from collections import OrderedDict

config = {
  'continental_us': {
    'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'TARGET_FID': 'int',
        'hub_rnk': 'int',
        'wildlife': 'float',
        'acres': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'aquatic': 'float',
        'terrestri': 'float',
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
        'stormsurge': 'float',
        'erosion': 'float'
      }
    }),
    'field_maps': {
      'OBJECTID': 'TARGET_FID',
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'storm_surge': 'stormsurge'
    },
  },

  'us_virgin_islands': {
    'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'TARGET_FID': 'int',
        'hub_rnk': 'int',
        'acres': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'terrestri': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'erosion': 'float',
        'floodprone': 'float',
        'slr': 'float',
        'stormsurge': 'float',
        'impermeabl': 'float',
        'low_areas': 'float',
        'marine': 'float',
        'wildlife': 'float'
      }
    }),
    'field_maps': {
      'OBJECTID': 'TARGET_FID',
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'storm_surge': 'stormsurge',
      'impermeable': 'impermeabl',
      'rank_val': 'hub_rnk'
    }
  },

  'puerto_rico': {
    'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'TARGET_FID': 'int',
        'wildlife': 'float',
        'hub_rnk': 'int',
        'acres': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'terrestri': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'erosion': 'float',
        'floodprone': 'float',
        'slr': 'float',
        'stormsurge': 'float',
        'impermeabl': 'float',
        'landslides': 'float',
        'low_areas': 'float',
        'marine': 'float',
        'tsunami': 'float'
      }
    }),
    'field_maps': {
      'OBJECTID': 'TARGET_FID',
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'storm_surge': 'stormsurge',
      'impermeable': 'impermeabl',
      'rank_val': 'hub_rnk'
    }
  },

  'northern_mariana_islands': {
    'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'TARGET_FID': 'int',
        'wildlife': 'float',
        'hub_rnk': 'int',
        'acres': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'terrestri': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'erosion': 'float',
        'floodprone': 'float',
        'slr': 'float',
        'impermeabl': 'float',
        'low_areas': 'float',
        'marine': 'float',
        'wave_flood': 'float'
      }
    }),
    'field_maps': {
      'OBJECTID': 'TARGET_FID',
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'impermeable': 'impermeabl',
      'wave_flooding': 'wave_flood',
      'rank_val': 'hub_rnk'
    }
  },

  'hawaii': {
    'id': { 'in': 'TARGET_FID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'TARGET_FID': 'int',
        'wildlife': 'float',
        'hub_rnk': 'int',
        'acres': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'terrestri': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'erosion': 'float',
        'floodprone': 'float',
        'slr': 'float',
        'impermeabl': 'float',
        'low_areas': 'float',
        'marine': 'float',
        'tsunami': 'float',
        'landslides': 'float',
        'stormsurge': 'float'
      }
    }),
    'field_maps': {
      'storm_surge': 'stormsurge',
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'impermeable': 'impermeabl',
      'hub_rank': 'hub_rnk'
    }
  },

  'american_samoa': {
    'id': { 'in': 'TARGET_FID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'TARGET_FID': 'int',
        'acres': 'float',
        'core_type': 'str',
        'wildlife': 'float',
        'hub_rnk': 'int',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'floodprone': 'float',
        'slr': 'float',
        'impermeabl': 'float',
        'marine': 'float',
        'tsunami': 'float',
        'wave_fld': 'float',
        'slope': 'float',
        'terrestri': 'float',
        'erosion': 'float'
      }
    }),
    'field_maps': {
      'TARGET_ID': 'TARGET_FID',
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'impermeable': 'impermeabl',
      'wave_flooding' : 'wave_fld',
      'Rank': 'hub_rnk'
    }
  },

  'guam': {
    'id': { 'in': 'hub_id', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon',
      'properties': {
        'acres': 'float',
        'TARGET_FID': 'int',
        'wildlife': 'float',
        'hub_rnk': 'int',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'pop_dens': 'float',
        'soc_vuln': 'float',
        'floodprone': 'float',
        'slr': 'float',
        'impermeabl': 'float',
        'marine': 'float',
        'tsunami': 'float',
        'wave_fld': 'float',
        'wave_exp': 'float',
        'slope': 'float',
        'terrestri': 'float',
        'erosion': 'float',
        'landslides': 'float',
      }
    }),
    'field_maps': {
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'impermeable': 'impermeabl',
      'Rank': 'hub_rnk',
      'wave_exposure': 'wave_exp',
      'wave_flooding': 'wave_fld',
      'hub_id': 'TARGET_FID'
    }
  },
  'alaska': {
    'id': { 'in': 'hub_id', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': 'Polygon', 
      'properties': {
        'acres': 'float',
        'TARGET_FID': 'int',
        'aquatic': 'float', # in config.yml
        'low_areas': 'float', # in config.yml
        'permafrost': 'float', # in config.yml
        'transportation': 'float', # in config.yml
        'wildlife': 'float', # in config.yml
        'hub_rnk': 'int', # in config.yml
        'exposure': 'float', # in config.yml
        'asset': 'float', # in config.yml
        'threat': 'float', # in config.yml
        'crit_infra': 'float', # in config.yml
        'crit_fac': 'float', # in config.yml
        'soc_vuln': 'float', # in config.yml
        'floodprone': 'float', # in config.yml
        'tsunami': 'float', # in config.yml
        'terrestri': 'float', # in config.yml
        'erosion': 'float', # in config.yml
      }
    }),
    'field_maps': {
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'pop_density': 'pop_dens',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'sea_level_rise': 'slr',
      'impermeable': 'impermeabl',
      'Rank': 'hub_rnk',
      'wave_exposure': 'wave_exp',
      'wave_flooding': 'wave_fld',
      'hub_id': 'TARGET_FID'
    }
  }



}
