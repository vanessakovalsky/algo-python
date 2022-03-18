capital =  100 + 100 * (5 / 100) 

annee = 0

annee_capital = {}

while capital <= 6300 :
    capital = capital + capital * (5/100)
    annee += 1
    annee_capital[annee] = capital

print(annee)