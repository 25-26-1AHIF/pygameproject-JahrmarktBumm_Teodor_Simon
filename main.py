import pygame
from game_variables.GameVariables import GameVariables as gv

def main_screen():
    pygame.init()
    pygame.display.set_caption("JahrmarktBumm")
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            # Weitere Events abfragen (z.B. Tastatureingaben)

        # Update der Spiellogik

        # Neu zeichnen der Grafiken

        # Das Display updaten
        pygame.display.flip()
        clock.tick(gv.FPS)

    pygame.quit()


if __name__ == "__main__":
    pass