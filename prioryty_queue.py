from typing import TypeVar, Tuple

T = TypeVar('T')

class PriorityQueue:


    def __init__(self, taille: int, fill: T, ord: str):
        '''
        ord = ordre
        Soit ASC = ascendant
        Soit DESC = descendant
        '''
        assert ord in ['ASC', 'DESC']
        self.ord=ord
        self.fill = fill
    
    def est_vide(self)->bool:
        '''
        Savoir si la queue est vide
        '''
        return len(self.fill) == 0
        
    def enfiler(self,val: Tuple[T,int])-> None:
        '''
        rajoute a la fin de la queues le val
        '''
        self.fill.append(val)   

    def defiler(self)->Tuple[T,int]:
        '''
        Sert a defiler la valeur la plus petite si la file est en ascendant
        Sert a defiler la valeur la plus grande si la file est en descendant
        En sachant que la valeur est a la place 0
        '''
        assert not(self.est_vide())
        self._maj_prio()
        defil_result = self.fill[0]
        self.fill.pop(0) 
        return (defil_result) 


    def maj_sommet(self,sommet,val):
        '''
        Sert a rajouter une nouvelle valeur dans la queue
        '''
        for i in self.fill:
            v,x = self.fill[i]
            if v==sommet:
                self.fill.append((sommet,val))
        pass


        #création d'un dictionnaire correspondant au contenu de self.fill, puis
        #modification du dico et recréation en liste
                
        
    def _maj_prio(self):
        '''
        trie les elements de la queues en fonction de leurs poids selon l'ordre
        Du plus petit au plus grand avec ASC et du plus grand au plus petit avec DESC
        '''
        self.fill = sorted(self.fill)
        if self.ord == 'DESC':
            self.fill.reverse()
        #trie les elem enfilés en fonction de leur poids selon ord
