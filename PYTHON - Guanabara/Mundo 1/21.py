import pygame
import os

# Verifica o diretório de trabalho atual
print("Diretório de trabalho:", os.getcwd())

pygame.mixer.init()
pygame.init()

# Carrega o arquivo de música (substitua pelo caminho correto se necessário)
pygame.mixer.music.load(r'C:\Users\thiag\OneDrive\Área de Trabalho\mascara.mp3')
pygame.mixer.music.play()

pygame.event.wait()
