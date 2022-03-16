# Exercice 2 - Installation de Python et premier pas

Cet exercice a pour objectifs : 
* de vous faire installer votre environnement de travail
* de vous faire écrire et exécuter vos premiers programmes Pythons

## Installation
* Suivre les recommandations d'installation pour installer l'environnement Python : https://wiki.python.org/moin/BeginnersGuide/Download 
* Installer un editeur de code : 
    * Certains sont spécialisés comme
        * PyDev (https://www.pydev.org/ )
        * PyCharm (https://www.jetbrains.com/pycharm/ )
    * D’autres sont plus léger comme
        * Visual Studio Code (https://code.visualstudio.com/ ),
        * Atom (https://atom.io/ )
        * Sublime text (http://www.sublimetext.com/ )
* Nous utiliserons VisualStudioCode et les extensions : Python, Python for VSCode et Visual Studio IntelliCode

### Installation sur les VM de formation

 (mot de passe demandé le même que pour se connecter sur la VM)

* Installation de firefox : 
    * Ouvrir l'application Terminal 
```
sudo apt update -y 

sudo apt install -y firefox
```

* Installation de Visual Studio Code 
    * Ouvrir firefox et aller sur https://code.visualstudio.com/download cliquer sur le bouton .deb
    * Ouvrir le terminal de nouveau 
```
cd Downloads

sudo dpkg -i code_1.65.2-1646927742_amd64.deb  
```
    * Dans les applications de la Vm vous avez maintenant accès à visual Studio Code 

## Premier pas

* Lancer votre environnement et utiliser l'intérpréteur de python (commande : `python`) 

* Voici une série d'opération, essayer de trouver le résultat de chaque avant de vérifier le résultat dans l'intérpréteur de Python : 
    * (1+2)**3
    * "Da" * 4
    * "Da" + 3
    * ("Pa"+"La") * 2
    * ("Da"*4) / 2
    * 5 / 2
    * 5 // 2
    * 5 % 2

* Bien, nous passons maintenant à des opérations sur les types de données, même chose, quelle est le résultat de chacune des instructions suivantes (vérifier ensuite dans l'intérpréteur )
    * str(4) * int("3")
    * int("3") + float("3.2")
    * str(3) * float("3.2")
    * str(3/4) * 2

## Calcul pour notre exemple

* Stocker dans une variable nommée capital le résultat du calcul ` 100 + 100 × (5 / 100)`
* Ajouter 5% à ce résultat
* Transformer le résultat en chaine de caractère et afficher le 