import pygame

#Enemy
class Enemy(object):

    walkLeft=[pygame.image.load(r'D:\\Python\\my projects\\pygame\Wild Hare Run A Quest for Carrots\\sprites\\wolf\\runLeft\\1.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\Wild Hare Run A Quest for Carrots\\sprites\\wolf\\runLeft\\2.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\Wild Hare Run A Quest for Carrots\\sprites\\wolf\\runLeft\\3.png'),
              pygame.image.load(r'D:\\Python\\my projects\\pygame\Wild Hare Run A Quest for Carrots\\sprites\\wolf\\runLeft\\4.png')]
    walkRight=[pygame.image.load(r'D:\\Python\\my projects\\pygame\Wild Hare Run A Quest for Carrots\\sprites\\wolf\\runRight\\1.png'),
               pygame.image.load(r'D:\\Python\\my projects\\pygame\Wild Hare Run A Quest for Carrots\\sprites\\wolf\\runRight\\2.png'),
               pygame.image.load(r'D:\\Python\\my projects\\pygame\Wild Hare Run A Quest for Carrots\\sprites\\wolf\\runRight\\3.png'),
               pygame.image.load(r'D:\\Python\\my projects\\pygame\Wild Hare Run A Quest for Carrots\\sprites\\wolf\\runRight\\4.png')]
    char1=pygame.image.load(r'D:\\Python\\my projects\\pygame\Wild Hare Run A Quest for Carrots\\sprites\\wolf\\runRight\\1.png')
    char2=pygame.image.load(r'D:\\Python\\my projects\\pygame\Wild Hare Run A Quest for Carrots\\sprites\\wolf\\runLeft\\1.png')

    def __init__(self,x,y,width,height,end):
        self.reset(x,y,width,height,end)

    def draw(self,win):
        
        if self.visible:
            self.move()
            if self.walkCount+1>=4:
                self.walkCount=0
            
            if self.vel>0:
                win.blit(self.walkRight[self.walkCount],self.rect)
                self.walkCount+=1
            elif self.vel<0:
                win.blit(self.walkLeft[self.walkCount],self.rect)
                self.walkCount+=1

        self.hitbox=(self.x+17,self.y+2,31,57)
        #pygame.draw.rect(win,(255,255,255),self.rect,2)

    
    def move(self):
        if self.vel>0: #if velocity > 0 then move right
            if self.rect.x+self.vel<self.path[1]: #check if enemy reaches end point
                self.rect.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.walkCount=0
        else: #if velocity < 0 then move left
            if self.rect.x-self.vel>self.path[0]: #check if enemy is at starting point
                self.rect.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.walkCount=0

    def reset(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.vel=3

        self.path=[self.x,self.end]
        self.visible=True
        self.walkCount=0

        self.rect=self.char1.get_rect()
        self.rect.x=x
        self.rect.y=y
    