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
        global score,score_font,score_surf  #使用的是全局变量
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
            hit_wall.play()
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            score = score + 1
            score_surf = score_font.render(str(score),1,(0,0,0))
            get_point.play()


class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self,location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20]) #创建一个表面
        image_surface.fill([0,0,0])#用黑色填充
        self.image = image_surface.convert()#转换成图片
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        
pygame.init()
pygame.mixer.init()
hit = pygame.mixer.Sound("hit_paddle.wav")
hit.set_volume(0.4)
hit_wall = pygame.mixer.Sound("hit_wall.wav")
hit_wall.set_volume(0.4)
get_point = pygame.mixer.Sound("get_point.wav")
get_point.set_volume(0.2)
splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.6)
new_life = pygame.mixer.Sound("new_life.wav")
new_life.set_volume(0.5)
bye = pygame.mixer.Sound("game_over.wav")
bye.set_volume(0.6)
pygame.mixer.music.load("test.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1) #无限循环
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
ball_speed = [10,5]
myBall = MyBallClass("wackyball.bmp",ball_speed,[50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270,400])#paddle球拍
score = 0
lives = 3 #表示有三条命
score_font = pygame.font.Font(None,50) #创建字体对象，None表示默认字体，字体大小
score_surf = score_font.render(str(score),True,(0,255,0))#渲染文本，向字体对象传入一个字符串，返回一个含有这个文本的新表面
score_pos = [10,10]                # True 是抗锯齿（参数为是否抗锯齿）
print ballGroup                    #锯齿现象是边缘较模糊
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
            paddle.rect.centerx = event.pos[0]#pos[0]是鼠标的x，[1]是y

    if pygame.sprite.spritecollide(paddle,ballGroup,False):
        myBall.speed[1] = -5
        hit.play()
        
    
    if not done:
        myBall.move()
        screen.blit(myBall.image,myBall.rect)
        screen.blit(paddle.image,paddle.rect)
        screen.blit(score_surf,score_pos) #把含有分数文本的表面块移到这个位置
        for i in range(lives):
            width = screen.get_rect().width
            screen.blit(myBall.image,[width-40*i,20])
        pygame.display.flip()
    if myBall.rect.top >= screen.get_rect().bottom:
        if not done:
            splat.play()
        lives = lives-1
        if lives <= 0:
            if not done:
                pygame.time.delay(1000)
                bye.play()
            ball_speed = [0,0]
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
            pygame.mixer.music.fadeout(2000)#让音乐淡出(逐渐减弱到消失)，2s后结束 fade褪色
        else:
            
            pygame.time.delay(1000)
            new_life.play()
            myBall.rect.top,myBall.rect.left = [50,50]
            screen.blit(myBall.image,myBall.rect)
            pygame.display.flip()
            pygame.time.delay(1000)
      
    
pygame.quit()
        


