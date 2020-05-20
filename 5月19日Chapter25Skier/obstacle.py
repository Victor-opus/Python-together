# -*- coding: cp936 -*-
import pygame,random



class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False

    def update(self):
        global speed
        self.rect.centery-=speed[1]
        if self.rect.centery < -32:
            self.kill()
def animate():
    screen.fill([255,255,255])
    obstacles.draw(screen) #将组中成员块移到屏幕
    pygame.display.flip() #flip翻转，使修改的生效
    
def create_map():
    global obstacles
    locations = []
    for i in range(10):
        row = random.randint(0,9)
        col = random.randint(0,9)
        location =  [col*64+32,row*64+32+640]
        if not (location in locations):
            locations.append(location)
            type = random.choice(["tree","flag"])
            if type == "tree":
                img = "skier_tree.png"
            elif type == "flag":
                img = "skier_flag.png"
            obstacle = ObstacleClass(img,location,type)
            obstacles.add(obstacle)

pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()
obstacles = pygame.sprite.Group()
map_position = 0
speed = [0,6]
create_map()

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    map_position += speed[1]
    if map_position >= 640:
        create_map()
        map_position = 0
    obstacles.update()
    animate()

pygame.quit()
