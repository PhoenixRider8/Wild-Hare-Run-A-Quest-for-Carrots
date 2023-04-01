from files.collectable import *
from files.health2 import *
import pygame

#Player
class Player(object):

    walkLeft=[pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runLeft\\2.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runLeft\\3.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runLeft\\4.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runLeft\\5.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runLeft\\6.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runLeft\\7.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runLeft\\8.png')]
    walkRight=[pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runRight\\2.png'),
               pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runRight\\3.png'),
               pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runRight\\4.png'),
               pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runRight\\5.png'),
               pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runRight\\6.png'),
               pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runRight\\7.png'),
               pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runRight\\8.png')]
    char1=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runRight\\1.png')
    char2=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\rabbit\\runLeft\\1.png')


    def __init__(self,x,y,width,height):
        self.reset(x,y,width,height)


    def draw(self,win):
        pygame.time.delay(50)
        
        if self.visible:
            if self.walkCount+1>=8:
                self.walkCount=0

            if not(self.standing):
                if self.left:
                    win.blit(self.walkLeft[self.walkCount],self.rect)
                    self.walkCount+=1
                elif self.right:
                    win.blit(self.walkRight[self.walkCount],self.rect)
                    self.walkCount+=1
            else:
                if self.right:
                    win.blit(self.char1,self.rect)
                elif self.left:
                    win.blit(self.char2,self.rect)
                else:
                    if self.direc==1:
                            win.blit(self.char1,self.rect)
                    elif self.direc==-1:
                        win.blit(self.char2,self.rect)
                    else:
                        win.blit(self.char1,self.rect)

        self.hitbox=(self.x+17,self.y+11,29,52) #set position every movement
        #pygame.draw.rect(win,(255,255,255),self.rect,2)

    def reset(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0
        self.standing=True
        self.direc=0 #direction at which player is facing before jumping
        self.hitbox=(self.x+17,self.y+11,29,52) #rectangle of 28x60
        self.cosVal=0 #number of carrots collected

        self.carrotImg=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\carrot\\carrot.png')
        self.collectable=Collected(self.carrotImg,self.cosVal)

        self.img=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\health\\heart.png')
        self.bg=pygame.transform.scale(pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\bg.png'), (1300, 600))
        self.health2=Health2(3,0,12,32,32,32,self.img,self.bg)
        self.visible=True

        self.rect=self.char1.get_rect()
        self.rect.x=x
        self.rect.y=y

        #sound effect
        self.jumpSound=pygame.mixer.Sound(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\music\\maro-jump-sound-effect_1.mp3')
        self.deathSound=pygame.mixer.Sound(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\music\\super-mario-death-sound-sound-effect.mp3')
