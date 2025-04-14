import pygame
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Lorem Ipsum')
pygame.display.get_icon()

running = True

while running:
    
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

screen.fill("blue")

pygame.display.flip()

clock.tick(60)

pygame.quit()

