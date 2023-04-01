import pygame
from files.glitch import *
from files.hack1 import *
from files.hack2 import *
from files.troll import *
#pygame.init()

class Start4(object):

    def __init__(self):
        self.WIDTH=1300
        self.HEIGHT=600
        # Set up background
        self.bg=pygame.transform.scale(pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\bg.png'), (self.WIDTH, self.HEIGHT))
        self.hare1=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\main menu\\sleep.png')
        self.hare2=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\main menu\\sleep(1).png')
        self.pos=(500,100)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.title_font = pygame.font.Font(None, 80)
        self.button_font = pygame.font.Font(None, 40)

        # Set up the colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gray = (128, 128, 128)
        self.red= (255,0,0)
        # Set up the buttons
        self.start_button = pygame.Rect(300, 250, 200, 50)
        self.start_text = self.button_font.render("Start", True, self.black)
        self.start_text_rect = self.start_text.get_rect(center=self.start_button.center)

        self.quit_button = pygame.Rect(300, 350, 200, 50)
        self.quit_text = self.button_font.render("Quit", True, self.black)
        self.quit_text_rect = self.quit_text.get_rect(center=self.quit_button.center)
        self.title_text = self.title_font.render("Wild Hare Run: A Quest for Carrots", True, self.red)

        # Set up music
        self.bgSound2=r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\music\\sound2.mp3'
        self.music2=pygame.mixer.Sound(self.bgSound2)

        # Set up Glitch
        self.glitch_vid=r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\videos\\Comp 1.mp4'
        self.glitch2=Glitch(self.glitch_vid)

        # Set up Hacks
        self.hacking1_vid=r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\videos\\cmd_1.mp4'
        self.hacking1=Hack1(self.hacking1_vid)
        self.hacking2=Hack2()

        # Set up Troll
        self.trolled_vid=r"D:\\Python\\tutorials\\pygame\\video\\troll\\You've been trolled.mp4"
        self.trolled=Troll(self.trolled_vid)

        # Set up Icon
        self.icon_img=r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\game logo\\gamelogo(2).PNG'
        self.icon=pygame.image.load(self.icon_img)
        self.icon_surface = pygame.Surface((32, 32))
        self.icon_surface.blit(self.icon, (0, 0))
        
        

    def main(self):
        
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Wild Hare Run: A Quest for Carrots")
        self.music2.play()
        running=True
        while running:
            # Handle events
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.collidepoint(event.pos):
                        # Start game
                        # print("boom")
                        self.glitch2.main()
                        self.hacking1.main()
                        self.hacking2.main()
                        self.trolled.main()
                        pygame.display.quit()
                        
                    elif self.quit_button.collidepoint(event.pos):
                        # Quit game
                        pygame.quit()
                        running = False

            # Clear the screen
            self.screen.blit(self.bg,(0,0))
            self.screen.blit(self.hare2,self.pos)

            # Draw the title
            
            self.title_position = self.title_text.get_rect(center=(650, 70))
            self.screen.blit(self.title_text, self.title_position)

            # Draw the buttons
            pygame.draw.rect(self.screen, self.gray, self.start_button)
            pygame.draw.rect(self.screen, self.gray, self.quit_button)
            self.screen.blit(self.start_text, self.start_text_rect)
            self.screen.blit(self.quit_text, self.quit_text_rect)

            # Update the screen
            pygame.display.flip()