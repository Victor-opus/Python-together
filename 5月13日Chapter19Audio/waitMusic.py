# -*- coding: cp936 -*-
import pygame,sys

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

pygame.mixer.music.load("test.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(2)#2�ǲ��Ŵ���������Ϊһֱ����
splat = pygame.mixer.Sound("splat.wav")#splat ž����(Sound��)
splat.set_volume(0.50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not pygame.mixer.music.get_busy():#��������Ƿ�æ(���Ƿ��ڲ������֣��Ƿ���1)
        splat.play()
        pygame.time.delay(1000)
        running = False
pygame.quit()
pygame.quit()
