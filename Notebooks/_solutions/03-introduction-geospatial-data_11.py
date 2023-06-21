# Inlezen van de protected areas
protected_areas = geopandas.read_file('data/protected_areas.shp')

# Bekijken van eerste rijen
protected_areas.head()