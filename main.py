import pygame
from game_variables.GameVariables import GameVariables as gv
from game.player import Player
from game.bullet import Bullet
from game.target import Target


def main_screen():
    pygame.init()
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))
    pygame.display.set_caption("JahrmarktBumm")

    frame_counter = 0

    # # # KI Google Gemini Anfang
    # Fehler behoben: Objekt EINMAL vor der Schleife erstellen.
    # Variable klein schreiben, um Konflikt mit der Klasse 'Player' zu vermeiden.
    player_object = Player(screen)
    # # # KI Ende, Prompt: ich kann den Player nicht zeichnen sag mir was falsch ist

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
                    pass


            # Weitere Events abfragen (z.B. Tastatureingaben)

        # Update der Spiellogik

        # Neu zeichnen der Grafiken
        screen.fill("darkgray")
        player_object.update_and_draw(frame_counter)

        # Das Display updaten
        pygame.display.flip()
        clock.tick(gv.FPS)

    pygame.quit()


if __name__ == "__main__":
    main_screen()
