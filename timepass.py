import pygame

WIDTH, HEIGHT = 900, 500
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')


# MAIN
def main():
    clock = pygame.time.Clock()
    run = True
    x = 10

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    rects =  pygame.Rect(0,0,x,HEIGHT)
                    x += 10

        # Draw
        def draw_window():
            WIN.fill('light blue')
            pygame.draw.rect(WIN, 'red', rects)
                
            pygame.display.update()

        draw_window()
        


if __name__ == '__main__':
    main()

pygame.quit()