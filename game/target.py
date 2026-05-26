import pygame
from game_variables.GameVariables import GameVariables as gv


class Target:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.targets = Target
        self.width = gv.TARGET_SIZE
        self.height = gv.TARGET_SIZE
        self.x_pos = gv.SCREEN_WIDTH // 2 - self.width // 2
        self.y_pos = 30
        self.direction = 1
        self.health = 1

    def get_rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def update_and_draw(self):
        self.x_pos += 1.5 * self.direction
        if self.x_pos <= 0 or self.x_pos >= gv.SCREEN_WIDTH - self.width:
            self.direction *= -1
        pygame.draw.rect(self.screen, "red", self.get_rect())
