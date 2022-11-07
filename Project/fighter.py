import pygame

class Agent():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))

    
    def draw(self, surface):
        pygame.draw.rect(surface, (100, 0, 0), self.rect)
