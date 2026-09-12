import pygame

pygame.mixer.init()
pygame.mixer.music.load('mario.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.delay(100)
