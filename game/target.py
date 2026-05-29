import pygame
from game_variables.GameVariables import GameVariables as gv


class Target:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.width = gv.TARGET_SIZE
        self.height = gv.TARGET_SIZE
        self.x_pos = -self.width
        self.y_pos = 50
        self.direction = 1
        self.speed = 2.5

    def get_rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def update_and_draw(self):
        self.x_pos += self.speed * self.direction
        pygame.draw.rect(self.screen, "red", self.get_rect())


class Targets:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.targets = []

    def add_target(self):
        self.targets.append(Target(self.screen))

    def update_and_draw(self, frame_counter: int):
        # Gleichmäßiger Spawn-Takt: Alle 2 Sekunden (120 Frames bei 60 FPS)
        if frame_counter % 120 == 0:
            self.add_target()

        for target in self.targets[:]:
            target.update_and_draw()

            # Ziel löschen, wenn es den rechten Bildschirmrand verlässt
            if target.x_pos > gv.SCREEN_WIDTH:
                if target in self.targets:
                    self.targets.remove(target)
