# -*- coding: cp936 -*-
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")#my_ball��һ��Ҳ�Ǳ��棬ֻ�ǿ�����
screen.blit(my_ball,[50,50])  #��my_ball������渴�Ƶ�screen���棬blit���ƣ���ָͼƬ�ĸ��ƣ�
pygame.display.flip()          #�����50���ඥ��50
pygame.time.delay(2000)
screen.blit(my_ball,[150,50])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print my_ball
pygame.quit()
