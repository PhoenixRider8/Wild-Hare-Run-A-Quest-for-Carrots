import pygame
from files.start import *

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH=1300
HEIGHT=600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wild Hare Run: A Quest for Carrots")

icon_img=r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\game logo\\gamelogo(1).PNG'
icon=pygame.image.load(icon_img)
icon_surface = pygame.Surface((32, 32))
icon_surface.blit(icon, (0, 0))
pygame.display.set_icon(icon)

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
                start1.main()
                pygame.display.quit()
                #print("Starting game...")
            elif quit_button.collidepoint(event.pos):
                # Quit game
                running = False

    # Clear the screen
    screen.blit(bg,(0,0))
    screen.blit(hare1,pos)

    # Draw the title
    title_text = title_font.render("Wild Hare Run: A Quest for Carrots", True, gray)
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
