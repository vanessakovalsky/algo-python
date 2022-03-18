def rentabilite(capital, taux, somme): 
    capital +=  capital * (taux / 100) 
    annee = 0

    annee_capital = {}

    while capital <= somme :
        capital = capital + capital * (taux/100)
        annee += 1
        annee_capital[annee] = capital

    return annee_capital

print(rentabilite(2000,10,6000))