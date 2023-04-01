import pygame
class Carrot(object):

    def __init__(self,x,y,width,height):
        self.reset(x,y,width,height)
    
    def draw(self,win):
        win.blit(self.img,(self.x,self.y))

    def collide(self,player):
        if (player.x>self.x and player.x<self.x+self.width) or (player.y<self.y and player.y>self.y+self.height):
            print("deleted")
            return True
        return False
    
    def reset(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

        self.img=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\carrot\\carrot.png')
        self.rect=self.img.get_rect()
        self.rect.x=x
        self.rect.y=y
        