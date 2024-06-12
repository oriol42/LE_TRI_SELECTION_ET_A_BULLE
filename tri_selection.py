tableau = [12,3,5,2,1,0,6,9,56,73,13,11]
taille_tableau = len(tableau) -1

for i in range(0,taille_tableau):
    minimum = i
    for j in range(i+1, taille_tableau + 1):
       if tableau[minimum] > tableau[j]:
           minimum = j
                
    variable_temporel = tableau[i]
    tableau[i] = tableau[minimum]
    tableau[minimum] = variable_temporel
print(tableau)