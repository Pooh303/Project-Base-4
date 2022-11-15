import pygame
from fighter import Agent #import Agent from fighter
import button

pygame.init()

#mouse cursor
pygame.mouse.set_cursor(*pygame.cursors.tri_left)

#screen setting
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
icon = pygame.image.load('assets/images/icon/fist2.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BASE4")


clock = pygame.time.Clock()
FPS = 144 #fps

#colors
RED = (255, 0 ,0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
TRANSPARENT = (0, 0, 0, 0) #fake png

#load  images
bg_image = pygame.image.load("assets/images/background/bgmix.jpg").convert_alpha() #background
start_img = pygame.image.load("assets/images/icon/buttons/play.png").convert_alpha()
start_img = pygame.transform.scale(start_img, (300,140))
resume_img = pygame.image.load("assets/images/icon/buttons/resume.png").convert_alpha()
resume_img = pygame.transform.scale(resume_img, (300,140))
# options_img = pygame.image.load("assets/images/button/button_options.png").convert_alpha()
quit_img = pygame.image.load("assets/images/icon/buttons/exit.png").convert_alpha()
quit_img = pygame.transform.scale(quit_img, (300,140))

#create button instances
start_button = button.Button(520, 160, start_img, 1)
resume_button = button.Button(520, 160, resume_img, 1)
# options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(520, 380, quit_img, 1)



def draw_bg():
    """draw BG"""
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))  #0,0 คือขนาดขอบ
    pygame.draw.line(screen, TRANSPARENT, (0, SCREEN_HEIGHT), (0, SCREEN_HEIGHT)) #โชว์พื้นสีเขียว
    # pygame.draw.line(screen, TRANSPARENT, (0, 520), (SCREEN_WIDTH, 520)) #โชว์พื้นสีเขียว (((อันเก่า)))

    

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30))


agent_1 = Agent(100, 340) #pos spawn agent1
agent_2 = Agent(800, 340) #pos spawn agent2

game_start = True
menu_state = "start"

def intro_loop():
    intro = True
    menu_state = "start"
    while intro:

        screen.fill((52, 78, 91))
        
        if game_start == True:
            if menu_state == "start":
                if start_button.draw(screen):
                    intro = False
                    game_loop()
                if quit_button.draw(screen):
                    pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        pygame.display.update() 

def paused_loop():
    intro = True
    menu_state = "resume"
    
    while intro:
        
        screen.fill((52, 78, 91))
        
        if game_start == True:
            if menu_state == "resume":
                if resume_button.draw(screen):
                    intro = False
                if quit_button.draw(screen):
                    intro = False
                    intro_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update() 

def game_loop():
    run = True
    paused = False
    while run:
        if not paused:
            pygame.mouse.set_visible(False)
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
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mouse.set_visible(True)
                        paused_loop()
                        pygame.display.update() 
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.display.update() #update display
        else:
            game_loop.update()
intro_loop()

pygame.quit()
