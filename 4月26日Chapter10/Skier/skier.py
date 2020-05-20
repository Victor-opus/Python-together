# -*- coding: utf-8 -*-
import pygame, sys, random
skier_images = ["skier_down.png", "skier_right1.png",
               "skier_right2.png","skier_left2.png",
               "skier_left1.png"]
class SkierClass(pygame.sprite.Sprite): #创建滑雪者
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320,100]
        self.angle = 0
    def turn(self, direction):#滑雪者转向
        self.angle = self.angle+direction
        if self.angle <-2:
            self.angle = -2
        if self.angle >2:
            self.angle =2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6-abs(self.angle)*2]
        return speed
    def move(self,speed):#滑雪者左右移动
        self.rect.centerx = self.rect.centerx+speed[0]
        if self.rect.centerx < 20:
            self.rect.centerx = 20
        if self.rect.centerx > 620:
            self.rect.centerx = 620
       
class ObstacleClass(pygame.sprite.Sprite): #创建树和小旗
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False
    def update(self): #让场景向上滚
        global speed
        self.rect.centery-= speed[1]
        if self.rect.centery < -32:
            self.kill()


def create_map(): #创建一个窗口，包含随机的树和小旗
    global obstacles
    locations = []
    for i in range(10):
        row = random.randint(0,9)
        col = random.randint(0,9)
        location = [col * 64+20, row*64+20+640]
        if not (location in locations):
            locations.append(location)
            type = random.choice(["tree","flag"])
            if type == "tree":
                img = "skier_tree.png"
            elif type == "flag":
                img = "skier_flag.png"
            obstacle = ObstacleClass(img, location, type)
            obstacles.add(obstacle)
def create_map():
    global obstacles
    locations = []
    for i in range(10):                 # 10 obstacles per screen 
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location  = [col * 64 + 32, row * 64 + 32 + 640] #center x, y for obstacle
        if not (location in locations):        # prevent 2 obstacles in the same place
            locations.append(location)          
            type = random.choice(["tree", "flag"])
            if type == "tree": img = "skier_tree.png"
            elif type == "flag":  img = "skier_flag.png"
            obstacle = ObstacleClass(img, location, type)
            obstacles.add(obstacle)

def animate(): #重绘屏幕
    screen.fill([255,255,255])
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text,[10,10])
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()
speed = [0, 6]
obstacles = pygame.sprite.Group()   # group of obstacle objects
skier = SkierClass()
map_position = 0
points = 0
create_map()      # create one screen full of obstacles
font = pygame.font.Font(None, 50)

# main Pygame event loop
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        
        if event.type == pygame.KEYDOWN:          # check for key presses
            if event.key == pygame.K_LEFT:        # left arrow turns left
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:     #right arrow turns right
                speed = skier.turn(1)
    skier.move(speed)                         # move the skier (left or right)
    map_position += speed[1]                      # scroll the obstacles
    
    # create a new block of obstacles at the bottom
    if map_position >= 640:
        create_map()
        map_position = 0
    
    # check for hitting trees or getting flags
    hit =  pygame.sprite.spritecollide(skier, obstacles, False)
    if hit:
        if hit[0].type == "tree" and not hit[0].passed:  #crashed into tree  
            points = points - 100
            skier.image = pygame.image.load("skier_crash.png")  # crash image
            animate()  
            pygame.time.delay(1000)
            skier.image = pygame.image.load("skier_down.png")  # resume skiing
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].type == "flag" and not hit[0].passed:   # got a flag
            points += 10
            hit[0].kill()                                 # remove the flag 
    
    obstacles.update()
    score_text = font.render("Score: " +str(points), 1, (0, 0, 0))
    animate()
    
pygame.quit()
    
