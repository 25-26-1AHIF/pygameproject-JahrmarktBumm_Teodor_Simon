import pygame
from game_variables.GameVariables import GameVariables as gv

class Player:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.width = gv.SCREEN_WIDTH * 0.75
        self.height = gv.SCREEN_HEIGHT * 0.75
        self.x_pos = gv.SCREEN_WIDTH // 2 - self.width // 2
        self.y_pos = gv.SCREEN_HEIGHT - self.height - 10

    def get_rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def update_and_draw(self, frame_counter: int):
        # aus PyGame SpaceShooter aus dem Unterricht
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x_pos > 0:
            self.x_pos -= 2
        if keys[pygame.K_d] and self.x_pos < gv.SCREEN_WIDTH - self.width:
            self.x_pos += 2
        # bis hier her

        # # # KI Google Gemini Anfang
        # Fehlende Zeichen-Logik hinzugefügt (zeichnet vorerst ein rotes Rechteck)
        pygame.draw.rect(self.screen, "red", self.get_rect())
        # # # KI Ende, Prompt: ich kann den Player nicht zeichnen sag mir was falsch ist
