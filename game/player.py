import pygame
from game_variables.GameVariables import GameVariables as gv
from game.bullet import Bullet, Bullets
from game.sprite import Sprite # <- KI Hilfe bei Sprite


class Player:
    def __init__(self, screen: pygame.Surface, bullets: Bullets):
        self.screen = screen
        self.width = gv.SCREEN_WIDTH * 0.08
        self.height = gv.SCREEN_HEIGHT * 0.12
        self.x_pos = gv.SCREEN_WIDTH // 2 - self.width // 2
        self.y_pos = gv.SCREEN_HEIGHT - self.height - 10
        self.bullets = bullets

        # Hier wird die Animation initialisiert (Beispielhaft mit 6 Bildern und 48x48 Pixeln je Frame)
        # HINWEIS: Passt image_count und die Rect-Größe (48, 48) an euer Player_sprito.png an!
        self.animation = Sprite(filepath="Assets/Player_sprito.png", animationspeed=6, image_count=6,
                                image_rect=pygame.Rect(0, 0, 48, 48))
        self.animation.load_spritesheet()

    def get_rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def shoot(self):
        mx = self.x_pos + self.width / 2 - gv.BULLET_SIZE / 2
        my = self.y_pos - gv.BULLET_SIZE
        self.bullets.add_bullet(Bullet(self.screen, mx, my, 0, -7))

    def update_and_draw(self, frame_counter: int):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x_pos > 0:
            self.x_pos -= 2
        if keys[pygame.K_d] and self.x_pos < gv.SCREEN_WIDTH - self.width:
            self.x_pos += 2

        # Zeichnet den Spieler animiert anstatt des statischen Blits
        self.animation.draw(self.screen, self.x_pos, self.y_pos, self.width, self.height, frame_counter)
