import pygame
import constantes

pygame.init()

screen = pygame.display.set_mode((constantes.WIDTH, constantes.HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Lorem Ipsum')

bg_img = pygame.image.load('img/sky.png')

def draw_grid():
    for x in range(0, constantes.WIDTH, constantes.BlockSize):
        for y in range(0, constantes.HEIGHT, constantes.BlockSize):
            rect = pygame.Rect(x, y, constantes.BlockSize)
            pygame.draw.rect(screen, constantes.WHITE, rect, 1)

run = True
while run:
    
    screen.blit(bg_img, (0, 0))
    screen.fill((0, 0, 0))  # Fill the background to clear the previous frame
    draw_grid()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
clock.tick(60)
pygame.quit()

