import pygame
class Collected(object):
    def __init__(self,img,val):
        self.img=img
        self.val=val
        self.font=pygame.font.SysFont('comicsans',20,True,True) #SysFont('name of font',size of font,bold,italic)

    def draw(self,win,x,y,visible):
        self.text=self.font.render('Collected     :'+str(self.val),2,(255,0,0)) #font.render('text to be displayed',1,(color))
        if visible: 
            win.blit(self.text,(x+32,y))
            win.blit(self.img,((x+132),y))
