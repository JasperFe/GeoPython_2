# Nagaan welke districten het punt educatiecentrum bevatten
mask = districten.contains(educatiecentrum)

# Mask toepassen om enkel de districten met het centrum te weerhouden:
districten[mask]