import pygame

class Button:
    def __init__(self, x, y, image, win):
        self.sprite = pygame.image.load(image)
        self.rect = pygame.Rect(x, y, self.sprite.get_width(), self.sprite.get_height())
        self.win = win
        self.coordinates = x, y
        self.draw(win)

    def draw(self, win):
        win.blit(self.sprite, self.coordinates)

    def isClicked(self, pos):
        return self.rect.collidepoint(pos)