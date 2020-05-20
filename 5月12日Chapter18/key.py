# -*- coding: cp936 -*-  #GBK
import pygame
pygame.init()
delay = 100 #在重复开始之前等待多长时间
interval = 50 #以多块的速度重复，即每个按键事件之间要隔多长时间
pygame.key.set_repeat(delay,interval) #单位均是ms
screen = pygame.display.set_mode([640,480])
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])
clock = pygame.time.Clock()
class Ball(pygame.sprite.Sprite):
    def __init__(self,image_file,speed,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        if self.rect.left <= screen.get_rect().left or \
           self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos


my_ball = Ball('beach_ball.png',[5,0],[20,20])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my_ball.rect.top = my_ball.rect.top - 10
            elif event.key == pygame.K_DOWN:
                my_ball.rect.top = my_ball.rect.top + 10

        
    clock.tick(30)
    screen.blit(background,(0,0))
    my_ball.move()
    screen.blit(my_ball.image,my_ball.rect)
    pygame.display.flip()
pygame.quit()
