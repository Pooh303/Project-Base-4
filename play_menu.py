import pygame
from fighter import Agent #import Agent from fighter
import button
from pygame import mixer

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

score = [0, 0] #play score [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

#def fighter var
SAMURAI_SIZE = 162
SAMURAI_SCALE = 4
SAMURAI_OFFSET = [72, 56]
SAMURAI_DATA = [SAMURAI_SIZE, SAMURAI_SCALE, SAMURAI_OFFSET]
AGENT_SIZE = 162
AGENT_SCALE = 4
AGENT_OFFSET = [72, 56]
AGENT_DATA = [AGENT_SIZE, AGENT_SCALE, AGENT_OFFSET]

#load  images
bg_image = pygame.image.load("assets/images/background/bgmix.jpg").convert_alpha() #background
start_img = pygame.image.load("assets/images/icon/buttons/play.png").convert_alpha()
start_img = pygame.transform.scale(start_img, (300,140))
resume_img = pygame.image.load("assets/images/icon/buttons/resume.png").convert_alpha()
resume_img = pygame.transform.scale(resume_img, (300,140))
# options_img = pygame.image.load("assets/images/button/button_options.png").convert_alpha()
quit_img = pygame.image.load("assets/images/icon/buttons/exit.png").convert_alpha()
quit_img = pygame.transform.scale(quit_img, (300,140))
main_img = pygame.image.load("assets/images/icon/buttons/mainmenu.png").convert_alpha()
main_img = pygame.transform.scale(main_img, (300,140))

#create button instances
start_button = button.Button(520, 160, start_img, 1)
resume_button = button.Button(520, 160, resume_img, 1)
# options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(520, 380, quit_img, 1)
main_button = button.Button(520, 380, main_img, 1)


#load spritesheets
samurai_sheet = pygame.image.load("assets/Characters/char_1/samurai.png").convert_alpha()
agent_sheet = pygame.image.load("assets/Characters/char_1/spirit.png").convert_alpha()
victory_img = pygame.image.load("assets/images/hey.png").convert_alpha()

#def num of steps in each animation
SAMURAI_ANIMATION_STEPS = [10, 8, 1, 4, 4, 4, 4]
AGENT_ANIMATION_STEPS = [8, 8, 1, 4, 4, 4, 6]

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

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
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30))


agent_1 = Agent(1, 200, 340, False, SAMURAI_DATA, samurai_sheet, SAMURAI_ANIMATION_STEPS) #pos spawn agent1
agent_2 = Agent(2, 1000, 340, True, AGENT_DATA, agent_sheet, AGENT_ANIMATION_STEPS) #pos spawn agent2

game_start = True
menu_state = "start"
def intro_loop():
    mixer.music.load('background.wav')#เพลง
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)#เปลี่ยนระเดับเสียงเพลง
    intro = True
    menu_state = "start"
    while intro:
        
        screen.fill((52, 78, 91))
        
        if game_start == True:
            if menu_state == "start":
                if start_button.draw(screen):
                    mixer.music.stop()
                    score[0] = 0
                    score[1] = 0
                    game_loop()
                if quit_button.draw(screen):
                    pygame.quit()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update() 

def paused_loop():
    intropaused = True
    menu_state = "resume"
    
    while intropaused:
        
        screen.fill((52, 78, 91))
        
        if game_start == True:
            if menu_state == "resume":
                if resume_button.draw(screen):
                    intropaused = False
                if quit_button.draw(screen):
                    intropaused = False
                    pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update() 



count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

def game_loop():
    #นับเวลาถอยหลังก่อนเริ่มเกม
    intro_count = 0
    last_count_update = pygame.time.get_ticks()
    agent_1 = Agent(1, 200, 340, False, SAMURAI_DATA, samurai_sheet, SAMURAI_ANIMATION_STEPS) #pos spawn agent1
    agent_2 = Agent(2, 1000, 340, True, AGENT_DATA, agent_sheet, AGENT_ANIMATION_STEPS) #pos spawn agent2
    run = True
    paused = False
    #update countdown
    round_over = False
    while run:
        if not paused:
            pygame.mouse.set_visible(False)
            clock.tick(FPS)
            
            # key = pygame.key.get_pressed()
            draw_bg()
            
            #show health
            draw_health_bar(agent_1.health, 20, 20)
            draw_health_bar(agent_2.health, 860, 20)
            draw_text("P1 : " + str(score[0]), score_font, RED, 20, 60)
            draw_text("P2 : " + str(score[1]), score_font, RED, 860, 60)
            
            
            
            
            
            if intro_count <= 0:
            #move agent
                agent_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, agent_2, round_over)
                agent_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, agent_1, round_over)
                
            # agent_2.move(SCREEN_WIDTH, SCREEN_HEIGHT)
            else:
            #display count timer
                draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
            #update count timer
                if (pygame.time.get_ticks() - last_count_update) >= 1000:
                    intro_count -= 1
                    last_count_update = pygame.time.get_ticks()
            
            
            agent_1.updateee()
            agent_2.updateee()
            
            #draw fighters
            agent_1.draw(screen)
            agent_2.draw(screen)

            if round_over == False:
                if agent_1.alive == False:
                    score[1] += 1
                    hurt_Sound = mixer.Sound('male_hurt.wav')
                    hurt_Sound.play(0)
                    hurt_Sound.set_volume(0.2)
                    round_over = True
                    round_over_time = pygame.time.get_ticks()
                elif agent_2.alive == False:
                    score[0] += 1
                    hurt_Sound = mixer.Sound('male_hurt.wav')
                    hurt_Sound.play(0)
                    hurt_Sound.set_volume(0.2)
                    round_over = True
                    round_over_time = pygame.time.get_ticks()
            else:
                if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                    round_over = False
                    intro_count = 3
                    agent_1 = Agent(1, 200, 340, False, SAMURAI_DATA, samurai_sheet, SAMURAI_ANIMATION_STEPS) #pos spawn agent1
                    agent_2 = Agent(2, 1000, 340, True, AGENT_DATA, agent_sheet, AGENT_ANIMATION_STEPS) #pos spawn agent2
                
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
