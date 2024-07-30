from core.constants import LIGNES, COLONNES, JOUEURS, VIDE
from core.utils import initialise_grille, alignement
from core.ui import afficher_grille


def jouer(grille, colonne, pion):
    """place le pion dans la colonne choisie par l'utilisateur"""
    for ligne in reversed(grille):
        if ligne[colonne - 1] == VIDE:
            ligne[colonne - 1] = pion
            break        

def saisie_colonne():
    """
    Demande à l'utilisateur de saisir une colonne valide dans laquelle jouer.
    Retourne la colonne saisie par l'utilisateur.
    """
    # Indique si la saisie est valide ou non
    isValid = False

    # Boucle tant que la saisie n'est pas valide
    while not isValid:
        try:
            # Demande à l'utilisateur de saisir une colonne
            col = int(input(f"Saisissez la colonne dans laquelle vous voulez jouer (1-{COLONNES}) : "))

            # Vérifie si la colonne est valide
            if 1 <= col <= COLONNES:
                isValid = True
                return col

            # Affiche un message d'erreur si la colonne n'est pas valide
            print(f"Veuillez entrer une colonne valide (1-{COLONNES})")
        except ValueError:
            # Affiche un message d'erreur si la saisie n'est pas un nombre
            print("Veuillez entrer une valeur numérique")
            

def main():
    """Où le jeu commencera."""
    grille = initialise_grille()
    afficher_grille(grille)


if __name__ == "__main__":
    main()
