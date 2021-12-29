import pygame
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Init State
pygame.init()

size = width, height = 1040, 720
screen = pygame.display.set_mode(size, pygame.SRCALPHA)
pygame.display.set_caption('Colliding Balls by Daryl :)')


# Soccer Balls
class Ball:
    def __init__(self, image, surface=screen, position=[width / 2, height / 2], speed=[1, 1]):
        self.image = image
        self.surface = surface
        self.position = position
        self.speed = speed

        self.ball = pygame.image.load(self.image)
        self.ball.set_colorkey(WHITE)
        self.ball.convert_alpha()

        self.ball = pygame.transform.scale(self.ball, (int(self.ball.get_width() / 2),
                                                       int(self.ball.get_height() / 2)))
        self.ball_rect = self.ball.get_rect(topleft=self.position)

    def check_border(self):
        if self.ball_rect.left < 0 or self.ball_rect.right > width:
            self.speed[0] *= -1
        elif self.ball_rect.top < 0 or self.ball_rect.bottom > height:
            self.speed[1] *= -1

    def draw_ball(self):
        self.surface.blit(self.ball, self.ball_rect)

    def move_ball(self):
        self.check_border()
        self.ball_rect = self.ball_rect.move(self.speed)
        self.draw_ball()

    def increase_speed(self):
        if self.speed[0] < 0:
            self.speed[0] -= 1
        if self.speed[1] < 0:
            self.speed[1] -= 1
        if self.speed[0] > 0:
            self.speed[0] += 1
        if self.speed[1] > 0:
            self.speed[1] += 1
        else:
            self.speed[0] += 1
            self.speed[1] += 1

    def decrease_speed(self):
        if self.speed[0] == 0:
            self.speed[0] += 0
        if self.speed[1] == 0:
            self.speed[1] += 0
        if self.speed[0] < 0:
            self.speed[0] += 1
        if self.speed[1] < 0:
            self.speed[1] += 1
        if self.speed[0] > 0:
            self.speed[0] -= 1
        if self.speed[1] > 0:
            self.speed[1] -= 1

    def check_collision(self, rect):
        case_a = (rect.top < self.ball_rect.bottom < rect.bottom)
        case_b = (rect.top < self.ball_rect.top < rect.bottom)

        case_c = (rect.left < self.ball_rect.right < rect.right)
        case_d = (rect.left < self.ball_rect.left < rect.right)

        if (case_a or case_b) and (case_c or case_d):
            self.speed[0] *= -1
            self.speed[1] *= -1


# Ball A
soccer_a = Ball('Soccer.gif', screen, [0, 0], [1, 1])

# Ball B
soccer_b = Ball('Soccer.gif', screen, [width - 200, 0], [-1, 1])

# Ball C
soccer_c = Ball('Soccer.gif', screen, [0, height - 200], [1, -1])

# Ball D
soccer_d = Ball('Soccer.gif')

# Ball E
tennis = Ball('tennis.gif')

# Ball F
beach = Ball('beach.png')

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            time.sleep(3)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_PLUS:
                soccer_a.increase_speed()
                time.sleep(3)

            if event.key == pygame.K_KP_MINUS:
                soccer_a.decrease_speed()
                time.sleep(3)

    # Draw Balls and Update Screen

    screen.fill(WHITE)

    soccer_a.check_collision(soccer_b.ball_rect)
    soccer_a.check_collision(soccer_c.ball_rect)
    soccer_a.check_collision(soccer_d.ball_rect)
    soccer_a.move_ball()

    soccer_b.check_collision(soccer_a.ball_rect)
    soccer_b.check_collision(soccer_c.ball_rect)
    soccer_b.check_collision(soccer_d.ball_rect)
    soccer_b.move_ball()

    soccer_c.check_collision(soccer_a.ball_rect)
    soccer_c.check_collision(soccer_b.ball_rect)
    soccer_c.check_collision(soccer_d.ball_rect)
    soccer_c.move_ball()

    soccer_d.check_collision(soccer_a.ball_rect)
    soccer_d.check_collision(soccer_b.ball_rect)
    soccer_d.check_collision(soccer_c.ball_rect)
    soccer_d.move_ball()

    pygame.display.flip()
