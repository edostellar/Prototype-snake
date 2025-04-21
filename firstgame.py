import pygame
import constantes

pygame.init()

screen = pygame.display.set_mode((constantes.WIDTH,
                                  constantes.HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Lorem Ipsum')

running = True
while running:
    
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

   pygame.display.update()

   screen.fill("black")
   pygame.display.flip()

   clock.tick(60)

pygame.quit()

