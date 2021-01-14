#PriorityQueue

```python
from typing import TypeVar, Tuple

T = TypeVar('T')

class PriorityQueue:
  '''
  une file d'elem (val, poids), un ordre (croissant ou décroissant)
  on défile le premier élément après rangement selon l'ordre sur les poids
  '''

  def __init__(self, taille: int, fill: T, ord: str):
      #ordre est soit croissant ('ASC'), soit décroissant ('DESC')
      assert ord in ['ASC', 'DESC']
      self.ord=ord
      if ord == 'ASC':
          self.fill = (fill,float('inf')) #plus grand que tout nombre
      else:
          self.fill = (fill,0)
      pass
  
  def est_vide(self)->bool:
      #kliklou
      if self.fill == ():
          return True
      return False
    
  def enfiler(self,val: Tuple[T,int])-> None:
      #kliklou
      self.fill += val[0],val[1]
      return None     

  def defiler(self)->Tuple[T,int]:
      #kliklou
      assert not(self.est_vide())
      n = self._maj_prio()
      defil_result = (self.fill[n-1] ,self.fill[n])
      self.fill = self.fill[:n-1]  + self.fill[n+1:]
      print(defil_result)
      return (defil_result) 
      
  def _maj_prio(self):
      #kliklou
      n = list(filter(lambda x:type(x)==float,self.fill))
      y = list(filter(lambda x:type(x)==int,self.fill))
      y.sort()
      if self.ord == 'ASC':
          for i in range(len(n)):
              y.append(n[i])
          print(y)
          return self.fill.index(min(y))
      else:
          y.reverse
          return self.fill.index(max(y))
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
