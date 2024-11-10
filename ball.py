import pygame

class Ball:
    def __init__(self, radius, color, speed, center, win):
        self.radius = radius
        self.color = color
        self.speed = speed
        self.center = center
        self.win = win
    
    def draw(self):
        pygame.draw.circle(self.win, self.color, self.center, self.radius)
        pygame.draw.circle(self.win, "black", self.center, self.radius, 3)
    

    