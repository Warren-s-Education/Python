from random import randrange
from copy import deepcopy


class IllegalMoveError(Exception):
    pass


class InvalidMoveError(Exception):
    pass


BOARD = [
    [(3 * row_index) + (1 + column_index) for row_index in range(3)]
    for column_index in range(3)
]

NAUGHT = 'O'
CROSS = 'X'


def print_marker_row(row):
    """Print row that contains game markers."""
    column_third = list(
        f"|{'': ^7}"
    )
    for column in range(3):
        column_third[4] = row[column]
        print(''.join(column_third), sep='', end='')
    print('|')


def display_board(board):
    """Print tic-tac-toe board."""
    HORIZONTAL_RULE = (f"+{'':-^7}" * 3) + "+"
    NO_MARKER_ROW = (f"|{'': ^7}" * 3) + "|"

    print(HORIZONTAL_RULE)
    for row in board:
        print(NO_MARKER_ROW)
        print_marker_row(row)
        print(NO_MARKER_ROW)
        print(HORIZONTAL_RULE)


def is_unoccupied(square, board):
    return board[square//3][square % 3].isnumeric()


def place_marker(square, marker, board):
    """Update board with """
    board[square//3][square % 3] = marker


def draw_move(board, marker):
    """Get legal move from computer and draw new board."""
    while True:
        square = randrange(0, 9)
        print(square + 1)
        if is_unoccupied(square, board):
            place_marker(square, marker, board)
            break
    display_board(board)


def enter_move(board, marker):
    """Get legal move from player and draw new board."""

    print("Enter your move: ", end='')

    while True:
        try:
            square = int(input()) - 1
            if is_unoccupied(square, board):
                place_marker(square, marker, board)
                break
            else:
                raise IllegalMoveError()
        except ValueError as e:
            print("\nThat move is invalid. Enter an integer from 1 to 9: ", end='')
        except IllegalMoveError as e:
            print("\nThat move is not legal. Play on an unoccupied square: ", end='')
    print()
    display_board(board)


def enter_move_v2(board):
    """Get legal move from player as (row, column) index."""
    is_valid_input = False
    is_unoccupied_position = False

    while not (is_valid_input and is_unoccupied_position):
        # Get user input and validate; if not valid, return to start of loop.
        move = input("Enter your move: ")
        is_valid_input = (len(move) == 1
                          and move >= '1'
                          and move <= '9')
        if not is_valid_input:
            print("Bad move - repeat your input!")
            continue

        # Convert position to row and column indices.
        move = int(move) - 1 	# cell's number from 0 to 8
        row = move // 3 	    # cell's row
        col = move % 3		    # cell's column

        # Check that the position is unoccupied; if occupied, return to start of
        # loop.
        is_unoccupied_position = board[row][col] in [NAUGHT, CROSS]
        if not is_unoccupied_position:
            print("Field already occupied - repeat your input!")
            continue

    return (row, col)


def victory_for(board, marker):
    '''Check if the game has been won.'''
    info = board, marker
    if (is_row_victory(*info)
            or is_column_victory(*info)
            or is_diagonal_victory(*info)
            ):
        return True
    else:
        return False


def is_row_victory(board, marker):
    '''Check if the game has been won on a row.'''
    for row in board:
        if ''.join(row) == marker * 3:
            return True
    return False


def is_column_victory(board, marker):
    '''Check if the game has been won on a column.'''
    for i in range(3):
        column = [
            board[0][i], board[1][i], board[2][i]
        ]
        if ''.join(column) == marker * 3:
            return True
    return False


def is_diagonal_victory(board, marker):
    '''Check if the game has been won on a diagonal.'''
    major_diagonal = [board[i][i] for i in range(3)]
    if ''.join(major_diagonal) == marker * 3:
        return True

    minor_diagonal = [board[i][j] for i, j in zip(range(3), range(2, -1, -1))]
    if ''.join(minor_diagonal) == marker * 3:
        return True

    return False


def play_game():
    COMPUTER, PLAYER = 0, 1
    MARKERS = [CROSS, NAUGHT]
    board = deepcopy(BOARD)
    # Since a maximum of 9 moves can be made on a 3x3 tic-tac-toe board, the
    # game loop repeats at most 9 times. If no victory condition breaks the
    # game loop, the game results in a draw. The computer plays on odd turns;
    # the human plays on even turns.
    for i in range(9):
        if i % 2 == COMPUTER:
            draw_move(board)
            if victory_for(board, MARKERS[COMPUTER]):
                print("Computer wins.")
                break
        else:
            enter_move(board)
            if victory_for(board, MARKERS[PLAYER]):
                print("Player wins.")
                break
    else:
        print("The game is a draw.")
