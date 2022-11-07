import pygame
from fighter import Agent #import Agent from fighter

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Project")

bg_image = pygame.image.load("assets/images/background/bg.jpg").convert_alpha() #background


def draw_bg():
    """draw BG"""
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))  #0,0 คือขนาดขอบ


agent_1 = Agent(100, 300) #pos spawn agent1
agent_2 = Agent(800, 300) #pos spawn agent2


run = True
while run:
    
    draw_bg()
    
    agent_1.draw(screen)
    agent_2.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update() #update display

pygame.quit()
