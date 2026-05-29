import pygame
from game_variables.GameVariables import GameVariables as gv
from game.player import Player
from game.bullet import Bullet, Bullets
from game.target import Target, Targets

#mainscreen
def main_screen():
    pygame.init()
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))
    pygame.display.set_caption("JahrmarktBumm")

    frame_counter = 0

    # KI Google Gemini Anfang
    # Fehler behoben: Bullets-Manager instanziiert und dem Player-Objekt übergeben
    bullets_manager = Bullets(screen)
    player_object = Player(screen, bullets_manager)
    # KI Ende, Prompt: Die bullet funktioniert nicht bitte sag mir was falsch ist
    targets_manager = Targets(screen)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    player_object.shoot()

        # Update der Spiellogik
        # KI Google Gemini Anfang
        # Logik hinzugefügt: Kollision Bullet mit Target
        for bullet in bullets_manager.bullets[:]:
            for target in targets_manager.targets[:]:
                if bullet.get_rect().colliderect(target.get_rect()):
                    if bullet in bullets_manager.bullets:
                        bullets_manager.bullets.remove(bullet)
                    if target in targets_manager.targets:
                        targets_manager.targets.remove(target)
        # KI Ende

        # Neu zeichnen der Grafiken
        screen.fill("darkgrey")
        player_object.update_and_draw(frame_counter)

        # KI Google Gemini Anfang
        # Logik hinzugefügt: Kugeln bewegen und auf dem Screen zeichnen
        bullets_manager.update_and_draw()
        # KI Ende, Prompt: Die bullet funktioniert nicht bitte sag mir was falsch ist

        targets_manager.update_and_draw(frame_counter)

        # KI Google Gemini Anfang
        # Fehler behoben
        frame_counter += 1
        # KI Ende, Prompt

        # Das Display updaten
        pygame.display.flip()
        clock.tick(gv.FPS)

    pygame.quit()


if __name__ == "__main__":
    main_screen()