    
try:
    import pygame #inicia el programa
    import constantes #importa las varibles
    print("All Libraries imported successfully \n")
except :
    print("Error while importing modules and libraries")


pygame.init()

screen = pygame.display.set_mode((constantes.WIDTH, constantes.HEIGHT))
clock = pygame.time.Clock()

#Titulo del juego
pygame.display.set_caption('Snake Game Prototype')
pygame.display.set_icon(constantes.ICON)

def draw_grid():
    for x in range(0, constantes.WIDTH, constantes.BlockSize):
        for y in range(0, constantes.HEIGHT, constantes.BlockSize):
            rect = pygame.Rect(x, y, constantes.BlockSize, constantes.BlockSize)
            pygame.draw.rect(screen, constantes.WHITE, rect, 1)

run = True
while run:

    screen.blit(constantes.BG, [0, 0])
    draw_grid()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            pygame.display.update()
clock.tick(60)
pygame.quit()
print ("Exited with no errors")

