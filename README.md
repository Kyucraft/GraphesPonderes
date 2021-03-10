La fonction 'parcours_largeur_pond()' prend deux éléments en Entrée:

  -> self, soit le graphe pondéré (puisqu'il s'agit d'une fonction qui sera ajoutée dans la class éponyme).
  
  -> s_i, soit le sommet à partir duquel on souhaite effectuer la fonction.
  


Le processus suit le même principe que celui vu sur le papier. Nous partons d'un sommet et avançons de proche en proche, tout en utilisant une file de priorité pour le choix des sommets à traîter à chaque début de boucle.



En sortie, la fonction PEUT retourner :

  -> distance et parents, deux dictionnaires renseignant pour le premier la distance de tout sommet par rapport au sommet initial et pour le second le parent de tout sommet.
  
  -> arbre_pond, l'arbre pondéré correspondant au graphe, qui est généré par une seconde fonction, la fonction 'generer_arbre_pondere()'
  
  
---------------


La seconde fonction, 'generer_arbre_pondere()', profite des travaux faits précédemment sur le fichier tree.py, qui a été modifié à l'occasion pour accueillir des noeuds sous forme de Tuple (a,b), lettres représentant respectivement le nom du sommet/noeud et la distance de ce-dernier vis-à-vis du sommet initial/de la racine de l'arbre.

La fonction prend en entrée :

  -> self, soit le graphe pondéré (il ne sert foncièrement à rien dans la fonction).
  
  -> s, le sommet duquel on part (donc le sommet initial utilisé dans la première fonction).
  
  -> d, le dictionnaire distance généré dans la première fonction.
  
  -> p, le dictionnaire parents généré dans la première fonction.
  
  
  
Le principe de la fonction est simple : à chaque début de boucle, il vient récupérer le premier élément d'un tableau généré en interne. Cet élément correspond à un sommet. Si ce sommet ne figure pas dans l'arbre, il y sera ajouté, avec la distance associée renseignée dans le dictionnaire d, en tant qu'enfant de son parent, renseigné dans le dictionnaire p. Puis le dictionnaire p sera parcouru, et le tableau précédemment cité recevra les noms de tout sommet ayant pour parent le sommet étudié durant ce tour.
Le processus tourne jusqu'à ce que le tableau cité précédemment soit vide.



En sortie, la fonction retourne :

  -> arbre, un arbre généré en début de fonction via la class Tree ('tree.py') et complété au fur et à mesure.
