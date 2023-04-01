import pygame

#Blocks
class Block(object):

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.grass=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\ground blocks\\grass.png')
        self.hitbox=(self.x+17,self.y+11,29,52)

        self.rectW=self.grass.get_width()
        self.rectH=self.grass.get_height()-23
        self.rect=pygame.Rect(self.x,self.y+23,self.rectW,self.rectH)

    def draw(self,win):
        win.blit(self.grass,(self.x,self.y))
        #pygame.draw.rect(win,(255,255,255),self,2)
        #pygame.display.update()

    