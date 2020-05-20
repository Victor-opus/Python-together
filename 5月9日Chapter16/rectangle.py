# -*- coding: cp936 -*-
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.rect(screen,[255,0,0],[250,150,300,200],2) #表面 颜色 位置加大小 线宽 0是填充
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
print screen
pygame.quit()
