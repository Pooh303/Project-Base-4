import pygame
from fighter import Agent #import Agent from fighter
import button
from pygame import mixer

pygame.init()

#Mouse cursor
pygame.mouse.set_cursor(*pygame.cursors.tri_left)


#Screen setting
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
icon = pygame.image.load('assets/images/icon/fist.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BASE4")


clock = pygame.time.Clock()
FPS = 144 #fps


#Colors
RED = (255, 0 ,0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
TRANSPARENT = (0, 0, 0, 0)

#Player score [P1, P2]
score = [0, 0]
round_over = False
ROUND_OVER_COOLDOWN = 2000


#def fighter Player1
P1_SIZE = 162
P1_SCALE = 4
P1_OFFSET = [72, 56]
P1_DATA = [P1_SIZE, P1_SCALE, P1_OFFSET]
#def fighter Player2
P2_SIZE = 162
P2_SCALE = 4
P2_OFFSET = [72, 56]
P2_DATA = [P2_SIZE, P2_SCALE, P2_OFFSET]


#Load images
bg_image = pygame.image.load("assets/images/background/bgmix.jpg").convert_alpha() #background
start_img = pygame.image.load("assets/images/icon/buttons/play.png").convert_alpha() #button
start_img = pygame.transform.scale(start_img, (300,140))
resume_img = pygame.image.load("assets/images/icon/buttons/resume.png").convert_alpha() #button
resume_img = pygame.transform.scale(resume_img, (300,140))
quit_img = pygame.image.load("assets/images/icon/buttons/exit.png").convert_alpha() #button
quit_img = pygame.transform.scale(quit_img, (300,140))
main_img = pygame.image.load("assets/images/icon/buttons/mainmenu.png").convert_alpha() #button
main_img = pygame.transform.scale(main_img, (300,140))


#Create button instances
start_button = button.Button(520, 160, start_img, 1)
resume_button = button.Button(520, 160, resume_img, 1)
quit_button = button.Button(520, 380, quit_img, 1)
main_button = button.Button(520, 380, main_img, 1)


#Load spritesheets
player1_skin = pygame.image.load("assets/Characters/player_1/samurai.png").convert_alpha()
player2_skin = pygame.image.load("assets/Characters/player_2/spirit.png").convert_alpha()
# victory_img = pygame.image.load("assets/images/blank.png").convert_alpha()


#def number of steps in each animation
PLAYER1_ANIMATION_STEPS = [10, 8, 1, 4, 4, 4, 4]
PLAYER2_ANIMATION_STEPS = [8, 8, 1, 4, 4, 4, 6]


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


player_1 = Agent(1, 200, 340, False, P1_DATA, player1_skin, PLAYER1_ANIMATION_STEPS) #pos spawn agent1
player_2 = Agent(2, 1000, 340, True, P2_DATA, player2_skin, PLAYER2_ANIMATION_STEPS) #pos spawn agent2

game_start = True
menu_state = "start"
def intro_loop():
    mixer.music.load('assets/audio/background.wav') #เพลง
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05) #เปลี่ยนระเดับเสียงเพลง
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
    player_1 = Agent(1, 200, 340, False, P1_DATA, player1_skin, PLAYER1_ANIMATION_STEPS) #pos spawn agent1
    player_2 = Agent(2, 1000, 340, True, P2_DATA, player2_skin, PLAYER2_ANIMATION_STEPS) #pos spawn agent2
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
            draw_health_bar(player_1.health, 20, 20)
            draw_health_bar(player_2.health, 860, 20)
            draw_text("P1 : " + str(score[0]), score_font, RED, 20, 60)
            draw_text("P2 : " + str(score[1]), score_font, RED, 860, 60)
            

            if intro_count <= 0:
            #move agent
                player_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player_2, round_over)
                player_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player_1, round_over)
                
            # player_2.move(SCREEN_WIDTH, SCREEN_HEIGHT)
            else:
            #display count timer
                draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
            #update count timer
                if (pygame.time.get_ticks() - last_count_update) >= 1000:
                    intro_count -= 1
                    last_count_update = pygame.time.get_ticks()
            
            
            player_1.updateee()
            player_2.updateee()
            
            #draw fighters
            player_1.draw(screen)
            player_2.draw(screen)

            if round_over == False:
                if player_1.alive == False:
                    score[1] += 1
                    round_over = True
                    round_over_time = pygame.time.get_ticks()
                elif player_2.alive == False:
                    score[0] += 1
                    round_over = True
                    round_over_time = pygame.time.get_ticks()
            else:
                if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                    round_over = False
                    intro_count = 3
                    player_1 = Agent(1, 200, 340, False, P1_DATA, player1_skin, PLAYER1_ANIMATION_STEPS) #pos spawn agent1
                    player_2 = Agent(2, 1000, 340, True, P2_DATA, player2_skin, PLAYER2_ANIMATION_STEPS) #pos spawn agent2
                
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
