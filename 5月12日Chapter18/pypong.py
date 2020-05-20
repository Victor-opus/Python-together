# -*- coding: cp936 -*-  #GBK
import pygame
from pygame.locals import *

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,image_file,speed,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        global score,score_font,score_surf  #ʹ�õ���ȫ�ֱ���
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            score = score + 1
            score_surf = score_font.render(str(score),1,(0,0,0))


class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self,location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20]) #����һ������
        image_surface.fill([0,0,0])#�ú�ɫ���
        self.image = image_surface.convert()#ת����ͼƬ
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        
pygame.init()
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
ball_speed = [10,5]
myBall = MyBallClass("wackyball.bmp",ball_speed,[50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270,400])#paddle����
score = 0
lives = 3 #��ʾ��������
score_font = pygame.font.Font(None,50) #�����������None��ʾĬ�����壬�����С
score_surf = score_font.render(str(score),True,(0,255,0))#��Ⱦ�ı��������������һ���ַ���������һ����������ı����±���
score_pos = [10,10]                # True �ǿ���ݣ�����Ϊ�Ƿ񿹾�ݣ�
print ballGroup                    #��������Ǳ�Ե��ģ��
print myBall
done = False
running = True
while running:
    clock.tick(20)
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]#pos[0]������x��[1]��y

    if pygame.sprite.spritecollide(paddle,ballGroup,False):
        myBall.speed[1] = -5
        
    myBall.move()
    if not done:
        screen.blit(myBall.image,myBall.rect)
        screen.blit(paddle.image,paddle.rect)
        screen.blit(score_surf,score_pos) #�Ѻ��з����ı��ı�����Ƶ����λ��
        for i in range(lives):
            width = screen.get_rect().width
            screen.blit(myBall.image,[width-40*i,20])
        pygame.display.flip()
    if myBall.rect.top >= screen.get_rect().bottom:
        lives = lives-1
        if lives == 0:
            final_text1 = "Game Over"
            final_text2 = "Your final score is: " + str(score)
            ft1_font = pygame.font.Font(None,70)
            ft1_surf = ft1_font.render(final_text1,1,(0,0,0))
            ft2_font = pygame.font.Font(None,50)
            ft2_surf = ft2_font.render(final_text2,1,(0,0,0))
            screen.blit(ft1_surf,[screen.get_width()/2 - \
                                  ft1_surf.get_width()/2,100])
            screen.blit(ft2_surf,[screen.get_width()/2 - \
                                  ft2_surf.get_width()/2,200])
            pygame.display.flip()
            done = True
        else:      
            pygame.time.delay(2000)
            myBall.rect.top,myBall.rect.left = [50,50]
      
    
pygame.quit()
        


