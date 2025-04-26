import pygame
import constantes

pygame.init()

screen = pygame.display.set_mode((constantes.WIDTH,
                                  constantes.HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Lorem Ipsum')

run = True
while run:
    
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False

   pygame.display.update()

   screen.fill(constantes.SCREEN_COLOR)
   pygame.display.flip()

   clock.tick(60)

pygame.quit()

