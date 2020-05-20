# -*- coding: cp936 -*-
import pygame
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")#my_ball是一个也是表面，只是看不到
screen.blit(my_ball,[50,50])  #将my_ball这个表面复制到screen表面，blit块移（特指图片的复制）
pygame.display.flip()          #距左边50，距顶部50
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print my_ball
pygame.quit()
