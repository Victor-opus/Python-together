import pygame
from random import *


class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

def animate(group):
    screen.fill([255,255,255])
    
    for ball in group:
        ball.move()
        group.remove(ball)
        if pygame.sprite.spritecollide(ball,group,False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]

        group.add(ball)
        
        screen.blit(ball.image,ball.rect)
    pygame.display.flip()
        

size = width, height = 640,480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "beach_ball.png"
clock = pygame.time.Clock()
group = pygame.sprite.Group()
print group
for row in range(0,3):
    for column in range(0,3):
        location = [column * 180 + 20, row * 180 + 20]
        speed = [choice([-2,2]),choice([-2,2])]
        print speed
        ball = MyBallClass(img_file,location,speed)
        group.add(ball)
        

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            frame_rate = clock.get_fps()
            print "frame rate = ",frame_rate
    animate(group)
    clock.tick(30)
pygame.quit()
