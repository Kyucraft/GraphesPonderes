from typing import TypeVar, Tuple

T = TypeVar('T')

class PriorityQueue:


    def __init__(self, taille: int, fill: T, ord: str):
        #ordre est soit croissant ('ASC'), soit décroissant ('DESC')
        assert ord in ['ASC', 'DESC']
        self.ord=ord
        self.fill = fill
    
    def est_vide(self)->bool:
        return len(self.fill) == 0
        
    def enfiler(self,val: Tuple[T,int])-> None:
        #Kiklou
        self.fill.append(val)   

    def defiler(self)->Tuple[T,int]:
        assert not(self.est_vide())
        self._maj_prio()
        defil_result = self.fill[0]
        self.fill.pop(0) 
        return (defil_result) 

    def maj_sommet(self,sommet,val):
        for i in self.fill:
            v,x = self.fill[i]
            if v==sommet:
                self.fill.append((sommet,val))
        pass
                
        
    def _maj_prio(self):
        #kliklou
        self.fill = sorted(self.fill)
        if self.ord == 'DESC':
            self.fill.reverse()
        #trie les elem enfilés en fonction de leur poids selon ord
     

f = PriorityQueue(10, [], 'ASC')
print(f.est_vide())
f.enfiler(('a', 5))
f.enfiler(('b', 3))
f.enfiler(('c', 1))


f = PriorityQueue(10, [], 'DESC')
f.enfiler(('a', 5))
f.enfiler(('b', 3))
f.enfiler(('c', 1))
