# GraphesPonderes

pour le codage de graphe pondéré, utiliser le codage suivant : 
(version graphe orienté pour faire simple)
```python
arete={'a':{'b':2, 'c':7}, 'b':{'c':3}, 'c':{}}
```


Pour vos tests, chaque membr du groupe doit : 
1/ concevoir un graphe pondéré sur le papier (au minimum 10 sommets)
2/ à faire en groupe : faire tourner l'algorithme vu en classe à la main sur ce graphe (filmer la trace d'exécution
3/ en déduire les dictionnaires `distance`, `parent` et l'arbre de parcours `arbre` calculées à la main, qui vont servir de vérification pour l'algo
4/ coder `arbre` avec la classe `Tree`
5/ coder ce graphe selon la syntaxe ci-dessus, c'est-à-dire écrire le dictionnaire décrivant les arêtes les sommets
6/rédiger le test
```python
#fichier test.py

from integration import *
from graphe_pondere import *
from tree import *

#test 1
#codage de arbre (réponse calculée à la main) 
#codage
g1 = GraphePondere(a1)
assert parcours_largeur(a1, s1) == (distance, parent, arbre)


#test 2
#codage de arbre (réponse calculée à la main) 
#codage
g1 = GraphePondere(a1)
assert parcours_largeur(a1, s1) == (distance, parent, arbre)


#test 3
#codage de arbre (réponse calculée à la main) 
#codage
g1 = GraphePondere(a1)
assert parcours_largeur(a1, s1) == (distance, parent, arbre)
```
