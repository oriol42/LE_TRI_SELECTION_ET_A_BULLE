tableau = [12,3,5,2,1,0,6,9,56,73,13,11]
taille_tableau = len(tableau) - 1
test = 1

while test == 1:
    test = 0
    for i in range(0,taille_tableau):
        if tableau[i] > tableau[i+1]:
            variable_temporel = tableau[i]
            tableau[i] = tableau[i+1]
            tableau[i+1] = variable_temporel
            test = 1
    taille_tableau = taille_tableau -1
print(tableau)