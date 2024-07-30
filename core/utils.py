from .constants import LIGNES, COLONNES, VIDE


def initialise_grille():
    """pour initialiser la grille avec des VIDE."""
    grille = []

    for _ in range(LIGNES):
        ligne = []
        for _ in range(COLONNES):
            ligne.append(VIDE)
        grille.append(ligne)
    return grille


def alignement():
    """pour vérifier l'alignement horizontal, vertical ou diagonal"""
    pass

