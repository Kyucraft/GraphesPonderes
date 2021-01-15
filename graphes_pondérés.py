from graphes_pondérés_class import *

g = Graphe_pondere({
    'a' : {'b' : 4, 'c' : 7},
    'b' : {'a' : 4, 'c' : 3},
    'c' : {'a' : 7, 'b' : 3}
})
"""
g.ajouter_sommet('d',{'b' : 5, 'c' : 6})
print(g)
g.supprimer_sommet('d')
print(g)
"""
print(g.liste_distance_arette())
