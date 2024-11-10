import pygame
import sys
import math
import random
from config import *
from ball import Ball
from button import Button

pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)

def DrawGui(ball_list, button_list):
    # Clear the screen.
    win.fill((255, 255, 255))
    
    # Balls
    pygame.draw.line(win, "black", LINE_START_POS, LINE_END_POS, LINE_WIDTH)
    pygame.draw.circle(win, "grey", SMALL_BALL_CENTER, SMALL_BALL_RADIUS)
    pygame.draw.circle(win, ("black"), SMALL_BALL_CENTER, SMALL_BALL_RADIUS, 3)
    pygame.draw.circle(win, "grey", MEDIUM_BALL_CENTER, MEDIUM_BALL_RADIUS)
    pygame.draw.circle(win,"black", MEDIUM_BALL_CENTER, MEDIUM_BALL_RADIUS, 3)
    pygame.draw.circle(win, "grey", LARGE_BALL_CENTER, LARGE_BALL_RADIUS)
    pygame.draw.circle(win, "black", LARGE_BALL_CENTER, LARGE_BALL_RADIUS, 3)

    # Colors
    pygame.draw.circle(win, "red", (SMALL_BALL_CENTER[0], 600), SMALL_BALL_RADIUS)
    pygame.draw.circle(win, "blue", (MEDIUM_BALL_CENTER[0], 600), SMALL_BALL_RADIUS)
    pygame.draw.circle(win, "yellow", (LARGE_BALL_CENTER[0], 600), SMALL_BALL_RADIUS)

    # Draw buttons.
    for button in button_list:
        button.draw()
    

    # Draw created balls.
    for ball in ball_list:
        ball.draw()
    
def IsBallClicked(ball_center, ball_radius, mouse_pos):
    distance = math.sqrt(pow((ball_center[0] - mouse_pos[0]), 2) + pow((ball_center[1] - mouse_pos[1]), 2))
    if distance <= ball_radius:
        return True
    else:
        return False

def main():
    run = True
    dt = 0
    FPS = 60
    clock = pygame.time.Clock()
    win.fill((255, 255, 255))

    color = "red"
    speed = 50
    ball_list = []
    button_list = []

    playbutton = Button(10, 480, "images/play.png", win)
    pausebutton = Button(10, 510, "images/pause.png", win)
    resetbutton = Button(10, 540, "images/reset.png", win)
    speedupbutton = Button(10, 570, "images/speedup.png", win)

    button_list.append(playbutton)
    button_list.append(pausebutton)
    button_list.append(resetbutton)
    button_list.append(speedupbutton)

    while run:
        dt = clock.tick(FPS) / 1000

        CREATED_SMALL_BALL_CENTER = (random.randint(SMALL_BALL_RADIUS, SCREEN_WIDTH - SMALL_BALL_RADIUS), random.randint(SMALL_BALL_RADIUS, 430))
        CREATED_MEDIUM_BALL_CENTER = (random.randint(MEDIUM_BALL_RADIUS, SCREEN_WIDTH - MEDIUM_BALL_RADIUS), random.randint(MEDIUM_BALL_RADIUS, 415))
        CREATED_LARGE_BALL_CENTER = (random.randint(LARGE_BALL_RADIUS, SCREEN_WIDTH - LARGE_BALL_RADIUS), random.randint(LARGE_BALL_RADIUS, 400))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if playbutton.isClicked(pos):
                    print("Clicked play.")

                elif pausebutton.isClicked(pos):
                    print("Clicked pause.")
                    
                elif resetbutton.isClicked(pos):
                    print("Clicked reset.")
                    ball_list.clear()

                elif speedupbutton.isClicked(pos):
                    print("Clicked speed up.")
                    speed *= 2

                elif IsBallClicked(SMALL_BALL_CENTER, SMALL_BALL_RADIUS, pos):
                    print("Clicked small ball.")                    
                    ball_list.append(Ball(SMALL_BALL_RADIUS, color, speed, CREATED_SMALL_BALL_CENTER, win))

                elif IsBallClicked(MEDIUM_BALL_CENTER, MEDIUM_BALL_RADIUS, pos):
                    print("Clicked medium ball.")
                    ball_list.append(Ball(MEDIUM_BALL_RADIUS, color, speed, CREATED_MEDIUM_BALL_CENTER, win))

                elif IsBallClicked(LARGE_BALL_CENTER, LARGE_BALL_RADIUS, pos):
                    print("Clicked large ball.")
                    ball_list.append(Ball(LARGE_BALL_RADIUS, color, speed, CREATED_LARGE_BALL_CENTER, win))

                elif IsBallClicked(RED_BALL_CENTER, SMALL_BALL_RADIUS, pos):
                    print("Clicked red ball.")
                    color = "red"

                elif IsBallClicked(BLUE_BALL_CENTER, SMALL_BALL_RADIUS, pos):
                    print("Clicked blue ball.")
                    color = "blue"

                elif IsBallClicked(YELLOW_BALL_CENTER, SMALL_BALL_RADIUS, pos):
                    print("Clicked yellow ball.")
                    color = "yellow"

        DrawGui(ball_list, button_list)
        pygame.display.update()


    
if __name__ == "__main__":
    main()