capital =  100 + 100 * (5 / 100) 
liste_capital = [capital]

captial_augmente = capital + capital * (5/100)

liste_capital.append(captial_augmente)

capital_augmente2 = captial_augmente + captial_augmente * (5/100)

liste_capital.append(capital_augmente2)

print('Première année',liste_capital[0])
print('l\'année dernière',liste_capital[-2])
print('cette année',liste_capital[-1])