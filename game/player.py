import pygame
from game_variables.GameVariables import GameVariables as gv
from game.bullet import Bullet, Bullets

class Player:
    def __init__(self, screen: pygame.Surface, bullets: Bullet):
        self.screen = screen
        self.width = gv.SCREEN_WIDTH * 0.08
        self.height = gv.SCREEN_HEIGHT * 0.12
        self.x_pos = gv.SCREEN_WIDTH // 2 - self.width // 2
        self.y_pos = gv.SCREEN_HEIGHT - self.height - 10
        self.bullets = bullets

    def get_rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def shoot(self):
        mx = self.x_pos + self.width / 2 - gv.BULLET_SIZE / 2
        my = self.y_pos - gv.BULLET_SIZE
        self.bullets.(Bullet(self.screen, mx, my, 0, -3))

    def update_and_draw(self, frame_counter: int):
        # aus PyGame SpaceShooter aus dem Unterricht
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x_pos > 0:
            self.x_pos -= 2
        if keys[pygame.K_d] and self.x_pos < gv.SCREEN_WIDTH - self.width:
            self.x_pos += 2
        # bis hier her

        # # # KI Google Gemini
        # Fehlende Zeichen-Logik hinzugefügt (zeichnet vorerst ein rotes Rechteck)
        pygame.draw.rect(self.screen, "red", self.get_rect())
        # # # KI Ende, Prompt: ich kann den Player nicht zeichnen sag mir was falsch ist
