import pygame, os
from random import choice

def texto_pantalla(texto, color, fondo, pos_x, pos_y, tam_fuente):
    datos_texto = []
    fuente =  pygame.font.SysFont('Comic Sans', tam_fuente)
    letras = fuente.render(texto, True, color, fondo)
    letras_rect = letras.get_rect()
    letras_rect.center = (pos_x, pos_y)
    datos_texto.append(letras)
    datos_texto.append(letras_rect)
    
    return datos_texto

def cargar_imagenes():
    letras  = []
    for i in range(97, 123):
        nom = f"button_{chr(i)}.png"
        letras.append(pygame.image.load(nom).convert_alpha())
    return letras

def escoger_palabra(lista):
    return choice(lista)

def extraer_rects_img(imagen, pos_x, pos_y):
    """Extrae rectangulo de una superfice: una imagen. Para que se pueda usar como boton"""
    #Topleft permite abarcar toda la superfice del btn cuando se presiona. No usar center
    rect = imagen.get_rect(topleft=(pos_x, pos_y)) 
    return rect 

def imprimir_multilinea(texto, posX, posY, tam_fuente, pantalla, color_fuente, color_fondo):
    lineas = texto.splitlines()
    for index, valor in enumerate(lineas):
        fuente  = pygame.font.SysFont('Verdana', tam_fuente)
        #si no se pone color de fondo como como 3er parametro en la funcion render el texto sale sin frame
        pantalla.blit(fuente.render(valor, 1, color_fuente, color_fondo), (posX, posY + tam_fuente * index))