#player
from files.health import *
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
        self.health=Health1(10)
        self.visible=True

    def draw(self,win):
        pygame.time.delay(27)
        if self.visible:
            if self.walkCount+1>=8:
                self.walkCount=0

            if not(self.standing):
                if self.left:
                    win.blit(self.walkLeft[self.walkCount],(self.x,self.y))
                    self.walkCount+=1
                elif self.right:
                    win.blit(self.walkRight[self.walkCount],(self.x,self.y))
                    self.walkCount+=1
            else:
                if self.right:
                    win.blit(self.char1,(self.x,self.y))
                elif self.left:
                    win.blit(self.char2,(self.x,self.y))
                else:
                    if self.direc==1:
                            win.blit(self.char1,(self.x,self.y))
                    elif self.direc==-1:
                        win.blit(self.char2,(self.x,self.y))
                    else:
                        win.blit(self.char1,(self.x,self.y))

        self.hitbox=(self.x+17,self.y+11,29,52) #set position every movement


#blocks
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

    def draw(self,win):
        win.blit(self.grass,(self.x,self.y))
        #pygame.display.update()

    def checkCollide(self,player):
        # Handle collision between player and block
        if player.x<self.x and player.x<self.x+self.width:
            if player.y>self.y-self.height:
                return True
            else:
                return False
        else:
            return False

#start
from files.player import *
from files.blocks import *
import pygame
pygame.init()
#Objects
rabbit=Player(0,480,63,57)
lvl1=[Block(200,380,64,64),Block(284,380,64,64)]

class Start(object):
    

    def __init__(self):
        self.WIDTH=1300
        self.HEIGHT=600
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        #setting up environment
        self.ground=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\ground blocks\\ground.png')
        self.bg=pygame.transform.scale(pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\bg.png'), (self.WIDTH, self.HEIGHT))

        self.bgSound1=r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\music\\sound1.mp3'
        self.bgSound2=r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\music\\sound2.mp3'

    #main function
    def main(self,music):
        running=True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys=pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and rabbit.x>rabbit.vel: 
                rabbit.x-=rabbit.vel
                rabbit.left=True
                rabbit.right=False
                rabbit.standing=False
                rabbit.direc=-1
                for i in lvl1:
                    if i.checkCollide(rabbit):
                        rabbit.y=i.y-i.height
                    else:
                        rabbit.y=480
            elif keys[pygame.K_RIGHT] and rabbit.x<self.WIDTH-rabbit.width-rabbit.vel:
                rabbit.x+=rabbit.vel
                rabbit.left=False
                rabbit.right=True
                rabbit.standing=False
                rabbit.direc=1
                for i in lvl1:
                    if i.checkCollide(rabbit):
                        rabbit.y=i.y-i.height
                    else:
                        rabbit.y=480
            else:
                rabbit.runCount=0
                rabbit.standing=True

            #Jump
            if(not(rabbit.isJump)):

                if keys[pygame.K_SPACE]:
                    rabbit.isJump=True
                    rabbit.left=False
                    rabbit.right=False
                    rabbit.runCount=0
            else:
                if rabbit.jumpCount>=-10:
                    neg=1
                    if rabbit.jumpCount<0:
                        neg=-1
                    rabbit.y-=rabbit.jumpCount**2 * 0.5 * neg
                    rabbit.jumpCount-=1
                else:
                    rabbit.isJump=False
                    rabbit.jumpCount=10

            

            self.reDrawFunc()
            
            pygame.display.update()

    def reDrawFunc(self):
        self.win.blit(self.bg,(0,0))
        self.win.blit(self.ground,(0,500))
        for grassy in lvl1:
            grassy.draw(self.win)
        rabbit.draw(self.win)


#main
import pygame
from files.start import *
 
# Initialize Pygame
pygame.init()

# Set up the display
WIDTH=1300
HEIGHT=600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wild Hare Run: A Quest for Carrots")
clock=pygame.time.Clock()

# Set up the fonts
title_font = pygame.font.Font(None, 80)
button_font = pygame.font.Font(None, 40)

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# Set up music
bgSound1=r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\music\\sound1.mp3'
bgSound2=r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\music\\sound2.mp3'
music=pygame.mixer.music.load(bgSound1)
pygame.mixer.music.play(1)

# Set up background
bg=pygame.transform.scale(pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\bg.png'), (WIDTH, HEIGHT))
hare1=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\main menu\\sleep.png')
hare2=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\main menu\\sleep(1).png')
pos=(500,100)

# Set up the buttons
start_button = pygame.Rect(300, 250, 200, 50)
start_text = button_font.render("Start", True, black)
start_text_rect = start_text.get_rect(center=start_button.center)

quit_button = pygame.Rect(300, 350, 200, 50)
quit_text = button_font.render("Quit", True, black)
quit_text_rect = quit_text.get_rect(center=quit_button.center)

# Set up objects
start1=Start()

# Set up the game loop
running = True
while running:
    clock.tick(27)
    # Handle events
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                # Start game
                start1.main(music)
                print("Starting game...")
            elif quit_button.collidepoint(event.pos):
                # Quit game
                running = False

    # Clear the screen
    screen.blit(bg,(0,0))
    screen.blit(hare1,pos)

    # Draw the title
    title_text = title_font.render("Wild Hare Run: A Quest for Carrots", True, black)
    title_position = title_text.get_rect(center=(650, 70))
    screen.blit(title_text, title_position)

    # Draw the buttons
    pygame.draw.rect(screen, gray, start_button)
    pygame.draw.rect(screen, gray, quit_button)
    screen.blit(start_text, start_text_rect)
    screen.blit(quit_text, quit_text_rect)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
