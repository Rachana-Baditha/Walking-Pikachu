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
        self.walkCount = 0
        
        self.left = False
        self.right = False
        self.up = False
        self.down = True
        
        self.stand = True
        
    def draw(self):
        
        
        if self.walkCount + 1 >=8:
             self.walkCount=0
     
        if not(self.stand):
            
            if self.left:
                wn.blit(WalkLeft[self.walkCount//2],(self.x,self.y))
                self.walkCount += 1
            
            elif self.right:
                wn.blit(WalkRight[self.walkCount//2],(self.x,self.y))
                self.walkCount += 1
        
            elif self.up:
                wn.blit(WalkUp[self.walkCount//2],(self.x,self.y))
                self.walkCount += 1
        
            elif self.down:
                wn.blit(WalkDown[self.walkCount//2],(self.x,self.y))
                self.walkCount += 1  
                
        else:
            
            if self.left:
                wn.blit(WalkLeft[self.walkCount//2],(self.x,self.y))
            elif self.right:
                wn.blit(WalkRight[self.walkCount//2], (self.x,self.y))
            elif self.up:
                wn.blit(WalkUp[self.walkCount//2],(self.x,self.y))
            elif self.down:
                wn.blit(WalkDown[self.walkCount//2],(self.x, self.y))

class projectile(object):
    
    def __init__(self,x,y,radius,color,facing,axis):
        
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.axis = axis
        
        self.vel = 8 * facing
        
    def draw(self):
        pygame.draw.circle(wn,self.color,(self.x,self.y),self.radius)
    


#Sprite Images
WalkRight = [pygame.image.load("PikaR1.png"), pygame.image.load("PikaR2.png"), pygame.image.load("PikaR3.png"), pygame.image.load("PikaR4.png")]
WalkLeft = [pygame.image.load("PikaL1.png"), pygame.image.load("PikaL2.png"), pygame.image.load("PikaL3.png"), pygame.image.load("PikaL4.png")]
WalkUp = [pygame.image.load("PikaB1.png"), pygame.image.load("PikaB2.png"), pygame.image.load("PikaB3.png"), pygame.image.load("PikaB4.png")]
WalkDown = [pygame.image.load("PikaF1.png"), pygame.image.load("PikaF2.png"), pygame.image.load("PikaF3.png"), pygame.image.load("PikaF4.png")]

bg = pygame.image.load("Grass.jpg")


run = True

#Keyboard Commands
def UseKeys(man,shocks):
    
    key = pygame.key.get_pressed()

    
    if key[pygame.K_SPACE]:
        
        if man.left:
            facing = -1
            axis = 1
        elif man.up:
            facing = -1
            axis = -1
        elif man.right:
            facing = 1
            axis = 1
        elif man.down:
            facing = 1
            axis = -1
        
        if len(shocks) <=6:
            shocks.append(projectile(round(man.x + man.width//2),round(man.y + 2*man.height//3),5,(255,255,0),facing,axis))
    
    if key[pygame.K_LEFT] and man.x>0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.up = False
        man.down = False
        man.stand = False
    elif key[pygame.K_RIGHT] and man.x<436:
        man.x += man.vel
        man.left = False
        man.right = True
        man.up = False
        man.down = False
        man.stand = False
    elif key[pygame.K_UP] and man.y>0:
        man.y -= man.vel
        man.left = False
        man.right = False
        man.up = True
        man.down = False
        man.stand = False
    elif key[pygame.K_DOWN] and man.y<436:
        man.y += man.vel
        man.left = False
        man.right = False
        man.up = False
        man.down = True
        man.stand = False
    else:
        man.stand = True
        
def RedrawWindow():
    global walkCount
    wn.blit(bg,(-260,0))
    
    man.draw()
    
    for shot in shocks:
        shot.draw()
        
    
    pygame.display.update()

    
#Main Game Loop
    
man = player(250,250,64,64)
shocks = []

while run:
    
    clock.tick(16)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    for shot in shocks:
        if (shot.x < 500 and shot.x > 0) and (shot.y < 500 and shot.y > 0):
            
            if shot.axis == 1:
                shot.x += shot.vel
            elif shot.axis == -1:
                shot.y += shot.vel
        
        else:
            shocks.remove(shot)
        
                
    UseKeys(man,shocks)
    
    RedrawWindow()
    
pygame.quit()
    
    
    