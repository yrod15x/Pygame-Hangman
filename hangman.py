#Programa que simula el juego del ahorcado. 

import pygame, sys
from funciones import *

pygame.init()

FPS = 60
fpsclock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
BLANCO = (255, 255, 255)
COLOR = (12, 67, 125)
FOND_TEXTO = (125, 65, 12)

ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HANGMAN")

letras = cargar_imagenes()
padding = 75
padding_top = 50
top_limit = 260

while True:
    ventana.fill(BLANCO)
    #padding lo multiplo por i para que vaya espaciando la letras hacia la derecha
    for i in range(26):
        #Cada if representa una linea del teclado
        if i < 7:
            ventana.blit(letras[i], ((WIDTH // 2 - top_limit + (padding * i)), HEIGHT // 2 - 20))
        elif i > 6 and i < 14:
            ventana.blit(letras[i], ((WIDTH // 2 - top_limit + (padding * (i - 7))), HEIGHT // 2 + padding_top))
        elif i > 13 and i < 21:
            ventana.blit(letras[i], ((WIDTH // 2 - top_limit + (padding * (i - 14))), HEIGHT // 2 + padding_top + 70))
        else:
            ventana.blit(letras[i], ((WIDTH // 2  + (padding * (i - 21)) - 185), HEIGHT // 2 + padding_top  + 140))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    fpsclock.tick(FPS)