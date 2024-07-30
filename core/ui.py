from .constants import COLONNES


def afficher_grille(grille):
    """pour afficher la grille."""
    for ligne in grille:
        print(' '.join(ligne))
    print(' '.join([str(i) for i in range(1, COLONNES + 1)]))

