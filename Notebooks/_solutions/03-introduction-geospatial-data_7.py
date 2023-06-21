import contextily

# Plot opstellen met de gewenste eigenschappen
ax = plotdata.plot(figsize=(12,6), markersize=5)

# Extra: wijzig de y-as: groter maken adhv ax.set(ylim = ...)
ax.set(ylim = (635000, 680000))

# uit het contextily pakket halen we de add_basemap() functie
contextily.add_basemap(ax)
