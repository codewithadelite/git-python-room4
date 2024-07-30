from .constants import LIGNES, COLONNES, VIDE


def initialise_matrice():
    """pour initialiser la matrice avec des VIDE."""
    matrice = []

    for _ in range(LIGNES):
        ligne = []
        for _ in range(COLONNES):
            ligne.append(VIDE)
        matrice.append(ligne)
    return matrice


def check_horizontal_combos(matrice, n_rows, n_cols, combo_length):
    """ ←→ 
    :param matrice: list() The matrice of the game.
    :param n_rows: int() Number of rows in the matrice.
    :param n_cols: int() Number of columns in the matrice.
    :param combo_length: int() The length of the winning combo.
    :return: int() 0 if not won and 1 or more if won
    """
    points = {length: 0 for length in combo_length}
    for r in range(n_rows):
        for length in combo_length:
            for c in range(n_cols - length + 1):
                if all(matrice[r][c + i] == matrice[r][c] != VIDE for i in range(length)):
                    points[length] += 1
    return points

def check_vertical_combos(matrice, n_rows, n_cols, combo_length):
    """ ↑↓
    :param matrice: list() The matrice of the game.
    :param n_rows: int() Number of rows in the matrice.
    :param n_cols: int() Number of columns in the matrice.
    :param combo_length: int() The length of the winning combo.
    :return: int() 0 if not won and 1 or more if won
    """
    points = {length: 0 for length in combo_length}
    for c in range(n_cols):
        for length in combo_length:
            for r in range(n_rows - length + 1):
                if all(matrice[r + i][c] == matrice[r][c] != VIDE for i in range(length)):
                    points[length] += 1
    return points


def check_pos_slope_combos(matrice, n_rows, n_cols, combo_length):
    """ ↗↙
    :param matrice: list() The matrice of the game.
    :param n_rows: int() Number of rows in the matrice.
    :param n_cols: int() Number of columns in the matrice.
    :param combo_length: int() The length of the winning combo.
    :return: int() 0 if not won and 1 or more if won
    """
    points = {length: 0 for length in combo_length}
    for length in combo_length:
        for r in range(n_rows - length + 1):
            for c in range(n_cols - length + 1):
                if all(matrice[r + i][c + i] == matrice[r][c] != VIDE for i in range(length)):
                    points[length] += 1
    return points

def check_neg_slope_combos(matrice, n_rows, n_cols, combo_length):
    """ ↘↖
    :param matrice: list() The matrice of the game.
    :param n_rows: int() Number of rows in the matrice.
    :param n_cols: int() Number of columns in the matrice.
    :param combo_length: int() The length of the winning combo.
    :return: int() 0 if not won and 1 or more if won
    """
    points = {length: 0 for length in combo_length}
    for length in combo_length:
        for r in range(length - 1, n_rows):
            for c in range(n_cols - length + 1):
                if all(matrice[r - i][c + i] == matrice[r][c] != VIDE for i in range(length)):
                    points[length] += 1
    return points

def alignement(matrice, combo_length=4):
    """Check for horizontal, vertical, or diagonal alignments
    :matrice: list() The matrice of the game
    :combo_length: int() The length of the winning combo
    :return: int() Total points based on alignments found.
    """
    if isinstance(combo_length, int):
        combo_length = [combo_length]
    n_rows = LIGNES or len(matrice)
    n_cols = COLONNES or len(matrice[0])
    total_points = 0
    points_per_length = {length: length for length in combo_length}

    horizontal_points = check_horizontal_combos(matrice, n_rows, n_cols, combo_length)
    vertical_points = check_vertical_combos(matrice, n_rows, n_cols, combo_length)
    pos_slope_points = check_pos_slope_combos(matrice, n_rows, n_cols, combo_length)
    neg_slope_points = check_neg_slope_combos(matrice, n_rows, n_cols, combo_length)

    for length in combo_length:
        total_points += horizontal_points[length] * points_per_length[length]
        total_points += vertical_points[length] * points_per_length[length]
        total_points += pos_slope_points[length] * points_per_length[length]
        total_points += neg_slope_points[length] * points_per_length[length]

    return total_points


def is_full_column(matrice, num_col):
    if num_col < 0 or num_col >= COLONNES:
        raise IndexError(f"Column index {num_col} is out of range")
    for row in matrice:
        if row[num_col] == VIDE:
            return False
    return True


def is_full_board(matrice):
    """
    Verify if the board is full
    :param matrice : List that represent board
    :return: (bool) True if board is full, otherwise False
    """
    return all(is_full_column(matrice, col) for col in range(COLONNES))