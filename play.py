import pygame
from fighter import Agent #import Agent from fighter
# import menu

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Project")


clock = pygame.time.Clock()
FPS = 144 #fps

bg_image = pygame.image.load("assets/images/background/bg.jpg").convert_alpha() #background


def draw_bg():
    """draw BG"""
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))  #0,0 คือขนาดขอบ
    X=0; Y=520; width=1280; height=340
    pygame.draw.rect(screen, (51, 102, 0), (X, Y, width, height)) #โชว์พื้นสีเขียว


agent_1 = Agent(100, 340) #pos spawn agent1
agent_2 = Agent(800, 340) #pos spawn agent2

paused = False
run = True
while run:
    
    clock.tick(FPS)
    
    # key = pygame.key.get_pressed()
    draw_bg()
    
    #move agent
    agent_1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    # agent_2.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    agent_1.draw(screen)
    agent_2.draw(screen)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # if key[pygame.K_ESCAPE]:
    #     menu()
             #กดescแล้วเข้าหน้า menu 


    pygame.display.update() #update display

pygame.quit()
