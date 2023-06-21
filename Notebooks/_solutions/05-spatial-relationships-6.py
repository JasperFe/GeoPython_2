# Mangrove plots met een afstand < 10 km
plots_centrum = plotdata.loc[dist_centrum<10000]

# We kunnen de afstand ook toevoegen aan de plotdata:
plotdata['dist_centrum'] = dist_centrum

#Resultaat: de plotjes van Sampling Unit 4 liggen het dichtst bij.
print(plots_centrum)