import pygame
class Health2(object):
    def __init__(self,val,x,y,width,height,pos,img,bg):
        self.val=val
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.pos=pos
        self.delete=False
        self.health=[]
        self.HeartSprite=img
        self.health+=self.val*[self.HeartSprite]
        self.bg=bg
        
    def draw(self,win):
        if self.delete:
            #self.health=[]
            #self.health=self.val*[self.HeartSprite]
            self.health.pop()
            self.val-=1
            
            self.x=10 
            win.blit(self.bg,(0,0))

        for i in self.health:
            
            win.blit(i,(self.x,self.y))
            self.x+=self.pos
            
        self.x=self.pos
            
        
        