from collections import OrderedDict

config = {
  'continental_us': {
    #'id': { 'in': 'NAME', 'out': 'areaName' },
    'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' },
    #'id': { 'in': 'STATEFP', 'out': 'STATEFP' },
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'areaName': 'str',
        'NAMELSAD': 'str', # counties
        'STATEFP': 'str', # states, counties
        #'COUNTYFP': 'str', # counties
        #'COUNTYNS': 'str', # counties
        #'AFFGEOID': 'str', # states, counties
        #'GEOID': 'int', # states, counties
        'STUSPS': 'str', # states, counties
        'STATE_NAME': 'str', # counties
        #'LSAD': 'int', # counties
        #'ALAND': 'int', # states, counties
        #'AWATER': 'int', # states, counties
        'hubs': 'float',
        'wildlife': 'float',
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
        'landcover_open_water': 'float',
        'landcover_perennial_icesnow': 'float',
        'landcover_developed_open_space': 'float',
        'landcover_developed_low_intensity': 'float',
        'landcover_developed_medium_intensity': 'float',
        'landcover_developed_high_intensity': 'float',
        'landcover_barren_land': 'float',
        'landcover_deciduous_forest': 'float',
        'landcover_evergreen_forest': 'float',
        'landcover_mixed_forest': 'float',
        'landcover_dwarf_scrub': 'float',
        'landcover_shrub_scrub': 'float',
        'landcover_grassland_herbaceous': 'float',
        'landcover_sedge_herbaceous': 'float',
        'landcover_lichens': 'float',
        'landcover_moss': 'float',
        'landcover_pasture_hay-areas': 'float',
        'landcover_cultivated_crops': 'float',
        'landcover_woody_wetlands': 'float',
        'landcover_emergent_herbaceous_wetlands': 'float'
      }
    }),
    'field_maps': {
      #'NAMELSAD': 'areaName', # counties
      #'NAME': 'areaName', # states
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
    #'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' },
    'id': { 'in': 'NAME', 'out': 'NAME' }, # states
    #'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'NAMELSAD': 'str', # counties
        'STATEFP': 'str', # states, counties
        'NAME' : 'str', # states, counties
        'STUSPS': 'str', # states, counties
        #'STATE_NAME': 'str', # counties
        #'TARGET_FID': 'int', # needed for hubs
        #'hub_rnk': 'int', # needed for hubs
        #'acres': 'float', # needed for hubs
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
        'wildlife': 'float',
        'landcover_background': 'float',
        'landcover_unclassified': 'float',
        'landcover_developed_high_intensity': 'float',
        'landcover_developed_medium_intensity': 'float',
        'landcover_developed_low_intensity': 'float',
        'landcover_developed_open space': 'float',
        'landcover_cultivated_crops': 'float',
        'landcover_pasture_hay': 'float',
        'landcover_grassland/herbaceous': 'float',
        'landcover_deciduous_forest': 'float',
        'landcover_evergreen_forest': 'float',
        'landcover_mixed_forest': 'float',
        'landcover_scrub_shrub': 'float',
        'landcover_palustrine_forested_wetland': 'float',
        'landcover_palustrine_scrub_shrub_wetland': 'float',
        'landcover_palustrine_emergent_wetland': 'float',
        'landcover_estuarine_forested_wetland': 'float',
        'landcover_estuarine_scrub/shrub_wetland': 'float',
        'landcover_estuarine_emergent_wetland': 'float',
        'landcover_unconsolidated_shore': 'float',
        'landcover_bare_land': 'float',
        'landcover_open_water': 'float',
        'landcover_palustrine_aquatic_bed': 'float',
        'landcover_estuarine_aquatic_bed': 'float',
        'landcover_tundra': 'float',
        'landcover_snow_ice': 'float',
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
      'geometry': ['Polygon', 'MultiPolygon'],
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
      'geometry': ['Polygon', 'MultiPolygon'],
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
    #'id': { 'in': 'TARGET_FID', 'out': 'TARGET_FID' }, # hubs 
    #'id': { 'in': 'NAME', 'out': 'NAME' }, # states 
    'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties 
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'TARGET_FID': 'int', # hubs
        'NAMELSAD': 'str', # states, counties
        'STATEFP': 'str', # states, counties
     #   'COUNTYFP': 'str', # counties
     #   'COUNTYNS': 'str', # counties
     #   'AFFGEOID': 'str', # states, counties
     #   'GEOID': 'int', # states, counties
        'NAME' : 'str', # counties
        'STUSPS': 'str', # states, counties
        'STATE_NAME': 'str', # counties
     #   'LSAD': 'int', # counties
     #   'ALAND': 'int', # states, counties
     #   'AWATER': 'int', # states, counties
        'wildlife': 'float',
        # 'hub_rnk': 'int', # hubs
        # 'acres': 'float', # hubs
        'hubs': 'float',
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
        'stormsurge': 'float',
        'landcover_background': 'float',
        'landcover_unclassified': 'float',
        'landcover_developed_high_intensity': 'float',
        'landcover_developed_medium_intensity': 'float',
        'landcover_developed_low_intensity': 'float',
        'landcover_developed_open space': 'float',
        'landcover_cultivated_crops': 'float',
        'landcover_pasture_hay': 'float',
        'landcover_grassland/herbaceous': 'float',
        'landcover_deciduous_forest': 'float',
        'landcover_evergreen_forest': 'float',
        'landcover_mixed_forest': 'float',
        'landcover_scrub_shrub': 'float',
        'landcover_palustrine_forested_wetland': 'float',
        'landcover_palustrine_scrub_shrub_wetland': 'float',
        'landcover_palustrine_emergent_wetland': 'float',
        'landcover_estuarine_forested_wetland': 'float',
        'landcover_estuarine_scrub/shrub_wetland': 'float',
        'landcover_estuarine_emergent_wetland': 'float',
        'landcover_unconsolidated_shore': 'float',
        'landcover_bare_land': 'float',
        'landcover_open_water': 'float',
        'landcover_palustrine_aquatic_bed': 'float',
        'landcover_estuarine_aquatic_bed': 'float',
        'landcover_tundra': 'float',
        'landcover_snow_ice': 'float',
        # 'land_nodat': 'float',
        # 'land_hi': 'float',
        # 'land_mi': 'float',
        # 'land_li': 'float',
        # 'land_os': 'float',
        # 'land_crop': 'float',
        # 'land_hay': 'float',
        # 'land_grass': 'float',
        # 'land_df': 'float',
        # 'land_ef': 'float',
        # 'land_mf': 'float',
        # 'land_scrub': 'float',
        # 'land_pfw': 'float',
        # 'land_pss': 'float',
        # 'land_pem': 'float',
        # 'land_efw': 'float',
        # 'land_ess': 'float',
        # 'land_eem': 'float',
        # 'land_shore': 'float',
        # 'land_bare': 'float',
        # 'land_ow': 'float',
        # 'land_pab': 'float',
        # 'land_eab': 'float',
        # 'land_tund': 'float',
        # 'land_snic': 'float'
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
      #'hub_rank': 'hub_rnk',
      #'NAMELSAD': 'areaName' # counties
      'NAME': 'areaName', # states
      # 'landcover_no_data': 'land_nodat',
      # 'landcover_developed_high_intensity': 'land_hi',
      # 'landcover_developed_medium_intensity': 'land_mi',
      # 'landcover_developed_low_intensity': 'land_li',
      # 'landcover_developed_open space': 'land_os',
      # 'landcover_cultivated_crops': 'land_crop',
      # 'landcover_pasture_hay': 'land_hay',
      # 'landcover_grassland/herbaceous': 'land_grass',
      # 'landcover_deciduous_forest': 'land_df',
      # 'landcover_evergreen_forest': 'land_ef',
      # 'landcover_mixed_forest': 'land_mf',
      # 'landcover_scrub_shrub': 'land_scrub',
      # 'landcover_palustrine_forested_wetland': 'land_pfw',
      # 'landcover_palustrine_scrub_shrub_wetland': 'land_pss',
      # 'landcover_palustrine_emergent_wetland': 'land_pem',
      # 'landcover_estuarine_forested_wetland': 'land_efw',
      # 'landcover_estuarine_scrub/shrub_wetland': 'land_ess',
      # 'landcover_estuarine_emergent_wetland': 'land_eem',
      # 'landcover_unconsolidated_shore': 'land_shore',
      # 'landcover_bare_land': 'land_bare',
      # 'landcover_open_water': 'land_ow',
      # 'landcover_palustrine_aquatic_bed': 'land_pab',
      # 'landcover_estuarine_aquatic_bed': 'land_eab',
      # 'landcover_tundra': 'land_tund',
      # 'landcover_snow_ice': 'land_snic'

    }
  },

  'american_samoa': {
    'id': { 'in': 'TARGET_FID', 'out': 'TARGET_FID' },
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
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
      'geometry': ['Polygon', 'MultiPolygon'],
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
    #'id': { 'in': 'NAME', 'out': 'areaName' }, # states
    #'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    'id': { 'in': 'Id', 'out': 'Id' }, # dissolved assessment 
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'NAMELSAD': 'str', # states, counties
        #'STATEFP': 'str', # states, counties
        #'COUNTYFP': 'str', # counties
        #'COUNTYNS': 'str', # counties
        #'AFFGEOID': 'str', # states, counties
        #'GEOID': 'int', # states, counties
        #'NAME' : 'str',
        #'STUSPS': 'str', # states, counties
        #'STATE_NAME': 'str', # counties
        #'LSAD': 'int', # counties
        #'ALAND': 'int', # states, counties
        #'AWATER': 'int', # states, counties
        'aquatic': 'float', 
        'low_areas': 'float',
        'permafrst': 'float', 
        'trsnpoton': 'float',
        'wildlife': 'float',
        'hubs': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'soc_vuln': 'float',
        'floodprone': 'float',
        'tsunami': 'float',
        'terrestri': 'float',
        'erosion': 'float',
        'landcover_open_water': 'float',
        'landcover_perennial_icesnow': 'float',
        'landcover_developed_open_space': 'float',
        'landcover_developed_low_intensity': 'float',
        'landcover_developed_medium_intensity': 'float',
        'landcover_developed_high_intensity': 'float',
        'landcover_barren_land': 'float',
        'landcover_deciduous_forest': 'float',
        'landcover_evergreen_forest': 'float',
        'landcover_mixed_forest': 'float',
        'landcover_dwarf_scrub': 'float',
        'landcover_shrub_scrub': 'float',
        'landcover_grassland_herbaceous': 'float',
        'landcover_sedge_herbaceous': 'float',
        'landcover_lichens': 'float',
        'landcover_moss': 'float',
        'landcover_pasture_hay-areas': 'float',
        'landcover_cultivated_crops': 'float',
        'landcover_woody_wetlands': 'float',
        'landcover_emergent_herbaceous_wetlands': 'float'
      }
    }),
    'field_maps': {
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'rank': 'hub_rnk',
      'permafrost': 'permafrst',
      'transportation': 'trsnpoton',
    }
  },
  'great_lakes': {
    'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    #'id': { 'in': 'NAME', 'out': 'NAME' }, # states
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        'NAMELSAD': 'str', # states, counties
        'STATEFP': 'str', # states, counties
        #'COUNTYFP': 'str', # counties
        #'COUNTYNS': 'str', # counties
        #'AFFGEOID': 'str', # states, counties
        #'GEOID': 'int', # states, counties
        #'NAME' : 'str', # counties
        'STUSPS': 'str', # states, counties
        #'STATE_NAME': 'str', # counties
        #'LSAD': 'int', # counties
        #'ALAND': 'int', # states, counties
        #'AWATER': 'int', # states, counties
        'aquatic': 'float',
        'wildlife': 'float',
        'hubs': 'float',
        'exposure': 'float',
        'asset': 'float',
        'threat': 'float',
        'crit_infra': 'float',
        'crit_fac': 'float',
        'soc_vuln': 'float',
        'floodprone': 'float',
        'terrestri': 'float',
        'slope': 'float',
        'erosion': 'float',
        'highwater': 'float', 
        'impermeabl': 'float',
        'pop_dens': 'float',
        'landcover_open_water': 'float',
        'landcover_perennial_icesnow': 'float',
        'landcover_developed_open_space': 'float',
        'landcover_developed_low_intensity': 'float',
        'landcover_developed_medium_intensity': 'float',
        'landcover_developed_high_intensity': 'float',
        'landcover_barren_land': 'float',
        'landcover_deciduous_forest': 'float',
        'landcover_evergreen_forest': 'float',
        'landcover_mixed_forest': 'float',
        'landcover_dwarf_scrub': 'float',
        'landcover_shrub_scrub': 'float',
        'landcover_grassland_herbaceous': 'float',
        'landcover_sedge_herbaceous': 'float',
        'landcover_lichens': 'float',
        'landcover_moss': 'float',
        'landcover_pasture_hay-areas': 'float',
        'landcover_cultivated_crops': 'float',
        'landcover_woody_wetlands': 'float',
        'landcover_emergent_herbaceous_wetlands': 'float',
      }
    }),
    'field_maps': {
      'terrestrial': 'terrestri',
      'crit_facilities': 'crit_fac',
      'social_vuln': 'soc_vuln',
      'floodprone_areas': 'floodprone',
      'rank_val': 'hub_rnk',
      'impermeable': 'impermeabl',
      'pop_density': 'pop_dens',
    }
  }



}
