import pygame
from game_variables.GameVariables import GameVariables as gv
from game.player import Player as Player

class Bullet:
    def __init__(self, screen: pygame.Surface, x_pos: float, y_pos: float, dx: float, dy: float):
        self.screen = screen
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dx = dx
        self.dy = dy
        self.width = gv.BULLET_SIZE
        self.height = gv.BULLET_SIZE

    def get_rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def update_and_draw(self):
        self.x_pos += self.dx
        self.y_pos += self.dy
        pygame.draw.rect(self.screen, "gold", (self.x_pos, self.y_pos, self.width, self.height))

class Bullets:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.bullets = []

    def add_rocket(self, bullet):
        self.bullets.append(bullet)

    def update_and_draw(self):
        for bullet in self.bullets[:]:
            bullet.update_and_draw()
            if bullet.y_pos < - bullet.height or bullet.y_pos > gv.SCREEN_HEIGHT:
                self.bullets.remove(bullet)