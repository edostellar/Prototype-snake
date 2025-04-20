import pygame
import constantes

class Personaje():
    def __init__(self, x, y):
        pass
        self.shape = pygame.rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.shape.center = (x, y)

def dibujar(self, screen):
    pygame.draw.rect (screen, constantes.COLOR_PERSONAJE, self.shape)