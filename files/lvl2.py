from files.player import *
from files.blocks import *
from files.carrot import *
from files.enemy import *
from files.door import *
from files.lvl3 import *
import pygame
#pygame.init()

class Start2(object):

    #Objects
    rabbit=Player(0,450,63,57)
    carrots=[Carrot(400,280,32,32),Carrot(356,450,32,32),Carrot(656,450,32,32)]
    wolves=[Enemy(200,350,45,30,264)]
    gate=Door(300,125,72,83,0)
    clock=pygame.time.Clock()

    lvl1=[Block(100,400,64,64),Block(200,350,64,64),Block(264,350,64,64),Block(400,280,64,64),Block(300,180,64,64),
         #Block(284,380,64,64),Block(284,380,64,64),Block(284,380,64,64),Block(284,380,64,64),Block(284,380,64,64),
      

          Block(0,550,64,64),Block(64,550,64,64),Block(128,550,64,64),Block(192,550,64,64),Block(256,550,64,64),
          Block(320,550,64,64),Block(384,550,64,64),Block(448,550,64,64),Block(512,550,64,64),Block(576,550,64,64),
          Block(640,550,64,64),Block(704,550,64,64),Block(768,550,64,64),Block(640,550,64,64),Block(832,550,64,64),
          Block(896,550,64,64),Block(960,550,64,64),Block(1024,550,64,64),Block(1088,550,64,64),Block(1152,550,64,64),
          Block(1216,550,64,64),Block(1280,550,64,64),Block(1344,550,64,64)]
    

    def __init__(self):
        self.WIDTH=1300
        self.HEIGHT=600
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.nextLevel=Start3()
        self.isNext=False

        #setting up environment
        #self.ground=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\ground blocks\\ground.png')
        self.bg=pygame.transform.scale(pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\bg.png'), (self.WIDTH, self.HEIGHT))

    #main function
    def main(self):
        pygame.display.set_caption("Level 2")
        running=True
        while running:

            dx=0
            dy=0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys=pygame.key.get_pressed()

            if keys[pygame.K_SPACE] and self.rabbit.isJump == False:
                self.rabbit.y -= 20
                self.rabbit.isJump = True
                self.rabbit.jumpSound.play()
            if keys[pygame.K_SPACE] == False:
                self.rabbit.isJump = False

            if keys[pygame.K_LEFT] and self.rabbit.x>self.rabbit.vel and self.rabbit.x+self.rabbit.width<self.WIDTH: 
                self.rabbit.x-=self.rabbit.vel
                self.rabbit.rect.x-=self.rabbit.vel
                self.rabbit.left=True
                self.rabbit.right=False
                self.rabbit.standing=False
                self.rabbit.direc=-1
                dx -= 5
                
                
            elif keys[pygame.K_RIGHT] and self.rabbit.x<self.WIDTH-self.rabbit.width-self.rabbit.vel and self.rabbit.x+self.rabbit.width<self.WIDTH:
                self.rabbit.x+=self.rabbit.vel
                self.rabbit.rect.x+=self.rabbit.vel
                self.rabbit.left=False
                self.rabbit.right=True
                self.rabbit.standing=False
                self.rabbit.direc=1
                dx += 5
                
            else:
                self.rabbit.walkCount=0
                self.rabbit.standing=True

            #add gravity
            self.rabbit.y += 1
            if self.rabbit.y > 10:
                self.rabbit.y = 10
            dy += self.rabbit.y

            #check collision for block
            for block in self.lvl1:
                #check for collision in x direction
                if block.rect.colliderect(self.rabbit.rect.x + dx, self.rabbit.rect.y, self.rabbit.width, self.rabbit.height):
                    dx = 0
                #check for collision in y direction
                if block.rect.colliderect(self.rabbit.rect.x, self.rabbit.rect.y+self.rabbit.vel, self.rabbit.width, self.rabbit.height):
                    #check if below the ground i.e jumping
                    if self.rabbit.y < 0:
                        dy=block.rect.bottom-self.rabbit.rect.top
                        self.rabbit.y=0
                    #check if below the ground i.e jumping
                    elif self.rabbit.y >= 0:
                        dy=block.rect.top-self.rabbit.rect.bottom
                        self.rabbit.y=0
            #update position of rabbit
            self.rabbit.rect.x += dx
            self.rabbit.rect.y += dy

            if self.rabbit.rect.bottom > self.HEIGHT:
                self.rabbit.rect.bottom = self.HEIGHT
                dy = 0

            #check collision for carrot
            for carrot in self.carrots:
                if carrot.rect.colliderect(self.rabbit.rect.x, self.rabbit.rect.y+self.rabbit.vel, self.rabbit.width, self.rabbit.height):
                    self.rabbit.collectable.val+=1 #increase val of carrots collected
                    self.gate.val+=1 #increase val of gate
                    self.carrots.remove(carrot)

            #check collision for wolf
            for wolf in self.wolves:
                if wolf.rect.colliderect(self.rabbit.rect.x, self.rabbit.rect.y+self.rabbit.vel, self.rabbit.width, self.rabbit.height):
                    self.rabbit.deathSound.play()
                    pygame.mixer.music.stop()
                    pygame.time.delay(5000)

                    self.rabbit.reset(0,450,63,57)
                    for wolf in self.wolves:
                        wolf.reset(200,350,45,30,264)
                    self.carrots=[Carrot(400,280,32,32),Carrot(356,450,32,32),Carrot(656,450,32,32)]
                    self.rabbit.collectable.val=0
                    self.gate=Door(300,180,72,83,0)

                    pygame.mixer.music.play(-1)
            
            #check collision for door
            if self.gate.rect.colliderect(self.rabbit.rect.x, self.rabbit.rect.y+self.rabbit.vel, self.rabbit.width, self.rabbit.height):
                if self.gate.passThrough(self.rabbit):
                    self.isNext=True
                    self.nextLevel.main()
                    pygame.display.quit()

                    
            self.reDrawFunc()
            
            pygame.display.update()

    def reDrawFunc(self):
        self.win.blit(self.bg,(0,0))
        #self.win.blit(self.ground,(0,500))
        for grassy in self.lvl1:
            grassy.draw(self.win)
        for carrot in self.carrots:
            carrot.draw(self.win)
        for wolf in self.wolves:
            wolf.draw(self.win)
        self.gate.draw(self.win)
        self.rabbit.draw(self.win)
        self.rabbit.collectable.draw(self.win,0,64,self.rabbit.visible)
        self.rabbit.health2.draw(self.win)
        
        #self.rabbit.health2.delete=False
