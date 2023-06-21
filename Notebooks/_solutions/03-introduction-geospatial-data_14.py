# nieuwe kolom berekenen met oppervlakte in km²
area_m2 = protected_areas.area
area_km2 = area_m2*10**-6
protected_areas['area_km2'] = area_km2

# Bovenstaande kan ook in één regel worden uitgevoerd:
protected_areas['area_km2'] = protected_areas.area*10**-6