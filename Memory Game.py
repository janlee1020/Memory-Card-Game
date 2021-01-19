import pygame
import time
import random
pygame.init()
pygame.font.init() 

#SET UP THE SCREEN
width, height = 900, 600
screen = pygame.display.set_mode((width,height))
font = pygame.font.SysFont("comicsans", 29)
pygame.display.set_caption(("Memory Card Game"))

#COLORS
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
orange = (255, 175 ,0)
yellow = (235, 235 ,0)

attempts = 5
level = "Easy"
screen.fill(white)
pygame.display.update()

#FIRST SCREEN SHOWING DIFFICULTY
def first_page(screen): 
    first_screen = pygame.display.set_mode((width,height))
    first_screen.fill(white)
    first_font = pygame.font.SysFont("comicsans", 40)
    level_font = pygame.font.SysFont("comicsans", 50)
    initlevel_text = level_font.render("CHOOSE YOUR LEVEL OF DIFFICULTY", 1, black)

    #DRAW RECTANGLES
    pygame.draw.rect(first_screen, green, (350,250,200,75))             #EASY RECTANGLE
    pygame.draw.rect(first_screen, yellow, (350,350,200,75))            #MEDIUM RECTANGLE
    pygame.draw.rect(first_screen, orange, (350,450,200,75))            #HARD RECTANGLE

    #DRAW TEXT
    easy_text = first_font.render("EASY", 1, black)
    medium_text = first_font.render("MEDIUM", 1, black)
    hard_text = first_font.render("HARD", 1, black)
    first_screen.blit(initlevel_text, (135, 130))
    first_screen.blit(easy_text, (410, 275))
    first_screen.blit(medium_text, (400, 375))
    first_screen.blit(hard_text, (410, 475))
    pygame.display.update() 


first_page(screen)

#DRAW TEXT
def redirect_window(screen): 
    attempts_text = font.render(f"Attempts: {attempts}", 1, black)
    level_text = font.render(f"Level: {level}", 1, black)
    easygame_text = font.pygame.font.render(f"Mode: Easy", 1, black)
    screen.blit(attempts_text, (200, 15))
    screen.blit(level_text, (600, 15))
    screen.blit(easygame_text, (400,15))
    pygame.display.update()



running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y)= pygame.mouse.get_pos()
            if event.button == 1:  # Left mouse button.
                    # Check if the rect collides with the mouse pos.
                if (x >= 350) :
                    redirect_window(screen)
                        #easyrect = pygame.draw.rect(first_screen, green, (350,250,200,75)) 








