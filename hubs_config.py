from collections import OrderedDict

# comment things in/out as needed for hubs/states/counties/huc8
# need to output as geojson for all of the landcover fields 
config = {
  'continental_us': {
    #'id': { 'in': 'TARGET_FID', 'out': 'TARGET_FID' }, # hubs
    #'id': { 'in': 'NAME', 'out': 'NAME' }, # states
    #'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    #'id': { 'in': 'huc8', 'out': 'huc8' }, # huc8
    'id': { 'in': 'STATEFP', 'out': 'STATEFP' }, # ALL I HAVE FOR IAN BOUNDARIES FOR STATE
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'TARGET_FID': 'int', # hubs
        #'hub_rnk': 'int', # hubs
        #'acres': 'float', # hubs
        #'NAMELSAD': 'str', #  counties
        'STATEFP': 'str', # states, counties - ALL I HAVE FOR IAN BOUNDARIES FOR STATE
        #'COUNTYFP': 'str', # counties
        #'COUNTYNS': 'str', # counties
        #'AFFGEOID': 'str', # states, counties
        #'GEOID': 'int', # states, counties
        #'NAME' : 'str', # states, counties
        #'STUSPS': 'str', # states, counties
        #'STATE_NAME': 'str', # counties
        #'LSAD': 'int', # counties
        #'huc8': 'str', # huc8
        #'name': 'str', # huc8
        'hubs': 'float', # maybe only for states, counties, huc8
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
    #'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' }, # hubs
    #'id': { 'in': 'NAME', 'out': 'NAME' }, # states
    #'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    'id': { 'in': 'huc8', 'out': 'huc8' }, # huc8
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'TARGET_FID': 'int', # hubs
        #'hub_rnk': 'int', # hubs
        #'acres': 'float', # hubs
        #'NAMELSAD': 'str', #  counties
        #'STATEFP': 'str', # states, counties - ALL I HAVE FOR IAN BOUNDARIES FOR STATE
        #'COUNTYFP': 'str', # counties
        #'COUNTYNS': 'str', # counties
        #'AFFGEOID': 'str', # states, counties
        #'GEOID': 'int', # states, counties
        #'NAME' : 'str', # states, counties
        #'STUSPS': 'str', # states, counties
        #'STATE_NAME': 'str', # counties
        #'LSAD': 'int', # counties
        'huc8': 'str', # huc8
        'name': 'str', # huc8
        'hubs': 'float', # maybe only for states, counties, huc8
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
    #'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' }, # hubs
    #'id': { 'in': 'NAME', 'out': 'NAME' }, # states
    #'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    'id': { 'in': 'huc8', 'out': 'huc8' }, # huc8
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'TARGET_FID': 'int', # hubs
        #'hub_rnk': 'int', # hubs
        #'acres': 'float', # hubs
        #'NAMELSAD': 'str', #  counties
        #'STATEFP': 'str', # states, counties - ALL I HAVE FOR IAN BOUNDARIES FOR STATE
        #'COUNTYFP': 'str', # counties
        #'COUNTYNS': 'str', # counties
        #'AFFGEOID': 'str', # states, counties
        #'GEOID': 'int', # states, counties
        #'NAME' : 'str', # states, counties
        #'STUSPS': 'str', # states, counties
        #'STATE_NAME': 'str', # counties
        #'LSAD': 'int', # counties
        'huc8': 'str', # huc8
        'name': 'str', # huc8
        'hubs': 'float', # maybe only for states, counties, huc8
        'wildlife': 'float',
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
        'tsunami': 'float',
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
        'landcover_snow_ice': 'float'
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
    #'id': { 'in': 'OBJECTID', 'out': 'TARGET_FID' }, # hubs
    #'id': { 'in': 'NAME', 'out': 'NAME' }, # states
    'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    #'id': { 'in': 'huc8', 'out': 'huc8' }, # huc8
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'TARGET_FID': 'int', # hubs
        #'hub_rnk': 'int', # hubs
        #'acres': 'float', # hubs
        'NAMELSAD': 'str', #  counties
        'STATEFP': 'str', # states, counties - ALL I HAVE FOR IAN BOUNDARIES FOR STATE
        'COUNTYFP': 'str', # counties
        'COUNTYNS': 'str', # counties
        'AFFGEOID': 'str', # states, counties
        'GEOID': 'int', # states, counties
        'NAME' : 'str', # states, counties
        'STUSPS': 'str', # states, counties
        'STATE_NAME': 'str', # counties
        'LSAD': 'int', # counties
        #'huc8': 'str', # huc8
        #'name': 'str', # huc8
        'hubs': 'float', # maybe only for states, counties, huc8
        'wildlife': 'float',
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
        'wave_flood': 'float',
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
        'landcover_snow_ice': 'float'
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

  # comment things in/out as needed for hubs/states/counties/huc8
  # need to output as geojson for all of the landcover fields
  'hawaii': {
    #'id': { 'in': 'TARGET_FID', 'out': 'TARGET_FID' }, # hubs
    'id': { 'in': 'NAME', 'out': 'NAME' }, # states
    #'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    #'id': { 'in': 'huc8', 'out': 'huc8' }, # huc8
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'TARGET_FID': 'int', # hubs
        #'hub_rnk': 'int', # hubs
        #'acres': 'float', # hubs
        #'NAMELSAD': 'str', #  counties
        'STATEFP': 'str', # states, counties - ALL I HAVE FOR IAN BOUNDARIES FOR STATE
        #'COUNTYFP': 'str', # counties
        #'COUNTYNS': 'str', # counties
        'AFFGEOID': 'str', # states, counties
        'GEOID': 'int', # states, counties
        'NAME' : 'str', # states, counties
        'STUSPS': 'str', # states, counties
        #'STATE_NAME': 'str', # counties
        #'LSAD': 'int', # counties
        #'huc8': 'str', # huc8
        #'name': 'str', # huc8
        'hubs': 'float', # maybe only for states, counties, huc8
        'wildlife': 'float',
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
        'landcover_snow_ice': 'float'
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
      #'hub_rank': 'hub_rnk', # hubs
    }
  },

  # comment things in/out as needed for hubs/states/counties/huc8
  # need to output as geojson for all of the landcover fields
  'american_samoa': {
    #'id': { 'in': 'TARGET_FID', 'out': 'TARGET_FID' },
    'id': { 'in': 'NAME', 'out': 'NAME' }, # states
    #'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    #'id': { 'in': 'huc8', 'out': 'huc8' }, # huc8
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'TARGET_FID': 'int',
        #'acres': 'float',
        #'hub_rnk': 'int',
        #'core_type': 'str',
        #'NAMELSAD': 'str', #  counties
        'STATEFP': 'str', # states, counties - ALL I HAVE FOR IAN BOUNDARIES FOR STATE
        #'COUNTYFP': 'str', # counties
        #'COUNTYNS': 'str', # counties
        'AFFGEOID': 'str', # states, counties
        'GEOID': 'int', # states, counties
        'NAME' : 'str', # states, counties
        'STUSPS': 'str', # states, counties
        #'STATE_NAME': 'str', # counties
        #'LSAD': 'int', # counties
        #'huc8': 'str', # huc8
        #'name': 'str', # huc8
        'hubs': 'float', # maybe only for states, counties, huc8
        'wildlife': 'float',
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
        'erosion': 'float',
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
        'landcover_snow_ice': 'float'
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
    #'id': { 'in': 'TARGET_FID', 'out': 'TARGET_FID' },
    #'id': { 'in': 'NAME', 'out': 'NAME' }, # states
    'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    #'id': { 'in': 'huc8', 'out': 'huc8' }, # huc8
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'TARGET_FID': 'int',
        #'acres': 'float',
        #'hub_rnk': 'int',
        #'core_type': 'str',
        'NAMELSAD': 'str', #  counties
        'STATEFP': 'str', # states, counties - ALL I HAVE FOR IAN BOUNDARIES FOR STATE
        'COUNTYFP': 'str', # counties
        'COUNTYNS': 'str', # counties
        'AFFGEOID': 'str', # states, counties
        'GEOID': 'int', # states, counties
        'NAME' : 'str', # states, counties
        'STUSPS': 'str', # states, counties
        'STATE_NAME': 'str', # counties
        'LSAD': 'int', # counties
        #'huc8': 'str', # huc8
        #'name': 'str', # huc8
        'hubs': 'float', # maybe only for states, counties, huc8
        'wildlife': 'float',
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
        'landcover_snow_ice': 'float'
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
   # comment things in/out as needed for hubs/states/counties/huc8
  # need to output as geojson for all of the landcover fields
  'alaska': {
    #'id': { 'in': 'Id', 'out': 'Id' }, # hubs
    'id': { 'in': 'NAME', 'out': 'NAME' }, # states
    #'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    #'id': { 'in': 'huc8', 'out': 'huc8' }, # huc8
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'NAMELSAD': 'str', #  counties
        'STATEFP': 'str', # states, counties - ALL I HAVE FOR IAN BOUNDARIES FOR STATE
        #'COUNTYFP': 'str', # counties
        #'COUNTYNS': 'str', # counties
        #'AFFGEOID': 'str', # states, counties
        'GEOID': 'int', # states, counties
        'NAME' : 'str', # states, counties
        'STUSPS': 'str', # states, counties
        #'STATE_NAME': 'str', # counties
        #'LSAD': 'int', # counties
        #'huc8': 'str', # huc8
        #'name': 'str', # huc8
        'aquatic': 'float', 
        # 'low_areas': 'float',
        # 'permafrst': 'float', 
        # 'trsnpoton': 'float',
        # 'wildlife': 'float',
        # 'hubs': 'float',
        # 'exposure': 'float',
        # 'asset': 'float',
        # 'threat': 'float',
        # 'crit_infra': 'float',
        # 'crit_fac': 'float',
        # 'soc_vuln': 'float',
        # 'floodprone': 'float',
        # 'tsunami': 'float',
        # 'terrestri': 'float',
        # 'erosion': 'float',
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
    #'id': { 'in': 'hub_id', 'out': 'TARGET_FID' }, # hubs
    #'id': { 'in': 'NAME', 'out': 'NAME' }, # states
    #'id': { 'in': 'NAMELSAD', 'out': 'NAMELSAD' }, # counties
    'id': { 'in': 'huc8', 'out': 'huc8' }, # huc8
    #'id': { 'in': 'STATEFP', 'out': 'STATEFP' }, # ALL I HAVE FOR IAN BOUNDARIES FOR STATE
    'schema': OrderedDict({
      'geometry': ['Polygon', 'MultiPolygon'],
      'properties': {
        #'TARGET_FID': 'int', # hubs
        #'NAMELSAD': 'str', #  counties
        #'STATEFP': 'str', # states, counties - ALL I HAVE FOR IAN BOUNDARIES FOR STATE
        #'COUNTYFP': 'str', # counties
        #'COUNTYNS': 'str', # counties
        #'AFFGEOID': 'str', # states, counties
        #'GEOID': 'int', # states, counties
        #'NAME' : 'str', # states, counties
        #'STUSPS': 'str', # states, counties
        #'STATE_NAME': 'str', # counties
        #'LSAD': 'int', # counties
        'huc8': 'str', # huc8
        'name': 'str', # huc8
        'hubs': 'float',
        'aquatic': 'float',
        'wildlife': 'float',
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
      'hub_id': 'TARGET_FID'
    }
  }



}
