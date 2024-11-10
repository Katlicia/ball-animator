import pygame
import random

class Ball:
    def __init__(self, radius, color, speed, center, win):
        self.radius = radius
        self.color = color
        self.speed = speed
        self.center = list(center)
        self.win = win

        self.dx = random.choice([-1, 1]) * self.speed
        self.dy = random.choice([-1, 1]) * self.speed
        
    
    def draw(self):
        pygame.draw.circle(self.win, self.color, self.center, self.radius)
        pygame.draw.circle(self.win, "black", self.center, self.radius, 3)
    
    def move(self, dt):
        # Update the position of the ball.
        self.center[0] += self.dx * dt
        self.center[1] += self.dy * dt

        if self.center[0] - self.radius <= 0 or self.center[0] + self.radius >= self.win.get_width():
            self.dx = -self.dx
        
        if self.center[1] - self.radius <= 0 or self.center[1] + self.radius >= 450:
            self.dy = -self.dy
    
    def updatespeed(self):
        # Update the speed of the ball.
        self.dx = (self.dx / abs(self.dx)) * self.speed
        self.dy = (self.dy / abs(self.dy)) * self.speed
 
    