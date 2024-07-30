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


def check_horizontal_combos(board, n_rows, n_cols, combo_length=4):
    """ ←→ """
    points = {length: 0 for length in combo_length}
    for r in range(n_rows):
        for length in combo_length:
            for c in range(n_cols - length + 1):
                if all(board[r][c + i] == board[r][c] != 0 for i in range(length)):
                    points[length] += 1
    return points

def check_vertical_combos(board, n_rows, n_cols, combo_length):
    """ ↑↓
    :param board: list() The board of the game.
    :param n_rows: int() Number of rows in the board.
    :param n_cols: int() Number of columns in the board.
    :param combo_length: int() The length of the winning combo.
    :return: bool() True if the winning combo, false otherwise.
    """
    points = {length: 0 for length in combo_length}
    for c in range(n_cols):
        for length in combo_length:
            for r in range(n_rows - length + 1):
                if all(board[r + i][c] == board[r][c] != 0 for i in range(length)):
                    points[length] += 1
    return points


def check_pos_slope_combos(board, n_rows, n_cols, combo_length):
    """ ↗↙
    :param board: list() The board of the game.
    :param n_rows: int() Number of rows in the board.
    :param n_cols: int() Number of columns in the board.
    :param combo_length: int() The length of the winning combo.
    :return: bool() True if the winning combo, false otherwise.
    """
    points = {length: 0 for length in combo_length}
    for length in combo_length:
        for r in range(n_rows - length + 1):
            for c in range(n_cols - length + 1):
                if all(board[r + i][c + i] == board[r][c] != 0 for i in range(length)):
                    points[length] += 1
    return points

def check_neg_slope_combos(board, n_rows, n_cols, combo_length):
    """ ↘↖
    :param board: list() The board of the game.
    :param n_rows: int() Number of rows in the board.
    :param n_cols: int() Number of columns in the board.
    :param combo_length: int() The length of the winning combo.
    :return: bool() True if the winning combo, false otherwise.
    """
    points = {length: 0 for length in combo_length}
    for length in combo_length:
        for r in range(length - 1, n_rows):
            for c in range(n_cols - length + 1):
                if all(board[r - i][c + i] == board[r][c] != 0 for i in range(length)):
                    points[length] += 1
    return points

def alignement(matrice, combo_length=4):
    """Check for horizontal, vertical, or diagonal alignments
    :matrice: list() The board of the game
    :combo_length: int() The length of the winning combo
    :return: int() Total points based on alignments found.
    """
    n_rows = len(matrice)
    n_cols = len(matrice[0])
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



