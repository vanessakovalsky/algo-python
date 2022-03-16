# (1+2)**3 # 27 
# "Da" * 4 # "DaDaDaDa"
# #"Da" + 3 # Erreur : on ne peut pas ajouter un nombre et une chaine de caractère 
# ("Pa"+"La") * 2 # "PaLaPaLa" Concaténation 
# #("Da"*4) / 2 # Erreur : pas de division ou de soustraction sur une chaine de caractère
# 5 / 2 # 2.5
# 5 // 2 # Division entière : 2
# 5 % 2 # Modulo (combien de fois je peux mettre le deuxième élement dans le premier). Il m'affiche ce qu'il reste


# str(4) * int("3") # --> "4" * 3 => 444
# int("3") + float("3.2") # 3 + 3.2 = 6.2
# str(3) * float("3.2") # Erreur : je ne peux multiplier une chaine que avec un entier
# str(3/4) * 2 # -> "0.75"*2 = "0.750.75"


capital =  100 + 100 * (5 / 100) 
print (capital) # 105
captial_augmente = capital + capital * (5/100)
print(captial_augmente) # 110.25
chaine_captial_augmente = str(captial_augmente)
print(chaine_captial_augmente) # 110.25
print(str(captial_augmente)) # 110.25

print(type(captial_augmente))
print(type(chaine_captial_augmente))


message = "Au bout de deux ans le capital sera de " + captial_augmente
print(message)