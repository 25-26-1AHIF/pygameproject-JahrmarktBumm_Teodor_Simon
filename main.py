import pygame
import json
import os
from game_variables.GameVariables import GameVariables as gv
from game.player import Player
from game.bullet import Bullet, Bullets
from game.target import Target, Targets


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
        json.dump(scores[:5], f)


def draw_menu(screen, title_text):
    screen.fill("black")

    font_title = pygame.font.SysFont("arial", 48)
    title_surface = font_title.render(title_text, True, "white")
    screen.blit(title_surface, (50, 100))

    font_button = pygame.font.SysFont("arial", 32)
    button_text = font_button.render("Starten", True, "white")
    button_rect = pygame.Rect(50, 200, 150, 50)

    pygame.draw.rect(screen, "red", button_rect, 2)
    screen.blit(button_text, (button_rect.x + 25, button_rect.y + 5))

    font_scores = pygame.font.SysFont("arial", 24)
    scores_title = font_scores.render("Top 5 Highscores:", True, "yellow")
    screen.blit(scores_title, (400, 100))

    highscores = load_highscores()
    for i, s in enumerate(highscores):
        score_text = font_scores.render(f"{i+1}. {s} Punkte", True, "white")
        screen.blit(score_text, (400, 140 + i * 30))

    return button_rect


# Ki Google Gemini Anfang
def main_screen():
    pygame.init()
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    game_state = "MENU"
    menu_title = "Jahrmarkt Bumm"

    bullets_manager = Bullets(screen)
    player = Player(screen, bullets_manager)
    targets_manager = Targets(screen)

    score = 0
    bullets_left = 10
    frame_counter = 0

    background_image = pygame.image.load("Assets/background.png").convert()
    background_image = pygame.transform.scale(background_image, (gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))

    # HIER GEÄNDERT: button_rect VOR der Schleife definieren, damit es nie None ist!
    button_rect = pygame.Rect(0, 0, 0, 0)

    running = True
    while running:
        clock.tick(gv.FPS)

        # Wenn wir im Menü sind, zeichnen wir es und holen uns die echten Button-Koordinaten
        if game_state == "MENU":
            button_rect = draw_menu(screen, menu_title)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == "MENU":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Das funktioniert jetzt fehlerfrei, da button_rect immer existiert
                    if button_rect.collidepoint(event.pos):
                        game_state = "GAME"
                        score = 0
                        bullets_left = 10
                        frame_counter = 0
                        bullets_manager.bullets.clear()
                        targets_manager.targets.clear()

            elif game_state == "GAME":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = "MENU"
                        menu_title = "Jahrmarkt Bumm"
                    elif event.key == pygame.K_SPACE:
                        if bullets_left > 0:
                            player.shoot()
                            bullets_left -= 1

        if game_state == "GAME":
            screen.blit(background_image, (0, 0))
            frame_counter += 1

            player.update_and_draw(frame_counter)
            targets_manager.update_and_draw(frame_counter)
            bullets_manager.update_and_draw()

            for b in bullets_manager.bullets[:]:
                for t in targets_manager.targets[:]:
                    if b.get_rect().colliderect(t.get_rect()):
                        score += 10
                        bullets_manager.bullets.remove(b)
                        targets_manager.targets.remove(t)
                        break

            if frame_counter >= gv.FPS * 15 or (bullets_left == 0 and len(bullets_manager.bullets) == 0):
                if score > 0:
                    save_highscore(score)
                game_state = "MENU"
                frame_counter = 0

            font_ui = pygame.font.SysFont("arial", 20)
            ammo_text = font_ui.render(f"Schüsse: {bullets_left}", True, "white")
            screen.blit(ammo_text, (10, 10))

            remaining_time = max(0, 15 - (frame_counter // gv.FPS))
            time_text = font_ui.render(f"Zeit: {remaining_time}s", True, "white")
            time_rect = time_text.get_rect(center=(gv.SCREEN_WIDTH // 2, 20))
            screen.blit(time_text, time_rect)

            score_text = font_ui.render(f"Punkte: {score}", True, "white")
            score_rect = score_text.get_rect(topright=(gv.SCREEN_WIDTH - 10, 10))
            screen.blit(score_text, score_rect)

        pygame.display.flip()

    pygame.quit()
# Ki Ende, Prompt: [Image_9d1d27.png / Fehlermeldung]


if __name__ == "__main__":
    main_screen()
