# -*- coding: cp936 -*-
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.circle(screen,[255,0,0],[320,240],30,0) #���� ��ɫ ���� �뾶 �߿� 0�����
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
print screen
pygame.quit()
