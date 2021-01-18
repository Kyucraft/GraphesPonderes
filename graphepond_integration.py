#Algo:

'''
fct parcours_largeur_pond(G,s_i):

    ##### comme c'est un algorithme, il n'est pas vraiment écrit comme une méthode. #####
    ##### cet algo ne couvre pas la partie sur la réalisation de l'arbre. Seulement les dicts parent et distance #####

    file = PriorityQueue()
    couleur = {}
    distance = {}
    parents = {}

    POUR CHAQUE s DANS G-[s_i]:
        couleur[s] <- "blanc"
        distance[s] <- 0
        parent[s]<-None

    couleur[s_i] <- "gris"
    distance[s_i] <- 0
    parent[s_i] <- None

    file.enfiler((s_i,0))

    TANT QUE NON file.est_vide():
        n <- file.defiler()
        val,dis <- n
        couleur[val] <- "noir"

        POUR CHAQUE v dans val.voisins:
            SI couleur[v]!="noir":
                SI couleur[v] == "blanc":
                    couleur[v] <- "gris"
                    distance[v] <- distance[val] + G.longueur(val,v)
                    parents[v] <- val
                    f.enfiler((v,distance[v]))

                SINON SI couleur[v] == "gris":
                    SI distance[val] + G.longueur(val,v) < distance[v]:
                        distance[v] <- distance[val] + G.longueur(val,v)
                        parents[v] <- val 
                        f.enfiler((v,distance[v]))
'''


from priority_queue import *
from graphe_pondere import *
from tree import *


def parcours_largeur_pond(self,s_i):
    #Ici, self apparaît comme une variable muette, mais tout est déjà configuré de sorte à ce qu'il suffise de coller la 
    #fonction dans graphe_pondere.py

    f = PriorityQueue(self.taille(),"",'ASC')   
    couleur = {}
    distance = {}
    parents = {}

    for s in self.arete:
        couleur[s] = "blanc"
        distance[s] = "infini"
        parent[s] = None

    couleur[s_i] = "gris"
    distance[s_i] = 0
    parent[s_i] = None

    f.enfiler((s_i,0))

    while not(f.est_vide()):
        n = f.defiler()
        val,dis = n
        couleur[val] = "noir"

        for v in val.arete:
            if couleur[v] != "noir":
                if couleur[v] == "blanc":
                    couleur[v] = "gris"
                    distance[v] = distance[val] + self.longueur(val,v)
                    parents[v] = val

                    f.enfiler((v,distance[v]))

                elif couleur[v] == "gris":
                    if distance[val] + self.longueur(val,v) < distance[v]:
                        distance[v] = distance[val] + self.longueur(val,v)
                        parents[v] = val

                        #ajouter le défilement de l'ancienne valeur associé à v dans la file. 
                        #Peut être une méthode de la Class PriorityQueue pour ça ?
                        f.enfiler((v,distance[v]))
