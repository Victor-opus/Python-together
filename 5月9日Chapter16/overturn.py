# -*- coding: cp936 -*-
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load('beach_ball.png')
my_ball2 = pygame.image.load('beach_ball.png')
x= 50
y= 50
x_speed = 2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(10)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x= x+x_speed
    if x > screen.get_width()-90:#只要球超过右边，左边立刻显示，故需要再块移，然后再擦除
        pygame.draw.rect(screen,[255,255,255],[x-screen.get_width(),y,90,90],0)
        screen.blit(my_ball,(x-screen.get_width(),y))
        
    if x > screen.get_width():
        x=0
  
    screen.blit(my_ball,(x,y))
    
    pygame.display.flip()
pygame.quit()
