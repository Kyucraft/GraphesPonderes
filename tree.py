#Les fonctions ci-dessous ont été sensiblement modifiée pour que l'arbre utilisé soit un arbre podéré, et pas seulement un arbre "classique".

from __future__ import annotations
from typing import List, TypeVar

T = TypeVar('T')

class Tree:
    def __init__(self, val: T, enfants: List[Tree]):
        '''
        un arbre est :
        soit vide, 
        soit la donnée d'une valeur à la racine
        et de la liste de ses sous-arbres
        '''
        self.val = val
        self.enfants = enfants


    def vide():
        return Tree(None,[])


    def est_vide(self):
        return self.val == None and self.enfants == []


    def contient(self, v):
        if self.est_vide():
            return False
        else:
            va,po = self.val
            return va==v or any(map(lambda e:e.contient(v), self.enfants))


    def ajouter_noeud(self,v,p):
        '''
        ajoute l'arbre Tree(v,[]) 
        comme enfant du noeud de val p dans self
        '''
        if not self.est_vide():
            va,po = self.val
            if va==p:
                self.enfants.append(Tree(v,[]))
            else:
                for e in self.enfants:
                    e.ajouter_noeud(v,p)


    def afficher(self,depth=0):
        if not self.est_vide():
            if depth==0:
                print(f'{depth*"___"+str(self.val)}')
            else:
                print(f'|{depth*"___"+str(self.val)}')

            for e in self.enfants:
                e.afficher(depth+1)

        return None


    def appliquer(self,f):
        '''
        map sur les valeurs
        '''
        if not self.est_vide():
            f(self.val)
            list(map(lambda e:e.appliquer(f), self.enfants))


    def t_map(self, f):
        '''
        map sur les sous-arbres
        NON fonctionnel
        '''
        if not self.est_vide():
            list(map(lambda e:e.t_map(f), self.enfants))



    #La fonction provient de 'graphepond_integration.py. Elle n'est copiée ici qu'à des fins de tests !!!
    '''
    def generer_arbre_pondere(self,s,d,p):
        

        tab_sommets = [s]

        while len(tab_sommets)!=0:
            print(tab_sommets)
            som = tab_sommets.pop(0)
            if som==s or not(self.contient(som)):
                if som!=s:
                    self.ajouter_noeud((som,d[som]),p[som])
                for keys,val in p.items():
                    if som == val:
                        tab_sommets.append(keys)
    '''




#Exemple fonctionnel avec le nouveau model d'arbre

'''
arbre = Tree(
    ("*",0),[
        Tree(
            ('+',2),[
                Tree(
                    (4,8),[]
                ),
                Tree(
                    (5,3),[]
                )
            ]),
        Tree((3,1),[])
    ]
)

arbre.afficher()
print(arbre.contient(9))
arbre.ajouter_noeud((9,8),'+')
arbre.afficher()
print(arbre.contient(9))
'''


#Test de la fonction generer_arbre_pondere() présente dans graphepond_integration.py

'''
arbre = Tree(("a",0),[])
parents = {
    "a":None,
    "b":"a",
    "c":"a",
    "d":"b",
    "e":"b",
    "f":"c",
    "g":"c",
    "h":"d",
    "i":"e",
    "j":"e",
    "k":"e",
    "l":"g"
}

distance = {
    "a":"infini",
    "b":2,
    "c":3,
    "d":3,
    "e":4,
    "f":7,
    "g":8,
    "h":12,
    "i":5,
    "j":7,
    "k":19,
    "l":42
}

arbre.afficher()
arbre.generer_arbre_pondere("a",distance,parents)
arbre.afficher()
'''
