import pygame
from fighter import Agent #import Agent from fighter


pygame.init()

# screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Base4")


clock = pygame.time.Clock()
FPS = 144 #fps

RED = (255, 0 ,0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
TRANSPARENT = (0, 0, 0, 0)

bg_image = pygame.image.load("assets/images/background/bg.jpg").convert_alpha() #background


def draw_bg():
    """draw BG"""
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))  #0,0 คือขนาดขอบ
    pygame.draw.line(screen, TRANSPARENT, (0, 520), (SCREEN_WIDTH, 520)) #โชว์พื้นสีเขียว


def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30))


agent_1 = Agent(100, 340) #ตำแหน่งเกิดของ agent1
agent_2 = Agent(800, 340) #ตำแหน่งเกิดของ agent2

paused = False
run = True
while run:
    
    
    clock.tick(FPS)
    
    # key = pygame.key.get_pressed()
    draw_bg()
    
    #show health
    draw_health_bar(agent_1.health, 20, 20)
    draw_health_bar(agent_2.health, 860, 20)
    
    #move agent
    agent_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, agent_2)
    # agent_2.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    agent_1.draw(screen)
    agent_2.draw(screen)
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
            import menu #ต้องการให้ไปหน้า resume ยังไม่เสร็จ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update() #update display

pygame.quit()
