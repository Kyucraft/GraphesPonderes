# GraphesPonderes

pour définir un graphe pondéré, on lui passe le dictionnaire des voisins de chaque sommet, en précisant à chaque fois la longueur de l'arête. Dans ce projet, on utilisera la convention suivante 
(version graphe orienté pour faire simple)
```python
arete={'a':{'b':2, 'c':7}, 'b':{'c':3}, 'c':{}}
```
Du coup pour savoir la longueur d'une arête, si elle existe :

`arete[s][t]`.

On peut imaginer une méthode 
```python
def longueur_arete(self,s,t):
  '''
  renvoie la longueur de l'aréte entre deux sommets s et t du graphe
  Exception KeyError levée si il n'y a pas d'arête.
  à utiliser avec un try:... except KeyError:...
  '''
  assert self.contient(s)
  assert self.contient(t)
  return self.arete[s][t]
```

Attention : quand un sommet n'a pas de voisin accessible (possible en particulier dans un graphe orienté), on doit qd même rajouter son étiquette dans le dictionnaire `arete` avec comme valeur le dict vide, comme c le cas pour `c` dans l'exemple.
