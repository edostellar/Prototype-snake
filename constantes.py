import pygame

#TAMAÑO DE LA VENTANA
WIDTH = 1000
HEIGHT = 1000

#COLORES ESTABLECIDOS
WHITE = ( [200, 200, 200] )
YELLOW = ( [255, 255, 0] )
BLUE = ( [0, 0, 255] )
RED = ( [255, 0, 0] )
BLACK = ( [0, 0, 0] )
GREEN = ( [0, 255, 0] )

BlockSize = 50

#IMAGENES
ICON = pygame.image.load("Sprites/game_icon.png")
BG = pygame.image.load("Sprites/sky.png")
BG = pygame.transform.scale(BG, (1000, 1000))