import pygame
import os
import button
import sys
pygame.font.init()
pygame.mixer.init()

# Variables
WIDTH,HEIGHT = 900, 500
FPS = 60
MAIN_TITLE_FONT = pygame.font.Font(os.path.join('fonts', 'title.ttf'), 100)
NORMAL_FONT = pygame.font.Font(os.path.join('fonts', 'health.ttf'), 30)

# Colors
GREEN = (0,255,0)
DARK_BROWN = (98,52,18)
RUBY = (155, 17, 30)

# Display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load(os.path.join('Assets', 'logo.ico'))
pygame.display.set_icon(icon)

# Images
main_menu_bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'home_background.jpg')), (WIDTH, HEIGHT))
play_button_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'play.png')), (100, 70))
back_button_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'back.png')), (50,50))
i_button = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'i_button.png')), (50,50))
dev_img = pygame.image.load(os.path.join('Assets', 'dev.png'))
dev = pygame.transform.scale(dev_img, (400, 500))
dev_rect = pygame.Rect(WIDTH - dev.get_width() + 120, 0, dev.get_width(), dev.get_height())
about_line = pygame.Rect(WIDTH - dev.get_width() + 110, 0, 10, HEIGHT)
instagram = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'instagram.png')), (50,50))
gmail = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'gmail.png')), (50,40))
singleplayer_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'singleplayer.png')), (250, 80))
multiplayer_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'multiplayer.png')), (250, 80))
rocket_img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'rocket.png')), (250, 300)), 90)
gamemode_bg = pygame.image.load(os.path.join('Assets', 'gamemode_bg.jpg'))
yes_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'yes.png')), (150, 70))
no_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'no.png')), (150, 70))

# Sounds
play_click = pygame.mixer.Sound(os.path.join('Assets', 'play_click.wav'))
back_click = pygame.mixer.Sound(os.path.join('Assets', 'back_click.wav'))
main_bg_music = pygame.mixer.Sound(os.path.join('Assets', 'main_menu.mp3'))
BG = pygame.mixer.Sound(os.path.join('Assets', 'background.mp3'))
BG.set_volume(0.01)

 # About
about = NORMAL_FONT.render('i', 1, 'brown')

