import pygame

class Agent():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.jump_count = 0

    def move(self, screen_width, screen_height):
        """move left right"""
        SPEED = 10
        GRAVITY = 0.5
        dx = 0
        dy = 0
        
        key = pygame.key.get_pressed()
        
        #move LR
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
        #jump
        if key[pygame.K_w] and self.jump == False:
            self.vel_y = -15
            self.jump = True
        
        self.vel_y += GRAVITY
        dy += self.vel_y
        
        
        
        # ไม่ให้เดินออกจอ
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 200:
            self.vel_y = 0
            self.jump = False
            self.jump_count = 0
            dy = screen_height - 200 - self.rect.bottom
        
        
        self.rect.x += dx
        self.rect.y += dy
    
    def draw(self, surface):
        pygame.draw.rect(surface, (100, 0, 0), self.rect)
