from core.constants import LIGNES, COLONNES, JOUEURS
from core.utils import initialise_grille, alignement
from core.ui import afficher_grille

def jouer():
    """pour jouer"""
    pass

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
            col = int(input(f"Saisissez la colonne dans laquelle vous voulez jouer (0-{COLONNES-1}) : "))

            # Vérifie si la colonne est valide
            if 0 <= col < COLONNES:
                isValid = True
                return col

            # Affiche un message d'erreur si la colonne n'est pas valide
            print(f"Veuillez entrer une colonne valide (0-{COLONNES-1})")
        except ValueError:
            # Affiche un message d'erreur si la saisie n'est pas un nombre
            print("Veuillez entrer une valeur numérique")
            

def main():
    """Où le jeu commencera."""
    pass


if __name__ == "__main__":
    main()
