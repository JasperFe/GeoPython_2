# Mask  aanmaken
mask = countries['continent'] == 'Oceania'

# subset aanmaken
countries_oceania = countries[mask]

# Of in één stap:
countries_oceania = countries[countries['continent'] == 'Oceania']