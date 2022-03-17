# # a = 12
# # b = 42
# # c = a * b / a # Définit la Variable qui s'appelle c 

# # print(c) # Utilisation de la fonction print avec l'argument c (la variable que l'on a définit avant) 

# # chaine_de_caractere = 'Ceci est une donnees d\'un type chaines de caractère'

# # # Manipulation de Liste

x_men = ['Volverine','tornade','mystique','phoenix','quicksilver']
# # print(x_men[1])# Affiche l'élément à la position 1 de la liste /!\ commence à la position 0 
# # print(x_men[1:3]) # Affiche les éléments à partir de 1 et jusqu'à 3 (exclus)
# # print(x_men[-1]) # Affiche le premier élément de la liste en partant de la fin

# # x_men.append('hulk') # Ajoute à la fin de la liste 'hulk'
# # x_men.insert(2,'toto') # Ajoute à la position 2, la valeur toto
# # print(x_men)
# # x_men2 = x_men # Crée un alias de liste (/!\ on pointe sur les mêmes données)
# # print(x_men2)
# # x_men2.append('batman')
# # print(x_men2)
# # print(x_men)
# # x_men3 = x_men.copy() # Duplique la liste
# # print(x_men3)
# # x_men3.append('Joker')
# # print(x_men3)
# # print(x_men)

# # print(x_men.count('batman')) # Compte le nombre de fois où le mot 'batman' est présent dans la liste
# # x_men.extend(['xm1','xm2','xm3']) # Ajoute à la fin de la liste les nouveaux éléments
# # print(x_men)
# # id = x_men.index('Volverine') # Renvoit la première position ou l'élément Volverine est trouvé
# # print(id)
# # x_men.pop(2) # Supprime l'élément à la position 2
# # print(x_men)
# # x_men.remove('xm2') # Supprime l'élément ayant pour valeur 'xm2'
# # print(x_men)

# ## Manipulation des tuples

# mon_tuple = ('chaussette', 'tee-shirt','pantalon','sous-vetements','pull')
# # print (mon_tuple[1:])
# # # mon_tuple.append('chapeau')   
# # print(mon_tuple.count('pull'))
# # print(mon_tuple.index('chaussette'))

# ## Manipulation des dictionnaires

# mon_dictionnaire = {"nom":'David','prenom':'Vanessa','departement':"06"}

# cles = ('nom','prenom','departement')
# valeurs = 0

# nouveau_dictionnaire = dict.fromkeys(cles,valeurs)
# print(nouveau_dictionnaire)

# print(mon_dictionnaire['nom'])
# print(mon_dictionnaire.get('nom'))

# print(mon_dictionnaire.items())

# print(mon_dictionnaire.keys())
# print(mon_dictionnaire.values())


# mon_dictionnaire.pop('departement')
# print(mon_dictionnaire)

# mon_dictionnaire['test'] = "une super valeur qui vaut 42"
# print(mon_dictionnaire)
# mon_dictionnaire.popitem()
# print(mon_dictionnaire)

# mon_dictionnaire['nouvelle_cla'] = 'gfshgksfhg ifshqgkjhqi'
# mon_dictionnaire.setdefault('newkey','test valeur')
# print(mon_dictionnaire)
# print(mon_dictionnaire.setdefault('newkey'))
# print(mon_dictionnaire)

# mon_dictionnaire.update({'newkey':'nouvelle valeur','nom':'toto'})
# print(mon_dictionnaire)
# mon_dictionnaire['newkey'] =  'troisieme valeur'
# print(mon_dictionnaire)

## Tester sur une condition

# numero1 = 8798456
# numero2 = 87984564564

# if numero1 == numero2 :
#     print('Numero 1 est supérieur à numéro 2')
#     print('Numero 1 ', numero1)
#     print('numero 2', numero2)
# elif numero1 >= numero2 :
#     print('condition numéro 2 vrai')
# else :
#     print('Numéro 2 supérieur à numéro 1')
#     print('Numero 1 ', numero1)
#     print('numero 2', numero2)


## Boucles 

print(x_men)

for personnage in  x_men:
    print('Le xmen est ', personnage)
    print('La taille de son nom est ', len(personnage))

compteur = 0 # Ne pas nommer un compteur i 
while compteur < 2 :
    print('valeur du compteur avant incrementation = ', compteur)
    compteur = compteur + 1 # compteur += 1 
    print('valeur du compteur apres incrementation = ', compteur)

print('apres la boucle') 

