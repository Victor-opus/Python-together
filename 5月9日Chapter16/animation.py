# -*- coding: cp936 -*-
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")#my_ball是一个也是表面，只是看不到
x = 50
y = 50 #距左边50，距顶部50
screen.blit(my_ball,[x,y])  #将my_ball这个表面复制到screen表面，blit块移（特指图片的复制）
pygame.display.flip()
for i in range(1,200):
    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x = x + 5
    screen.blit(my_ball,[x,y])
    pygame.display.flip()
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print my_ball
pygame.quit()
