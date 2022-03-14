# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:35:21 2019

@author: Guillaume
"""

"""
Conjecture de Syracuse !

Introduction :
    
On appelle suite de Syracuse une suite d'entiers naturels définie de la
manière suivante : 
    On part d'un nombre entier plus grand que zéro :
    - s’il est pair, on le divise par 2
    - s’il est impair, on le multiplie par 3 et on ajoute 1.

La conjecture de Syracuse est l'hypothèse mathématique selon laquelle
la suite de Syracuse de n'importe quel entier strictement positif atteint 1.

But de l'exercice :

Le but de l'exercice est d'implémenter un programme qui part d'un nombre
donné par l'utilisateur et qui renvoie le nombre d'étapes pour atteindre 1
en utilisant la suite de Syracuse.

"""

#TODO