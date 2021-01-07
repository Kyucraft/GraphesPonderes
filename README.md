#PriorityQueue

```python
from typing import TypeVar, Tuple

T = TypeVar('T')

class PriorityQueue:
  '''
  une file d'elem (val, poids), un ordre (croissant ou décroissant)
  on défile le premier élément après rangement selon l'ordre sur les poids
  '''

  def __init__(self, taille: int, fill: Tuple(T,int), ord: str):
      #ordre est soit croissant ('ASC'), soit décroissant ('DESC')
      assert ord in ['ASC', 'DESC']
      if ord == 'ASC':
          self.fill = ("",float('inf')) #plus grand que tout nombre
      else:
          self.fill = ("",0)
      pass
  
  def est_vide(self)->bool:
      pass
    
  def enfiler(self,val: Tuple[T,int])-> None:
      pass
  
  def defiler(self)->Tuple[T,int]:
      assert not(self.est_vide())
      self._maj_prio()
      #renvoyer le premier eleme dans l'ordre (avec son poids !)
      
  def _maj_prio(self):
      #trie les elem enfilés en fonction de leur poids selon ord
     

f = PriorityQueue(10, "", 'ASC')
f.enfiler(('a', 5))
f.enfiler(('b', 3))
f.enfiler(('c', 1))
assert f.defiler() == ('c', 1)

f = PriorityQueue(10, "", 'DESC')
f.enfiler(('a', 5))
f.enfiler(('b', 3))
f.enfiler(('c', 1))
assert f.defiler() == ('a', 5)
```
