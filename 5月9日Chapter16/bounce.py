# -*- coding: cp936 -*-
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")#my_ball��һ��Ҳ�Ǳ��棬ֻ�ǿ�����
x = 50
y = 50 #�����50���ඥ��50
x_speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x= x+x_speed
    #if x > screen.get_width() -90 or x < 0:
    if x > screen.get_width() -180 or x < 0:
        x_speed = -x_speed  #�ı��ٶȷ��ţ�ʹ����ת
    screen.blit(my_ball,[x,y])
    pygame.display.flip()
    
print my_ball
pygame.quit()
