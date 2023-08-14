import pygame
import os
import random
pygame.font.init()

WIDTH, HEIGHT = 900, 500
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Singleplayer')

# Images
SINGLEPLAYER_BG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'singleplayer_bg.jpg')), (WIDTH, HEIGHT))
YELLOW_SPACESHIP = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png')), (60,40))
BULLET_IMG= pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Bullet1.png')), (10,10))
LASER_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'green_laser.png')), (10,10))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spaceship_red.png')), (60,40)), 180)
GREEN_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spaceship_green.png')), (60,40)), 180)
BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spaceship_blue.png')), (60,40)), 180)

# Fonts
FONT1 = pygame.font.Font((os.path.join('fonts', 'health.ttf')), 60)

class Ship:
    def __init__(self, x, y, health=100) -> None:
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_height(self):
         return self.ship_img.get_height()
    
    def get_width(self):
         return self.ship_img.get_width()

class Player(Ship):
    def __init__(self, x, y, health=100) -> None:
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACESHIP
        self.laser_img = LASER_IMG
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.bullet_img = BULLET_IMG

class Enemy(Ship):
    COLOR_MAP = {
            'red': (RED_SPACESHIP, BULLET_IMG),
            'blue': (BLUE_SPACESHIP, BULLET_IMG),
            'green': (GREEN_SPACESHIP, BULLET_IMG)
                }

    def __init__(self, x, y, color, health=100) -> None:
        super().__init__(x, y, health)
        self.ship_img , self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

def main():
    clock = pygame.time.Clock()
    run = True
    lives = 10
    level = 0
    player = Player(WIDTH//2 - 25, 400)
    player_vel = 10

    enemies = []
    wave_length = 6

    enemy_vel = 1
    bullets = []
    bullet_vel = 10

    while run:
        clock.tick(FPS)
        if len(enemies) == 0:
            level += 1
            if wave_length < 12:
                wave_length += 3
            else:
                wave_length = 12
                enemy_vel += 2
            for i in range(wave_length) or wave_length == 12:
                enemy = Enemy(random.randrange(50, WIDTH - 50), random.randrange(-900, -100), random.choice(['red', 'blue', 'green']))
                enemies.append(enemy)
                enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.get_width(), enemy.get_height())
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    bullet = pygame.Rect(player.x + player.get_width()//2, player.y, 5, 10)
                    bullets.append(bullet)

        # Display
        def set_display():
            WIN.fill('yellow')
            WIN.blit(SINGLEPLAYER_BG, (0,0))
            lives_text = FONT1.render(f'Lives: {lives}', 1, 'yellow')
            WIN.blit(lives_text, (0,0))
            level_text = FONT1.render(f'Level: {level}', 1, 'yellow')
            WIN.blit(level_text, (WIDTH - level_text.get_width(), 0))

            for enemy in enemies:
                enemy.draw(WIN)

            for bullet in bullets:
                WIN.blit(BULLET_IMG, (bullet.x, bullet.y))

            player.draw(WIN)


            pygame.display.update()

        # Movement
        def movement():
            get_pressed = pygame.key.get_pressed()
            if get_pressed[pygame.K_w] and player.y > 0:
                player.y -= player_vel
            if get_pressed[pygame.K_s] and player.y + player.get_height() < HEIGHT:
                player.y += player_vel
            if get_pressed[pygame.K_a] and player.x > 0:
                player.x -= player_vel
            if get_pressed[pygame.K_d] and player.x + player.get_width() + 5< WIDTH:
                player.x += player_vel

        # Bullet movement
        def move_bullet():
            for bullet in bullets:
                bullet.y -= bullet_vel
                if bullet.y == 0:
                    bullets.remove(bullet)
                if enemy_rect.colliderect(bullet):
                    pygame.QUIT


        for enemy in enemies:
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() == HEIGHT:
                enemies.remove(enemy)

        set_display()
        move_bullet()
        movement()

if __name__ == '__main__':
    main()

pygame.quit()
