class Graphe_pondere:
    def __init__(self,vois = {}):
        self.vois = vois

    def __repr__(self)->dict:
        nouveau_dict = {}
        for i in list(self.vois.keys()):
            nouveau_dict[i] = self.vois[i]
        return(f"{nouveau_dict}")
    
    def taille(self):
        return len(self.vois.keys())

    def ajouter_sommet(self,sommet,liens):
        self.vois[sommet] = liens
        for i in list(liens.keys()):
            self.vois[i][sommet] = liens[i]

    def supprimer_sommet(self,sommet):
        liens_sommet = self.vois[sommet]
        del self.vois[sommet]
        for i in list(self.vois.keys()):
            del self.vois[i][sommet.index(self.vois[i])]
