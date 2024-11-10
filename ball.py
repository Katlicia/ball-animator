import pygame

class Ball:
    def __init__(self, radius, color, speed, center):
        self.radius = radius
        self.color = color
        self.speed = speed
        self.center = center

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.center, self.radius)
    

    