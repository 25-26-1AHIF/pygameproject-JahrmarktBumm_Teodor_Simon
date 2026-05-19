import pygame

pygame.init()
pygame.display.set_caption("JahrmarktBumm")
screen = pygame.display.set_mode((640, 480))

running = True

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

# PyGame sauber beenden (cleanup)
pygame.quit()