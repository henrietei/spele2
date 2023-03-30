import pygame
import sys
import time
import random

black = (0,0,0)
white = (255, 255, 255)
gray = (230, 230, 230)
gray1 = (220, 220, 220)
yellow = (255, 255, 0)
green = (0, 255, 0)  
 

def draw_rect(x,y):
    pygame.draw.rect(screen, green, pygame.Rect(x, y, 60, 60))
    pygame.display.flip()



def surface():
    pygame.draw.rect(screen, gray1, (100, 105, 60, 90))
    pygame.draw.rect(screen, gray1, (185, 105, 60, 90))
    pygame.draw.rect(screen, gray1, (270, 105, 60, 90))
    pygame.draw.rect(screen, gray1, (355, 105, 60, 90))
    pygame.draw.rect(screen, gray1, (440, 105, 60, 90))
    pygame.draw.rect(screen, gray1, (100, 205, 405 , 90))
    pygame.draw.rect(screen, gray1, (100, 305, 405, 90))
    pygame.draw.rect(screen, gray1, (100, 405, 405, 90))
    pygame.draw.rect(screen, gray1, (100, 505, 405, 90))
#pygame.draw.rect(screen, color, (100, 610, 225, 72))


with open('words.txt', 'r',  encoding="utf-8") as g:
    lines = g.readlines()

b = random.randint(0, len(lines)-1)
a = lines[b]

print(a)


pygame.init()
  


clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 700])
base_font = pygame.font.Font("SourceCodePro-ExtraBold.ttf", 72)
user_text = ''
input_rect = pygame.Rect(100, 95, 225, 72)
  

  
active = False

screen.fill(gray)

surface()
while True:
    for event in pygame.event.get():
      # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-2]
                print("kgghh")
                screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                

            else:
                if len(user_text)<=9:
                    if event.unicode != "'":
                        user_text += event.unicode + " " 
                
      
    # it will set background color of screen
    
  
    """if active:
        color = color_active
    else:
        color = color_passive"""
          
    # draw rectangle and argument passed which should
    # be on screen
    """pygame.draw.rect(screen, gray1, (100, 105, 405, 90))
    pygame.draw.rect(screen, gray1, (100, 205, 405 , 90))
    pygame.draw.rect(screen, gray1, (100, 305, 405, 90))
    pygame.draw.rect(screen, gray1, (100, 405, 405, 90))
    pygame.draw.rect(screen, gray1, (100, 505, 405, 90))
    #pygame.draw.rect(screen, color, (100, 610, 225, 72))"""
  
    text_surface = base_font.render(user_text, True, black)
    #pygame.draw.rect(screen, black, input_rect)
      
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    
    """if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:  
           print(user_text)
           time.sleep(1)
           for i in range (5):
                if user_text.find(a[i])== -1:
                    
                    print("nav")
                if user_text.find(a[i]) != -1: 
                    print(i, "ir")
                    #diceDisplay = base_font.render(str(user_text[i]), 1, black)
                    #screen.blit(diceDisplay, (520, 30))
                    draw_rect(i, i+100)
"""
               
               



    



      
  
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    #input_rect.w = max(100, 155)
      
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()
      
    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)
    