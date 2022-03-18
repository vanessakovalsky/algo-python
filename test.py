
# On crée une fonction qui permet de demander le nom et de l'afficher
from unittest import result


def demanderLeNom():
    nom = input('Quel est votre nom ?')
    print(nom)


def demanderUneInformation(quelInfo):
    if type(quelInfo) == str:
        message = 'Quel est ' + quelInfo
    else : 
        message = 'Quel est ' + str(quelInfo)
    parametre = input(message)
    return parametre, message

# resultat_42 = demanderUneInformation("la vie ?")
# print('la question est', resultat_42[1])
# print("la reponse est",resultat_42[0])

# demanderUneInformation('l heure de fin de la formation ?')

def calculPerimetre(rayon):
    pi = 3.14
    diametre = rayon * 2
    perimetre = diametre * pi
    return perimetre, diametre

resultats = calculPerimetre(5)

print('le diametre est de ', resultats[1])
print('le perimetre est de ',resultats[0])