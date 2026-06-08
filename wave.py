import pygame
import numpy as np

pygame.init()

WIDTH = 1200
HEIGHT = 700

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Wave Superposition Simulator"
)

clock = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,100,255)
GREEN = (0,180,0)

time = 0

running = True

while running:

    screen.fill(WHITE)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    wave1_points = []
    wave2_points = []
    resultant_points = []

    for x in range(WIDTH):

        y1 = 80 * np.sin(
            0.02 * x - 0.05 * time
        )

        y2 = 80 * np.sin(
            0.02 * x + 0.05 * time
        )

        y_total = y1 + y2

        wave1_points.append(
            (x, int(150 + y1))
        )

        wave2_points.append(
            (x, int(350 + y2))
        )

        resultant_points.append(
            (x, int(550 + y_total))
        )

    pygame.draw.lines(
        screen,
        RED,
        False,
        wave1_points,
        2
    )

    pygame.draw.lines(
        screen,
        BLUE,
        False,
        wave2_points,
        2
    )

    pygame.draw.lines(
        screen,
        GREEN,
        False,
        resultant_points,
        3
    )

    font = pygame.font.SysFont(
        "Arial",
        24
    )

    screen.blit(
        font.render(
            "Wave 1",
            True,
            RED
        ),
        (20, 40)
    )

    screen.blit(
        font.render(
            "Wave 2",
            True,
            BLUE
        ),
        (20, 250)
    )

    screen.blit(
        font.render(
            "Resultant Wave",
            True,
            GREEN
        ),
        (20, 450)
    )

    time += 1

    pygame.display.update()

    clock.tick(60)

pygame.quit()
