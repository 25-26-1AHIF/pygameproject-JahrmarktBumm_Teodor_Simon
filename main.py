import pygame
from game_variables.GameVariables import GameVariables as gv


def start_screen(screen, title_text):
    screen.fill("black")
    font_title = pygame.font.SysFont("arial", 64)
    title_surface = font_title.render(title_text, True, "white")
    title_rect = title_surface.get_rect(center=(gv.SCREEN_WIDTH // 2, 150))
    screen.blit(title_surface, title_rect)

    font_button = pygame.font.SysFont("arial", 32)
    button_text = font_button.render("Starten", True, "white")
    button_rect = pygame.Rect(0, 0, 120, 50)
    button_rect.center = (gv.SCREEN_WIDTH // 2, gv.SCREEN_HEIGHT // 2)

    pygame.draw.rect(screen, "red", button_rect, 1)
    screen.blit(button_text, (button_rect.x + 15, button_rect.y + 5))


def main_screen():
    pygame.init()
    pygame.display.set_caption("JahrmarktBumm")
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))

    game_state = "MENU"
    menu_title = "JahrmarktBumm"

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if game_state == "MENU":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button_rect = pygame.Rect(gv.SCREEN_WIDTH // 2 - 60, gv.SCREEN_HEIGHT // 2 - 25, 120, 50)
                        if button_rect.collidepoint(mouse_pos):
                            game_state = "GAME"

                elif game_state == "GAME":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_state = "MENU"
                            menu_title = "WeltraumShooter"

            # Weitere Events abfragen (z.B. Tastatureingaben)

        # Update der Spiellogik

        # Neu zeichnen der Grafiken

        # Das Display updaten
        pygame.display.flip()
        clock.tick(gv.FPS)

    pygame.quit()


if __name__ == "__main__":
    pass