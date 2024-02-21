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
estado = 'started'

ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HANGMAN")

animales = ['gato', 'perro', 'leon', 'tigre']
palabra_actual = escoger_palabra(animales)
palabra_espacios = ['_' for i in range(len(palabra_actual))]

letras = cargar_imagenes()
letras_rects = []
padding = 75
padding_top = 50
top_limit = 260

while True:
    ventana.fill(BLANCO)
    # Imprimo en pantallas las letras. Como son imagenes debo sacarles su rectangulo y posicion para que se usen como botones. (Presionar ejecuten algo) - Funcion extraer_rects_img() empieza a llenar una lista con los rectangulos de cada imagen
    if estado == 'started':
        #Muestra los espacios en pantalla. De acuerdo al largo de la palabra de debe ajustar la poscion de inicio para que quede esteticamente organizada 
        espacios = texto_pantalla(" ".join(palabra_espacios), COLOR, BLANCO, (WIDTH // 2 - 80), (HEIGHT // 2 - 100), 65)
        ventana.blit(espacios[0], espacios[1])
    
        for i in range(26):
            #Cada if representa una linea del teclado. Padding lo multiplo por i para que vaya espaciando la letras hacia la derecha
            if i < 7:
                ventana.blit(letras[i], ((WIDTH // 2 - top_limit + (padding * i)), HEIGHT // 2 - 20))
                letras_rects.append(extraer_rects_img(letras[i], (WIDTH // 2 - top_limit + (padding * i)), HEIGHT // 2 - 20))
            elif i > 6 and i < 14:
                ventana.blit(letras[i], ((WIDTH // 2 - top_limit + (padding * (i - 7))), HEIGHT // 2 + padding_top))
                letras_rects.append(extraer_rects_img(letras[i], (WIDTH // 2 - top_limit + (padding * (i - 7))), HEIGHT // 2 + padding_top))
            elif i > 13 and i < 21:
                ventana.blit(letras[i], ((WIDTH // 2 - top_limit + (padding * (i - 14))), HEIGHT // 2 + padding_top + 70))
                letras_rects.append(extraer_rects_img(letras[i], (WIDTH // 2 - top_limit + (padding * (i - 14))), HEIGHT // 2 + padding_top + 70))
            else:
                ventana.blit(letras[i], ((WIDTH // 2  + (padding * (i - 21)) - 185), HEIGHT // 2 + padding_top  + 140))
                letras_rects.append(extraer_rects_img(letras[i],(WIDTH // 2  + (padding * (i - 21)) - 185), HEIGHT // 2 + padding_top  + 140))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and estado == 'started':
            #Ya las imagenes tienen su rectangulo que permite verificar si el mouse se presiono sobre ellas. Al presionar una tecla se mira si la esa letra esta en la palabra
            for i in range(26):
                if letras_rects[i].collidepoint(pygame.mouse.get_pos()):
                    #Si la letra esta una sola vez en la palabra se busca su indice 
                    if palabra_actual.count(chr(i + 97)) == 1:
                        if chr(i + 97) in palabra_actual:
                            palabra_espacios[palabra_actual.find(chr(i + 97))] = chr(i + 97)
                            break
                    elif palabra_actual.count(chr(i + 97)) > 1:
                        for index, val in enumerate(palabra_actual):
                            if val == chr(i + 97):
                                palabra_espacios[index] = chr(i + 97)                       
    
    pygame.display.update()
    fpsclock.tick(FPS)