# -*- coding: cp936 -*-
import pygame
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_red = pygame.image.load("DozerRed.png")#my_ball��һ��Ҳ�Ǳ��棬ֻ�ǿ�����
screen.blit(my_red,[50,50])  #��my_ball������渴�Ƶ�screen���棬blit���ƣ���ָͼƬ�ĸ��ƣ�
pygame.display.flip()          #�����50���ඥ��50
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print my_red
pygame.quit()
