
#Optie 1
for el in range(1,100,2):
    print(el)
    
# Optie 2:
for el in range(1,100):
    if (el%2) !=0: #% = the remainder operator
        print(el)
    else:
        continue