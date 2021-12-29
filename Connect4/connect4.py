import numpy as np
import pygame
import sys
import math

# CONSTANTS
ROW_COUNT = 6
COL_COUNT = 7
SQUARE_SIZE = 100
RADIUS = SQUARE_SIZE/2 - 5

# COLORS
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


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


def draw_board(surface, b):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(surface, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if b[r, c] == 0:
                pygame.draw.circle(surface, BLACK, (c*SQUARE_SIZE+SQUARE_SIZE/2, r*SQUARE_SIZE+SQUARE_SIZE*3/2), RADIUS)
            elif b[r, c] == 1:
                pygame.draw.circle(surface, RED,
                                   (c * SQUARE_SIZE + SQUARE_SIZE / 2, r * SQUARE_SIZE + SQUARE_SIZE * 3 / 2), RADIUS)
            elif b[r, c] == 2:
                pygame.draw.circle(surface, YELLOW,
                                   (c * SQUARE_SIZE + SQUARE_SIZE / 2, r * SQUARE_SIZE + SQUARE_SIZE * 3 / 2), RADIUS)
    pygame.display.update()


# Graphics
pygame.init()

width = COL_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)

myFont = pygame.font.SysFont("monospace", 75)

# Init State
board = create_board(ROW_COUNT, COL_COUNT)
print(board)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Connect 4 by Daryl :)')
draw_board(screen, board)
pygame.display.update()

game_over = False
turn = 0

# Game Loop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            pos_x = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (pos_x, SQUARE_SIZE/2), RADIUS)

            else:
                pygame.draw.circle(screen, YELLOW, (pos_x, SQUARE_SIZE / 2), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            # Ask player 1 input
            if turn == 0:
                pos_x = event.pos[0]
                selection = int(math.floor(pos_x/SQUARE_SIZE))
                drop_piece(board, 1, ROW_COUNT - 1, selection)
                if is_winning(board, 1):
                    print('Congrats!! Player 1 wins!!')
                    label = myFont.render('Player 1 wins!', True, RED)
                    screen.blit(label, (40, 10))
                    game_over = True

            # Ask player 2 input
            else:
                pos_x = event.pos[0]
                selection = int(math.floor(pos_x / SQUARE_SIZE))
                drop_piece(board, 2, ROW_COUNT - 1, selection)
                if is_winning(board, 2):
                    print('Congrats!! Player 2 wins!!')
                    label = myFont.render('Player 2 wins!', True, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True
            print(board)
            draw_board(screen, board)
            pygame.display.update()

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)