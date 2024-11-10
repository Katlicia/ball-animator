import pygame
import sys
from config import *
from ball import Ball
from button import Button

pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)

def DrawGui():
    win.fill((255, 255, 255))
    # Draw gui elements.

    # Balls
    pygame.draw.line(win, "black", LINE_START_POS, LINE_END_POS, LINE_WIDTH)
    pygame.draw.circle(win, "grey", SMALL_BALL_CENTER, SMALL_BALL_RADIUS)
    pygame.draw.circle(win, ("black"), SMALL_BALL_CENTER, SMALL_BALL_RADIUS, 3)
    pygame.draw.circle(win, "grey", MEDIUM_BALL_CENTER, MEDIUM_BALL_RADIUS)
    pygame.draw.circle(win,"black", MEDIUM_BALL_CENTER, MEDIUM_BALL_RADIUS, 3)
    pygame.draw.circle(win, "grey", LARGE_BALL_CENTER, LARGE_BALL_RADIUS)
    pygame.draw.circle(win, "black", LARGE_BALL_CENTER, LARGE_BALL_RADIUS, 3)

    # Buttons
    playbutton = Button(10, 480, "images/play.png", win)
    pausebutton = Button(10, 510, "images/pause.png", win)
    resetbutton = Button(10, 540, "images/reset.png", win)
    speedupbutton = Button(10, 570, "images/speedup.png", win)

    # Colors
    pygame.draw.circle(win, "red", (SMALL_BALL_CENTER[0], 600), SMALL_BALL_RADIUS)
    pygame.draw.circle(win, "blue", (MEDIUM_BALL_CENTER[0], 600), SMALL_BALL_RADIUS)
    pygame.draw.circle(win, "yellow", (LARGE_BALL_CENTER[0], 600), SMALL_BALL_RADIUS)
    


def main():
    run = True
    dt = 0
    FPS = 60
    clock = pygame.time.Clock()
    while run:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        DrawGui()
        pygame.display.update()

if __name__ == "__main__":
    main()