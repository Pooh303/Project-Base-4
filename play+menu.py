import pygame
from fighter import Agent #import Agent from fighter
import button

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Project")


clock = pygame.time.Clock()
FPS = 144 #fps

RED = (255, 0 ,0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#load  images
bg_image = pygame.image.load("assets/images/background/bg.jpg").convert_alpha() #background
start_img = pygame.image.load("assets/images/button/play.png").convert_alpha()
start_img = pygame.transform.scale(start_img, (280, 110))
resume_img = pygame.image.load("assets/images/button/button_resume.png").convert_alpha()
options_img = pygame.image.load("assets/images/button/button_options.png").convert_alpha()
quit_img = pygame.image.load("assets/images/button/button_quit.png").convert_alpha()

#create button instances
start_button = button.Button(504, 125, start_img, 1)
resume_button = button.Button(504, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(536, 375, quit_img, 1)



def draw_bg():
    """draw BG"""
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))  #0,0 คือขนาดขอบ
    pygame.draw.line(screen, RED, (0, 520), (SCREEN_WIDTH, 520)) #โชว์พื้นสีเขียว
    

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


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
                    intro_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update() 

def game_loop():
    run = True
    intro_loop()
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
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused_loop()
                    pygame.display.update() 
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update() #update display
game_loop()

pygame.quit()
