# -*- coding: cp936 -*-
import pygame,sys

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

pygame.mixer.music.load("test.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(2)#2是播放次数，负数为一直播放
splat = pygame.mixer.Sound("splat.wav")#splat 啪啦声(Sound类)
splat.set_volume(0.50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not pygame.mixer.music.get_busy():#检查音乐是否忙(即是否在播放音乐，是返回1)
        splat.play()
        pygame.time.delay(1000)
        running = False
pygame.quit()
pygame.quit()
