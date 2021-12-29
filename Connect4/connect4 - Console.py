import numpy as np
import time


# CONSTANTS
ROW_COUNT = 6
COL_COUNT = 7


# Functions
def create_board(r, c):
    b = np.zeros((r, c))
    return b


def is_valid(b, sel):
    return b[0, sel] == 0


def drop_piece(b, player, r, sel):
    global turn
    if r == 0:
        if is_valid(b, sel):
            b[r, sel] = player

        else:
            print('No more room please make another choice:')
            turn += 1

    elif b[r, sel] == 0:
        b[r, sel] = player

    else:
        drop_piece(b, player, r - 1, sel)


def is_winning(b, player):
    # Horizontal win
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if b[-(r + 1), c] == player and b[-(r + 1), c + 1] == player and \
                    b[-(r + 1), c + 2] == player and b[-(r + 1), c + 3] == player:
                return True

    # Vertical win
    for r in range(ROW_COUNT - 3):
        for c in range(COL_COUNT):
            if b[-(r + 1), c] == player and b[-(r + 2), c] == player and \
                    b[-(r + 3), c] == player and b[-(r + 4), c] == player:
                return True

    # Diagonal win Positive Slope
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if b[-(r + 1), c] == player and b[-(r + 2), c + 1] == player and \
                    b[-(r + 3), c + 2] == player and b[-(r + 4), c + 3] == player:
                return True

    # Diagonal Win Negative Slope
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if b[r, c] == player and board[r + 1, c + 1] == player and \
                    b[r + 2, c + 2] == player and b[r + 3, c + 3] == player:
                return True


# Init State
board = create_board(ROW_COUNT, COL_COUNT)
print(board)


game_over = False
turn = 0

# Game Loop
while True:
    print(80*'*')
        
    # Ask player 1 input
    try:
        if turn == 0:
            selection = int(input('Player 1 make your move (1:7):'))
            if selection not in range(COL_COUNT + 1):
                print('Please select a value between 1 and 7')
                turn += 1
            else:
                drop_piece(board, 1, ROW_COUNT - 1, selection - 1)
                                    
                print(board)
                
                if is_winning(board, 1):
                    print('Congrats!! Player 1 won!!')
                    time.sleep(5)
                    break

    # Ask player 2 input
        else:
            selection = int(input('Player 2 make your move (1:7):'))
            if selection not in range(COL_COUNT + 1):
                print('Please select a value between 1 and 7')
                turn += 1
            else:
                drop_piece(board, 2, ROW_COUNT - 1, selection - 1)
                    
                print(board)
                
                if is_winning(board, 2):
                    print('Congrats!! Player 2 won!!')
                    time.sleep(5)
                    break

        turn += 1
        turn = turn % 2
        
    except EOFError:
        break
