# -*- coding: cp936 -*-
import pygame,sys
pygame.init()
pygame.mixer.init()#混音器初始化

screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

splat = pygame.mixer.Sound("splat.wav")
print splat
splat.play()   #播放声音

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
