protected_areas.plot()


# Extra: plotten volgens type:
plt =MUMA.plot(column='category', legend = True, categorical = True)
# Extra: legend verplaatsen naar een geschiktere posities
leg = plt.get_legend() # Legend-item afzonderen naar een nieuwe variabele
leg.set_bbox_to_anchor((1.5, 0.2, 0.2, 0.2)) # attribuut niet de locatie kan wijzigen => prutsen