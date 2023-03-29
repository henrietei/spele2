import pygame
import sys
import time
import random



with open('words.txt', 'r',  encoding="utf-8") as g:
    lines = g.readlines()


b = random.randint(0, len(lines)-1)
a = lines[b]

print(a)

black = (0,0,0)
white = (255, 255, 255)
gray = (230, 230, 230)
gray1 = (220, 220, 220)
yellow = (255, 255, 0)
green = (0, 255, 0)  
 
# pygame.init() will initialize all
# imported module
pygame.init()
  
clock = pygame.time.Clock()
  
# it will display on screen
screen = pygame.display.set_mode([600, 700])
  
# basic font for user typed
base_font = pygame.font.Font("SourceCodePro-ExtraBold.ttf", 72)
user_text = ''
  
# create rectangle
input_rect = pygame.Rect(100, 95, 225, 72)
  
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
#color_active = white
  
# color_passive store color(chartreuse4) which is
# color of input box.
#color_passive = gray1
#color = color_passive
  
active = False
  
while True:
    for event in pygame.event.get():
      # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
  
        if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-2]
  
            # Unicode standard is used for string
            # formation
            else:
                if len(user_text)<=9:
                    if event.unicode != "'":
                        user_text += event.unicode + " " 
                
      
    # it will set background color of screen
    screen.fill(gray)
  
    """if active:
        color = color_active
    else:
        color = color_passive"""
          
    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen, gray1, (100, 105, 405, 90))
    pygame.draw.rect(screen, gray1, (100, 205, 405 , 90))
    pygame.draw.rect(screen, gray1, (100, 305, 405, 90))
    pygame.draw.rect(screen, gray1, (100, 405, 405, 90))
    pygame.draw.rect(screen, gray1, (100, 505, 405, 90))
    #pygame.draw.rect(screen, color, (100, 610, 225, 72))
  
    text_surface = base_font.render(user_text, True, black)

      
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    
        
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:  
           print(user_text)
           time.sleep(1)
           for i in range (5):
            if user_text.find(a[i]) == -1: 
               print("nav")


    



      
  
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    #input_rect.w = max(100, 155)
      
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()
      
    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)
    