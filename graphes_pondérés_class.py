class Graphe_pondere:
    def __init__(self,vois = {}):
        self.vois = vois

    def __repr__(self)->str:
        nouveau_dict = {}
        for i in list(self.vois.keys()):
            nouveau_dict[i] = self.vois[i]
        return(f"{nouveau_dict}")

    def ajouter_sommet(self,sommet,liens):
        self.vois[sommet] = liens
        for i in list(liens.keys()):
            self.vois[i][sommet] = liens[i]

    def supprimer_sommet(self,sommet):
        liens_sommet = self.vois[sommet]
        del self.vois[sommet]
        for i in list(liens_sommet.keys()):
            for k,v in self.vois[i].items():
                if k == sommet:
                    del self.vois[i][k]
                    break

    def taille(self):
        return len(self.vois.keys())

    def est_vide(self):
        return self.vois == {}

    def contient(self,s,t):
        if t in self.vois[s].keys():
            return True
        else:
            return False

    def longueur_arete(self,s,t):
        try:
            assert self.existe(s)
            assert self.existe(t)
        except ValueError:
            pass
        return self.vois[s][t]

    def existe(self,s):
        return s in self.vois.keys()