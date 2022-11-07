import pygame

class Agent():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))

    def move(self):
        """move left right"""
        SPEED = 10
        dx = 0
        dy = 0
        
        key = pygame.key.get_pressed()
        
        #move LR
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
            
        self.rect.x += dx
        self.rect.y += dy
    
    def draw(self, surface):
        pygame.draw.rect(surface, (100, 0, 0), self.rect)
