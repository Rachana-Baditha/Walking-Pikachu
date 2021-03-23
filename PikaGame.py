import pygame

pygame.init()

#Window for Game
wn = pygame.display.set_mode((500,500))
pygame.display.set_caption("Walking Pikachu")

clock = pygame.time.Clock()

class player(object):
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.vel = 5
        self.walkcount = 0
        
        self.left = False
        self.right = False
        self.up = False
        self.down = True


#Sprite Images
WalkRight = [pygame.image.load("PikaR1.png"), pygame.image.load("PikaR2.png"), pygame.image.load("PikaR3.png"), pygame.image.load("PikaR4.png")]
WalkLeft = [pygame.image.load("PikaL1.png"), pygame.image.load("PikaL2.png"), pygame.image.load("PikaL3.png"), pygame.image.load("PikaL4.png")]
WalkUp = [pygame.image.load("PikaB1.png"), pygame.image.load("PikaB2.png"), pygame.image.load("PikaB3.png"), pygame.image.load("PikaB4.png")]
WalkDown = [pygame.image.load("PikaF1.png"), pygame.image.load("PikaF2.png"), pygame.image.load("PikaF3.png"), pygame.image.load("PikaF4.png")]

bg = pygame.image.load("Grass.jpg")


run = True

#Keyboard Commands
def UseKeys(man):
    global man.vel
    global man.x,man.y
    global man.left, man.right, man.up, man.down
    
    key = pygame.key.get_pressed()
    
    if key[pygame.K_LEFT] and man.x>0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.up = False
        man.down = False
    elif key[pygame.K_RIGHT] and man.x<436:
        man.x += man.vel
        left = False
        right = True
        up = False
        down = False
    elif key[pygame.K_UP] and y>0:
        y -= vel
        left = False
        right = False
        up = True
        down = False
    elif key[pygame.K_DOWN] and y<436:
        y += vel
        left = False
        right = False
        up = False
        down = True
        
def RedrawWindow():
    global walkCount
    wn.blit(bg,(-260,0))

        
    if walkCount + 1 >=8:
        walkCount=0
    
    if left:
        wn.blit(WalkLeft[walkCount//2],(x,y))
        walkCount += 1
        
    elif right:
        wn.blit(WalkRight[walkCount//2],(x,y))
        walkCount += 1
    
    elif up:
        wn.blit(WalkUp[walkCount//2],(x,y))
        walkCount += 1
    
    elif down:
        wn.blit(WalkDown[walkCount//2],(x,y))
        walkCount += 1    
        
    
    pygame.display.update()
    
man = player(250,250,64,64)
    
#Main Game Loop
while run:
    
    clock.tick(16)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    UseKeys()
    
    RedrawWindow()
    
pygame.quit()
    
    
    