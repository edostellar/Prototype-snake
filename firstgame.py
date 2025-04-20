import pygame
import constantes
from player import Personaje

jugador = Personaje(250,50)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((constantes.WIDTH,
                                  constantes.HEIGHT))
pygame.display.set_caption('Lorem Ipsum')

running = True
while running:
    
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

   pygame.display.update()

   screen.fill("black")
   jugador.dibujar(screen)
   pygame.display.flip()

   clock.tick(60)

pygame.quit()

