import pygame 
import time

# Inicializa todos os módulos do Pygame
pygame.init()

# Carrega o arquivo de música
pygame.mixer.music.load("natal.mp3")

# Toca o arquivo de música
pygame.mixer.music.play()

# Aguarda a reprodução do arquivo de música (duração em segundos)
while pygame.mixer.music.get_busy():
    time.sleep(1)