# GraphesPonderes

pour le codage de graphe pondéré, utiliser le codage suivant : 
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

