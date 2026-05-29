import pygame
from game_variables.GameVariables import GameVariables as gv
from game.player import Player
from game.bullet import Bullet, Bullets
from game.target import Target, Targets


def draw_menu(screen, title_text):
    screen.fill("black")

    # Titel
    font_title = pygame.font.SysFont("arial", 64)
    title_surface = font_title.render(title_text, True, "white")
    title_rect = title_surface.get_rect(center=(gv.SCREEN_WIDTH // 2, 150))
    screen.blit(title_surface, title_rect)

    # Start-Button
    font_button = pygame.font.SysFont("arial", 32)
    button_text = font_button.render("Starten", True, "white")
    button_rect = pygame.Rect(0, 0, 120, 50)
    button_rect.center = (gv.SCREEN_WIDTH // 2, gv.SCREEN_HEIGHT // 2)

    pygame.draw.rect(screen, "red", button_rect, 1)
    screen.blit(button_text, (button_rect.x + 15, button_rect.y + 5))

    return button_rect


def main_screen():
    pygame.init()
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))
    pygame.display.set_caption("JahrmarktBumm")

    # Spiel-Zustände
    game_state = "MENU"
    menu_title = "Jahrmarkt Bumm"
    frame_counter = 0

    bullets_manager = Bullets(screen)
    player_object = Player(screen, bullets_manager)
    targets_manager = Targets(screen)

    running = True
    clock = pygame.time.Clock()

    # Lokaler Platzhalter für den Button-Bereich im aktuellen Frame <- KI
    current_button_rect = pygame.Rect(0, 0, 0, 0)

    while running:

        # EVENT HANDLING <- teils von KI (Punkte Makiert) und Space Shooter
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Events im MENÜ <- KI und Space Shooter
            if game_state == "MENU":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if current_button_rect.collidepoint(event.pos):
                        game_state = "GAME"
                        frame_counter = 0

            # Events im SPIEL <- KI und Space Shooter
            elif game_state == "GAME":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = "MENU"
                        menu_title = "Jahrmarkt Bumm"
                    if event.key == pygame.K_SPACE:
                        player_object.shoot()

        if game_state == "MENU":
            current_button_rect = draw_menu(screen, menu_title)

        elif game_state == "GAME":
            # Kollisionsabfrage
            for bullet in bullets_manager.bullets[:]:
                for target in targets_manager.targets[:]:
                    if bullet.get_rect().colliderect(target.get_rect()):
                        if bullet in bullets_manager.bullets:
                            bullets_manager.bullets.remove(bullet)
                        if target in targets_manager.targets:
                            targets_manager.targets.remove(target)

            # Neu zeichnen der Spiel-Grafiken
            screen.fill("darkgray")
            player_object.update_and_draw(frame_counter)
            bullets_manager.update_and_draw()
            targets_manager.update_and_draw(frame_counter)

            frame_counter += 1

        # Das Display aktualisieren
        pygame.display.flip()
        clock.tick(gv.FPS)

    pygame.quit()


if __name__ == "__main__":
    main_screen()
