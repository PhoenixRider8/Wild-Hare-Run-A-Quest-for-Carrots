import pygame
class Door(object):
    doorOpen=[pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\door\\1.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\door\\2.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\door\\3.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\door\\4.png')]

    def __init__(self,x,y,width,height,val):
        self.reset(x,y,width,height,val)
        self.clock=pygame.time.Clock()

    def draw(self,win):
        if self.val==3 and self.count!=3:
            win.blit(self.doorOpen[self.count],self.rect)
            self.count+=1
        if self.count!=3:
            win.blit(self.doorOpen[0],self.rect)
        else:
            win.blit(self.doorOpen[3],self.rect)

        #pygame.draw.rect(win,(255,255,255),self.rect,2)

    def reset(self,x,y,width,height,val):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.val=val
        self.count=0

        self.rect=self.doorOpen[0].get_rect()
        self.rect.x=x
        self.rect.y=y


    def passThrough(self,player):
        if self.val==3 and player.rect.x>self.rect.x:
            return True
