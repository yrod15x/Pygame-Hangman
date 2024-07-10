#Programa que simula el juego del ahorcado. 

import pygame, sys
from funciones import *

pygame.init()

FPS = 60
fpsclock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
BLANCO = (255, 255, 255)
BLACK = (0, 0, 0)
VERDE = (0, 255, 0)
COLOR = (12, 67, 125)
FOND_TEXTO = (125, 65, 12)
menuFondo = pygame.image.load('menufondo1.png')
estado = 'unstarted'
score = 0

ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HANGMAN")

animales = ['gato', 'perro', 'leon', 'tigre', 'cocodrilo']
letras_usadas = set()
letra_pulsada = ''
juego = 'on'

letras = cargar_imagenes()
next_btn = pygame.image.load('button_next.png').convert_alpha()
exit_btn = pygame.image.load('button_exit.png').convert_alpha()
used_btn = pygame.image.load('button_used_letters.png').convert_alpha()
start_btn = pygame.image.load('button_start.png').convert_alpha()
#convierto la imagen en rect para poder hacer click en ella -> collidepoint(mouse.get_pos())
rect_start_btn = extraer_rects_img(start_btn, WIDTH //2 - 85, HEIGHT // 2 + 40)
letras_rects = []
padding = 75
padding_top = 50
top_limit = 260
errores = 0
div_let_usadas = 4
str_let_usadas = ''
musica_fondo = pygame.mixer.Sound('musicafondo.mp3')
incorrecto = pygame.mixer.Sound('sonidoincorrecto.mp3')

while True:
    ventana.fill(BLANCO)
    # Imprimo en pantallas las letras. Como son imagenes debo sacarles su rectangulo y posicion para que se usen como botones. (Presionar ejecuten algo) - Funcion extraer_rects_img() empieza a llenar una lista con los rectangulos de cada imagen
    if estado == 'started':
        if juego == 'on':
            palabra_actual = escoger_palabra(animales)
            palabra_espacios = ['_' for i in range(len(palabra_actual))]
            juego = 'off'
        if palabra_actual == "".join(palabra_espacios):
            estado = 'finished'
        #Muestra los espacios en pantalla. De acuerdo al largo de la palabra de debe ajustar la poscion de inicio para que quede esteticamente organizada 
        espacios = texto_pantalla(" ".join(palabra_espacios), COLOR, BLANCO, (WIDTH // 2), (HEIGHT // 2 - 100), 65)
        ventana.blit(espacios[0], espacios[1])
        ventana.blit(used_btn, (560,20))
        #Se colocan las letras usadas en pantalla cuando lleguen a cierto tamano
        #se hace un salto de linea
        str_let_usadas = list(letras_usadas)
        str_let_usadas.sort()
        if len(str_let_usadas) > 8:
            str_let_usadas.insert(7, '\n')
            str_let_usadas.insert(7, '\n')
        imprimir_multilinea("".join(str_let_usadas), 590, 60, 25, ventana, BLACK, BLANCO)
        
        #imprimir score
        score_text = texto_pantalla(str(score), BLACK, BLANCO, WIDTH // 2 - 10, 37, 40)
        ventana.blit(score_text[0], score_text[1])
        
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
                
        #Dibuja el patibulo y el ahorcado cada vez que sea presione la tecla incorrecta
        if errores >= 1 and estado != 'finished':
            pygame.draw.line(ventana, (BLACK), (70, HEIGHT // 2 - 120), (170, HEIGHT // 2 - 120),5)
        if errores >= 2:
            pygame.draw.line(ventana, (BLACK), (70, HEIGHT // 2 - 120), (70, 40),5)
        if errores >= 3:
            pygame.draw.line(ventana, (BLACK), (70, 40), (120, 40),5)
        if errores >= 4:
            pygame.draw.line(ventana, (BLACK), (120, 40), (120, 60),5)
        if errores >= 5:
            pygame.draw.circle(ventana, (BLACK), (120, 80), 20, 5)
        if errores >= 6:
            pygame.draw.line(ventana, (BLACK), (120, 100), (120, 150), 5)
        if errores >= 7:
            pygame.draw.line(ventana, (BLACK), (120, 120), (140, 120), 5)
        if errores >= 8:
            pygame.draw.line(ventana, (BLACK), (120, 120), (100, 120), 5)
        if errores >= 9:
            pygame.draw.line(ventana, (BLACK), (120, 150), (135, 170), 5)
        if errores >= 10:
            pygame.draw.line(ventana, (BLACK), (120, 150), (105, 170), 5) 
        if errores >= 10:
            estado = 'finished'     
    elif estado == 'unstarted':
        ventana.blit(menuFondo, (0, 0))
        ventana.blit(start_btn, (WIDTH //2 - 85, HEIGHT // 2 + 40))
        musica_fondo.play(-1)
        musica_fondo.set_volume(0.5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #comenzar el juego presionando el boton start. 
        if event.type == pygame.MOUSEBUTTONDOWN and estado == 'unstarted':
            if rect_start_btn.collidepoint(pygame.mouse.get_pos()):
                estado = 'started'
                musica_fondo.stop()
        elif event.type == pygame.MOUSEBUTTONDOWN and estado == 'started':
            #Ya las imagenes tienen su rectangulo que permite verificar si el mouse se presiono sobre ellas. Al presionar una tecla se mira si la esa letra esta en la palabra
            for i in range(26):
                letra_pulsada = chr(i + 97)
                if letras_rects[i].collidepoint(pygame.mouse.get_pos()) and letra_pulsada not in letras_usadas:
                    #Si la letra esta una sola vez en la palabra se busca su indice 
                    if palabra_actual.count(letra_pulsada) > 0:
                        letras_usadas.add(letra_pulsada)
                        score += 10
                    if palabra_actual.count(letra_pulsada) == 1:
                        if letra_pulsada in palabra_actual:
                            palabra_espacios[palabra_actual.find(letra_pulsada)] = letra_pulsada
                            letras_usadas.add(letra_pulsada)
                            break
                    elif palabra_actual.count(letra_pulsada) > 1:
                        for index, val in enumerate(palabra_actual):
                            if val == letra_pulsada:
                                palabra_espacios[index] = letra_pulsada 
                                  
                    elif letra_pulsada not in letras_usadas:
                        #Lleva la cuenta de los errores para ir dibujando cada pieza del
                        #patibulo y el ahorcado una por una. 
                        errores += 1
                        letras_usadas.add(letra_pulsada)
                        incorrecto.play()
                elif letras_rects[i].collidepoint(pygame.mouse.get_pos()) and letra_pulsada in letras_usadas:
                    #agregar sonido  
                    incorrecto.play()          
                    #print("Letra registrada")
        if event.type == pygame.MOUSEBUTTONDOWN and estado == 'finished':
            #Si se hace click en salir o siguiente - Sacar el rect de la imagen
            exit_btn_rect = extraer_rects_img(exit_btn, (WIDTH //2) - 70, (HEIGHT // 2) - 220)
            next_btn_rect = extraer_rects_img(next_btn, (WIDTH //2) - 70, (HEIGHT // 2) - 270)
            if exit_btn_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            elif next_btn_rect.collidepoint(pygame.mouse.get_pos()):
                estado = 'started'
                juego = 'on'
                letras_usadas = set()
                letra_pulsada = ''
                        
    #Imprimir en pantalla un resumen del juego
    if estado == 'finished':
        ventana.blit(next_btn,((WIDTH //2) - 70, (HEIGHT // 2) - 270))
        ventana.blit(exit_btn,((WIDTH //2) - 70, (HEIGHT // 2) - 220))
        ventana.blit(used_btn, (560,30))
        imprimir_multilinea("".join(str_let_usadas), 590, 80, 20, ventana, BLACK, BLANCO)
        pal_score = texto_pantalla("Score", BLACK, BLANCO, 120, 40, 35)
        ventana.blit(pal_score[0], pal_score[1])
        score_text[1] = (95, 60)
        ventana.blit(score_text[0], score_text[1])
        palabra_actual_rect = texto_pantalla(palabra_actual, VERDE, BLANCO, (WIDTH // 2) - 10, (HEIGHT // 2), 100)
        ventana.blit(palabra_actual_rect[0], palabra_actual_rect[1])
                                               
    pygame.display.update()
    fpsclock.tick(FPS)