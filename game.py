import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH,HEIGHT = 900, 500
PLAYER_WIDTH, PLAYER_HEIGHT = 50,50

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Mania')
logo = pygame.image.load(os.path.join('Assets', 'logo.ico'))
pygame.display.set_icon(logo)
FPS = 60
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
BG = pygame.mixer.Sound(os.path.join('Assets', 'background.mp3'))
bullet_sound = pygame.mixer.Sound(os.path.join('Assets', 'gun_sound1.mp3'))
winner_sound = pygame.mixer.Sound(os.path.join('Assets', 'win_music.mp3'))
hit_sound = pygame.mixer.Sound(os.path.join('Assets', 'hit.mp3'))


# Assets
RED_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT)), 90)
YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT)), 270)
BACKGROUND_IMG = pygame.image.load(os.path.join('Assets', 'space.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))
BAR_IMG = pygame.image.load(os.path.join('Assets', 'bar.jpg'))

# Main
def main():
    clock = pygame.time.Clock()
    run = True
    BG.play()
    pygame.mixer.music.set_volume(10)

    yellow_rect = pygame.Rect(WIDTH//4 - PLAYER_WIDTH//2 , HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDTH, PLAYER_HEIGHT)
    yellow_bullets = []
    red_rect = pygame.Rect(WIDTH - WIDTH//4 - PLAYER_WIDTH//2, HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDTH, PLAYER_HEIGHT)
    red_bullets = []
    RED_HEALTH = 10
    YELLOW_HEALTH = 10
    bar_rect = pygame.Rect(0,0,WIDTH, 40)

    while run:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
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

        def draw():
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



            pygame.display.update()

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
        draw()

    main()

if __name__ == '__main__':
    main()