# Create Button
play_button = button.Button(WIDTH//2 - play_button_img.get_width()//2, HEIGHT//2 - play_button_img.get_height()//2, play_button_img)
back_button = button.Button(0, 0, back_button_img)
about_button = button.Button(WIDTH - i_button.get_width(), HEIGHT - i_button.get_height(), i_button)
singleplayer_button = button.Button(100, 170, singleplayer_img)
multiplayer_button = button.Button(100, 200 + singleplayer_img.get_height() + 10, multiplayer_img)
yes_button = button.Button(450 - yes_img.get_width()//2, 200, yes_img)
no_button = button.Button(450 - no_img.get_width()//2, 200 + yes_img.get_height() + 12, no_img)

# Draw Window
def draw():
    WIN.fill(GREEN)

    # Main BG
    WIN.blit(main_menu_bg, (0,0))

    # Main Title
    title = MAIN_TITLE_FONT.render('SPACE MANIA', 1, 'gold')
    WIN.blit(title, (WIDTH//2 - title.get_width()//2 , HEIGHT//4 - title.get_height()//2 ))

    # About
    about = NORMAL_FONT.render('i', 1, 'brown')
    WIN.blit(about, (about_button.x, about_button.y))

# Pressing singleplayer
def play_single_player():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        WIN.fill('yellow')
        pygame.display.set_caption('Singleplayer')

        comming_soon = MAIN_TITLE_FONT.render('Comming Soon', 1, RUBY)
        WIN.blit(comming_soon, (WIDTH//2 - comming_soon.get_width()//2, HEIGHT//2 - comming_soon.get_height()//2))

        #Back
        if back_button.draw(WIN):
                back_click.play()
                main_bg_music.play()
                play_getpressed()

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                confirm_exit(play_single_player)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    back_click.play()
                    main_bg_music.play()
                    play_getpressed()

        pygame.display.update()

# Pressing local multiplayer
def play_local_multiplayer():
    PLAYER_WIDTH, PLAYER_HEIGHT = 50,50

    # Assets
    RED_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
    RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT)), 90)
    YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
    YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT)), 270)
    BACKGROUND_IMG = pygame.image.load(os.path.join('Assets', 'space.png'))
    BACKGROUND = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))
    BAR_IMG = pygame.image.load(os.path.join('Assets', 'bar.jpg'))

    # Variables
    GREEN = (0,255,0)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)
    RUBY = (224, 17, 95)
    GOLD = (255, 215, 0)
    VEL = 7
    BULLET_VEL = 10
    MAX_BULLETS = 3
    RED_HIT = pygame.USEREVENT + 1
    YELLOW_HIT = pygame.USEREVENT + 2
    MAIN_FONT = pygame.font.Font(os.path.join('fonts', 'health.ttf'), 35)
    WINNER_FONT = pygame.font.Font(os.path.join('fonts', 'title.ttf'), 100)
    TITLE_FONT = pygame.font.Font(os.path.join('fonts', 'title.ttf'), 50)

    # TRACKS
    bullet_sound = pygame.mixer.Sound(os.path.join('Assets', 'gun_sound1.mp3'))
    winner_sound = pygame.mixer.Sound(os.path.join('Assets', 'win_music.mp3'))
    hit_sound = pygame.mixer.Sound(os.path.join('Assets', 'hit.mp3'))

    def fill():
        WIN.fill(GREEN)

        WIN.blit(BACKGROUND, (0,0))

        middleline_rect = pygame.Rect(WIDTH//2 - 2.5, 0, 5, HEIGHT)
        pygame.draw.rect(WIN, BLACK, middleline_rect)
        pygame.draw.rect(WIN, BLACK, bar_rect)

        for bullet in yellow_bullets:
            pygame.draw.rect(WIN, YELLOW, bullet)
        for bullet in red_bullets:
            pygame.draw.rect(WIN, RED, bullet)

        red_health_text = MAIN_FONT.render(f'HEALTH: {RED_HEALTH}', 1, RUBY)
        WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 5, 5))

        yellow_health_text = MAIN_FONT.render(f'HEALTH: {YELLOW_HEALTH}', 1, YELLOW)
        WIN.blit(yellow_health_text, (5,5))

        title_font = TITLE_FONT.render(f'SPACE MANIA', 1, GOLD, BLACK)
        WIN.blit(title_font, (WIDTH//2 - title_font.get_width()//2, 0))

        WIN.blit(YELLOW_SPACESHIP, (yellow_rect.x, yellow_rect.y))
        WIN.blit(RED_SPACESHIP, (red_rect.x, red_rect.y))


    # Main
    clock = pygame.time.Clock()
    run = True
    yellow_rect = pygame.Rect(WIDTH//4 - PLAYER_WIDTH//2 , HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDTH, PLAYER_HEIGHT)
    yellow_bullets = []
    red_rect = pygame.Rect(WIDTH - WIDTH//4 - PLAYER_WIDTH//2, HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDTH, PLAYER_HEIGHT)
    red_bullets = []
    RED_HEALTH = 10
    YELLOW_HEALTH = 10
    bar_rect = pygame.Rect(0,0,WIDTH, 40)

    while run:
        clock.tick(FPS)
        pygame.display.set_caption('Multiplayer')

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                confirm_exit(play_local_multiplayer)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    BG.stop()
                    back_click.play()
                    main_bg_music.play()
                    play_getpressed()
                if event.key == pygame.K_q and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow_rect.x + 23, yellow_rect.y + 22, 15, 5)
                    yellow_bullets.append(bullet)
                    bullet_sound.play()
                if event.key == pygame.K_o and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red_rect.x, red_rect.y + 25, 15, 5)
                    red_bullets.append(bullet)
                    bullet_sound.play()
                
            if event.type == RED_HIT:
                    RED_HEALTH -= 1
                    hit_sound.play()
            if event.type == YELLOW_HIT:
                    YELLOW_HEALTH -= 1
                    hit_sound.play()

        def player_moment():
                key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_w] and yellow_rect.y > 5:
                    yellow_rect.y -= VEL
                if key_pressed[pygame.K_s] and yellow_rect.y < HEIGHT - PLAYER_HEIGHT - 5:
                    yellow_rect.y += VEL
                if key_pressed[pygame.K_a] and yellow_rect.x > 5:
                    yellow_rect.x -= VEL
                if key_pressed[pygame.K_d] and yellow_rect.x < WIDTH//2 -PLAYER_WIDTH -2.5:
                    yellow_rect.x += VEL

                if key_pressed[pygame.K_i] and red_rect.y > 5:
                    red_rect.y -= VEL
                if key_pressed[pygame.K_k] and red_rect.y < HEIGHT - PLAYER_HEIGHT - 5:
                    red_rect.y += VEL
                if key_pressed[pygame.K_j] and red_rect.x > WIDTH//2 +5:
                    red_rect.x -= VEL
                if key_pressed[pygame.K_l] and red_rect.x + PLAYER_WIDTH < WIDTH -4:
                    red_rect.x += VEL

        def bullet_moment():
            for bullet in yellow_bullets:
                bullet.x += BULLET_VEL
                if bullet.x + 15 >= WIDTH:
                    yellow_bullets.remove(bullet)
                if red_rect.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(RED_HIT))
                    yellow_bullets.remove(bullet)

            for bullet in red_bullets:
                bullet.x -= BULLET_VEL
                if bullet.x <= 0:
                    red_bullets.remove(bullet)
                if yellow_rect.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(YELLOW_HIT))
                    red_bullets.remove(bullet)

        def draw_winner(text, COLOR):
            winner_sound.play()
            win_text = WINNER_FONT.render(text, 1, COLOR)
            WIN.blit(win_text, (WIDTH//2- win_text.get_width()//2, HEIGHT//2 - win_text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)

        winner_text = ''
        if RED_HEALTH == 0:
            winner_text = "Yellow Wins!!"
            COLOR = YELLOW
        if YELLOW_HEALTH == 0:
            winner_text = "Red Wins!!"
            COLOR = RUBY

        if winner_text != '':
            draw_winner(winner_text, COLOR)
            break

        player_moment()
        bullet_moment()
        fill()

        #Back
        ##if back_button.draw(WIN):
                #BG.stop()
                #back_click.play()
                #run = False
                #play_getpressed()
                #exit()

        pygame.display.update()
        
    play_local_multiplayer()

# Pressing play
def play_getpressed():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        WIN.fill('yellow')
        WIN.blit(gamemode_bg, (30, 130))
        menu_border = pygame.Rect(30, 120, 405, 310)
        pygame.display.set_caption('Game mode')
        pygame.draw.rect(WIN, 'black', menu_border, 10)
        game_mode = MAIN_TITLE_FONT.render('Game Mode', 1, RUBY)
        WIN.blit(game_mode, (WIDTH//2 - game_mode.get_width()//2, 0))
        WIN.blit(rocket_img, (500, 130))

        #Back
        if back_button.draw(WIN):
                main_bg_music.stop()
                back_click.play()
                main()

        if singleplayer_button.draw(WIN):
            main_bg_music.stop()
            play_click.play()
            play_single_player()

        if multiplayer_button.draw(WIN):
            main_bg_music.stop()
            play_click.play()
            BG.play()
            play_local_multiplayer()

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                confirm_exit(play_getpressed)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_bg_music.stop()
                    back_click.play()
                    main()

        pygame.display.update()

# Pressing about
def  about_getpressed():
    clock = pygame.time.Clock()
    run = True

    def fill():
        WIN.fill('yellow')
        WIN.fill('brown', dev_rect)
        WIN.fill('black', about_line)
        WIN.blit(dev, (WIDTH - dev.get_width(), 0))

        # About info
        about_title = MAIN_TITLE_FONT.render('About', 1, 'dark red')
        WIN.blit(about_title, (60, 0))
        name = NORMAL_FONT.render('Made by ', 1, 'black')
        WIN.blit(name, (50, 100))
        name_ = NORMAL_FONT.render('SWESHIK REDDY', 1, 'brown')
        WIN.blit(name_, (50 + name.get_width(), 100))
        version = NORMAL_FONT.render('Version - ', 1, 'black')
        WIN.blit(version, (50, 100 + name.get_height()))
        version_ = NORMAL_FONT.render('1.0.0 (Beta)', 1, 'brown')
        WIN.blit(version_, (50 + version.get_width(),100 + name.get_height()))
        WIN.blit(instagram, (50, HEIGHT - instagram.get_height() - 20))
        instagram_info = NORMAL_FONT.render('instagram.com/sweshik_red_e', 1, 'black')
        WIN.blit(instagram_info, (55 + instagram.get_width(), HEIGHT - instagram.get_height() - 25 + instagram_info.get_height()//2))
        WIN.blit(gmail, (50, HEIGHT - instagram.get_height() - 20 - gmail.get_height()))
        gmail_info = NORMAL_FONT.render('vagalamsweshikreddy@gmail.com', 1, 'black')
        WIN.blit(gmail_info, (55 + gmail.get_width(), HEIGHT - instagram.get_height() - 20 - gmail.get_height() + 5))

        next_version = NORMAL_FONT.render('Upcomming Features in V-2.0.0 (Beta)', 1, 'black')
        next_version_info1 = NORMAL_FONT.render("- Power Up's ", 1, 'brown')
        next_version_info2 = NORMAL_FONT.render("- Singleplayer Gamemode ", 1, 'brown')
        next_version_info3 = NORMAL_FONT.render("- Changeable Space Ships ... ", 1, 'brown')
        WIN.blit(next_version, (50, 120 + name.get_height() + version.get_height()))
        WIN.blit(next_version_info1, (50, 120 + name.get_height() + version.get_height() + next_version.get_height()))
        WIN.blit(next_version_info2, (50, 120 + name.get_height() + version.get_height() + next_version.get_height() + next_version_info1.get_height()))
        WIN.blit(next_version_info3, (50, 120 + name.get_height() + version.get_height() + next_version.get_height() + next_version_info1.get_height() + next_version_info2.get_height()))

    while run:
        clock.tick(FPS)
        fill()
        pygame.display.set_caption('About')

        #Back
        if back_button.draw(WIN):
                main_bg_music.stop()
                back_click.play()
                run = False
                main()

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                confirm_exit(about_getpressed)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_bg_music.stop()
                    back_click.play()
                    run = False
                    main()

        pygame.display.update()

#Confirm exit menu
def confirm_exit_menu():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        exit_menu = pygame.Rect(WIDTH//4 - 70, HEIGHT//4 - 50, 600, 330)
        pygame.draw.rect(WIN, (0, 15, 43), exit_menu)
        pygame.draw.rect(WIN, 'yellow', exit_menu, 10)

        exit_text = MAIN_TITLE_FONT.render('Exit', 1, 'gold')
        WIN.blit(exit_text, (WIDTH//2 - exit_text.get_width()//2, HEIGHT//4 - 45))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_bg_music.stop()
                    back_click.play()
                    main()
                    

        if yes_button.draw(WIN):
            back_click.play()
            sys.exit()

        if no_button.draw(WIN):
            back_click.play()
            main()

        pygame.display.update()

#Confirm exit
def confirm_exit(place):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        exit_menu = pygame.Rect(WIDTH//4 - 70, HEIGHT//4 - 50, 600, 330)
        pygame.draw.rect(WIN, (0, 15, 43), exit_menu)
        pygame.draw.rect(WIN, 'black', exit_menu, 10)

        exit_text = MAIN_TITLE_FONT.render('Exit', 1, 'gold')
        WIN.blit(exit_text, (WIDTH//2 - exit_text.get_width()//2, HEIGHT//4 - 45))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_bg_music.stop()
                    back_click.play()
                    place()
                    

        if yes_button.draw(WIN):
            back_click.play()
            sys.exit()

        if no_button.draw(WIN):
            back_click.play()
            place()

        pygame.display.update()


# Main
def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        pygame.display.set_caption('Space Mania')
        main_bg_music.play()
        main_bg_music.set_volume(0.01)
        clock.tick(FPS)
        draw()


        # Start button
        if play_button.draw(WIN):
            main_bg_music.stop()
            play_click.play()
            main_bg_music.play()
            play_getpressed()

        # About button
        if about_button.draw(WIN):
            main_bg_music.stop()
            play_click.play()
            main_bg_music.play()
            about_getpressed()

        # Events
        ## Close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                confirm_exit_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_bg_music.stop()
                    back_click.play()
                    confirm_exit_menu()
                    run = False


        pygame.display.update()
if __name__ == '__main__':
    main()

pygame.quit()