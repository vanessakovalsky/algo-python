# Exercice 4 - Test et boucle

## Objectifs 
* Etre capable de mettre en place des tests selon différentes conditions
* Ecrire et utiliser des boucles pour parcourir des listes  

## Tester des conditions 
* Écrire un programme min_max.py, qui demande de saisir 2 valeurs et qui affiche la plus petite des 2 valeurs
* Écrire un script longeur_chaine.py, qui demande de saisir 2 chaînes de caractères et qui affiche la plus grande des 2 chaînes (celle qui a le plus de caractères)
* Ecrire le script convertir.py, qui effectue une conversion euros en dollars.
    * Le programme commencera par demander à l’utilisateur d’indiquer par un caractère ’E’ ou ’$’la devise du montant qu’il va entrer.
    * Puis le programme exécutera une action conditionnelle de la forme 
    ```python
    if devise== 'E' :
        ....
    elif devise== '$' :
        ....
    else:
        .......... #affichage d'un message d'erreur
    ```

## Boucler sur différentes données
* Écrire un programme, qui affiche 42 fois ”Je dois refaire les exercices” à l’aide de l’instruction for.
* Avec l'instruction while, on va compléter les paroles d'une chanson :
    * La séquence d’instructions permet d'afficher un message
    ```python
    n=10
    print("C'est dans % d ans je m'en irai j'entends le loup le renard chanter" %n)
    ```
    * On souhaite à l'aide d'une boucle afficher la même instruction jusqu'à ce que la valeur de la variable n soit à 0.
    * Attention à adapter la phrase (singulier / pluriel) sur la valeur 1   


## [Programme rentabilité] Ajouter le test et la boucle sur notre programme
* Dans le programme de rentabilité, ajouter un test pour vérifier si le montant souhaité est atteint
* Ajouter également une boucle pour afficher le montant associé à chaque année
