import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
font = pygame.font.SysFont('arial', 25)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


Point = namedtuple('Point', 'x, y')

# rgb colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)
LIME = (0, 255, 0)

BLOCK_SIZE = 20
SPEED = 10


class SnakeGame:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake By Daryl :)")
        self.clock = pygame.time.Clock()

        # init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()

    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def _update_ui(self):
        self.display.fill(BLACK)
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1,
                             pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2,
                             pygame.Rect(pt.x + (BLOCK_SIZE*1/5), pt.y + (BLOCK_SIZE*1/5),
                                         (BLOCK_SIZE*3/5), (BLOCK_SIZE*3/5)))

        pygame.draw.rect(self.display, LIME,
                         pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render(f'Score: {self.score}', True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE

        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE

        elif direction == Direction.UP:
            y -= BLOCK_SIZE

        elif direction == Direction.DOWN:
            y += BLOCK_SIZE

        self.head = Point(x, y)

    def _is_collision(self):
        # Hits boundary
        cond1 = (self.head.x > self.w - BLOCK_SIZE)
        cond2 = (self.head.x < 0)
        cond3 = (self.head.y > self.h - BLOCK_SIZE)
        cond4 = (self.head.y < 0)
        if cond1 or cond2 or cond3 or cond4:
            return True

        # Hits itself
        if self.head in self.snake[1:]:
            return True

        return False

    def play_step(self):
        # 1. Collect User Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN

        # 2. Move
        self._move(self.direction)
        self.snake.insert(0, self.head)

        # 3. Check if game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score

        # 4. Place new food or just move
        if self.head == self.food:
            self.score += 1
            self._place_food()

        else:
            self.snake.pop()

        # 5. Update UI and Clock
        self._update_ui()
        self.clock.tick(SPEED)

        # 6. Return game over and score
        return game_over, self.score


if __name__ == '__main__':
    game = SnakeGame()

    while True:
        game_over, score = game.play_step()

        if game_over:
            break

    print(f'Final Score: {score}')

    label = font.render(f'GAME OVER', True, WHITE)
    label_rect = label.get_rect(center=(game.w/2, game.h/2 - 50))
    label2 = font.render(f'Final Score: {score}', True, WHITE)
    label2_rect = label.get_rect(center=(game.w/2, game.h/2))

    game.display.blit(label, label_rect)
    game.display.blit(label2, label2_rect)

    pygame.display.update()

    pygame.time.wait(5000)

    pygame.quit()

