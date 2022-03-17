a = 12
b = 42
c = a * b / a # Définit la Variable qui s'appelle c 

print(c) # Utilisation de la fonction print avec l'argument c (la variable que l'on a définit avant) 

chaine_de_caractere = 'Ceci est une donnees d\'un type chaines de caractère'

# Manipulation de Liste

x_men = ['Volverine','tornade','mystique','phoenix','quicksilver']
print(x_men[1])# Affiche l'élément à la position 1 de la liste /!\ commence à la position 0 
print(x_men[1:3]) # Affiche les éléments à partir de 1 et jusqu'à 3 (exclus)
print(x_men[-1]) # Affiche le premier élément de la liste en partant de la fin

x_men.append('hulk') # Ajoute à la fin de la liste 'hulk'
x_men.insert(2,'toto') # Ajoute à la position 2, la valeur toto
print(x_men)
x_men2 = x_men # Crée un alias de liste (/!\ on pointe sur les mêmes données)
print(x_men2)
x_men2.append('batman')
print(x_men2)
print(x_men)
x_men3 = x_men.copy() # Duplique la liste
print(x_men3)
x_men3.append('Joker')
print(x_men3)
print(x_men)

print(x_men.count('batman')) # Compte le nombre de fois où le mot 'batman' est présent dans la liste
x_men.extend(['xm1','xm2','xm3']) # Ajoute à la fin de la liste les nouveaux éléments
print(x_men)
id = x_men.index('Volverine') # Renvoit la première position ou l'élément Volverine est trouvé
print(id)
x_men.pop(2) # Supprime l'élément à la position 2
print(x_men)
x_men.remove('xm2') # Supprime l'élément ayant pour valeur 'xm2'
print(x_men)