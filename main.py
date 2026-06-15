import pygame
import json
import os
from game_variables.GameVariables import GameVariables as gv
from game.player import Player
from game.bullet import Bullet, Bullets
from game.target import Target, Targets


# Ki Google Gemini Anfang
def load_highscores():
    if os.path.exists("highscores.json"):
        with open("highscores.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_highscore(new_score):
    scores = load_highscores()
    scores.append(new_score)
    scores.sort(reverse=True)
    with open("highscores.json", "w") as f:
        json.dump(scores[:5], f) # Nur Top 5 speichern
# Ki Ende, Prompt: Highscore Speicher-Logik hinzufügen


# Ki Google Gemini Anfang
def draw_menu(screen, title_text):
    screen.fill("black")

    # Titel (leicht nach links verschoben für Tabelle)
    font_title = pygame.font.SysFont("arial", 48)
    title_surface = font_title.render(title_text, True, "white")
    screen.blit(title_surface, (50, 100))

    # Start-Button (nach links verschoben)
    font_button = pygame.font.SysFont("arial", 32)
    button_text = font_button.render("Starten", True, "white")
    button_rect = pygame.Rect(100, 250, 140, 50)
    pygame.draw.rect(screen, "red", button_rect, 1)
    screen.blit(button_text, (button_rect.x + 20, button_rect.y + 5))

    # --- Highscore Tabelle auf der rechten Seite ---
    font_hs = pygame.font.SysFont("arial", 24)
    screen.blit(font_hs.render("Top 5 Highscores:", True, "yellow"), (gv.SCREEN_WIDTH - 240, 80))

    scores = load_highscores()
    for i, score in enumerate(scores):
        score_text = font_hs.render(f"{i + 1}. {score} Punkte", True, "white")
        screen.blit(score_text, (gv.SCREEN_WIDTH - 240, 120 + i * 30))

    return button_rect
# Ki Ende, Prompt: Menü mit Highscore-Anzeige erweitern


def main_screen():
    pygame.init()
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))
    pygame.display.set_caption("JahrmarktBumm")

    # Zustände
    game_state = "MENU"
    menu_title = "Jahrmarkt Bumm"
    frame_counter = 0
    score = 0

    bullets_manager = Bullets(screen)
    player_object = Player(screen, bullets_manager)
    targets_manager = Targets(screen)

    running = True
    clock = pygame.time.Clock()

    # Lokaler Platzhalter für den Button-Bereich im aktuellen Frame
    current_button_rect = pygame.Rect(0, 0, 0, 0)

    while running:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Events im MENÜ
            if game_state == "MENU":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if current_button_rect.collidepoint(event.pos):
                        game_state = "GAME"
                        frame_counter = 0

            # Events im SPIEL
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
                            score += 10  # Punkte vergeben!

            # Neu zeichnen der Spiel-Grafiken
            screen.fill("darkgray")
            player_object.update_and_draw(frame_counter)
            bullets_manager.update_and_draw()
            targets_manager.update_and_draw(frame_counter)

            # Ki Google Gemini Anfang
            # Timer prüfen (Jetzt auf 30 Sekunden geändert!)
            if frame_counter >= gv.FPS * 30:
                save_highscore(score)  # Score speichern
                score = 0  # Reset für nächstes Spiel
                frame_counter = 0  # Frame-Counter Reset
                game_state = "MENU"  # Zurück ins Menü

            # Timer & Punkte im Spiel oben links anzeigen (Auch hier auf 30s angepasst)
            font_ui = pygame.font.SysFont("arial", 20)
            remaining_time = max(0, 30 - (frame_counter // gv.FPS))
            ui_text = font_ui.render(f"Zeit: {remaining_time}s | Punkte: {score}", True, "white")
            screen.blit(ui_text, (10, 10))

            frame_counter += 1
            # Ki Ende, Prompt: 30s Timer-Prüfung und UI-Anzeige einbauen

        # Das Display aktualisieren
        pygame.display.flip()
        clock.tick(gv.FPS)

    pygame.quit()


if __name__ == "__main__":
    main_screen()