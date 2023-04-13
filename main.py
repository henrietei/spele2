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
guesses=[]
#input_y=95

def draw_rect(x,y):
    pygame.draw.rect(screen, green, pygame.Rect(x, y, 60, 60))
    pygame.display.flip()

def surface1():
    for i in range (5):
        for i1 in range (6):
            pygame.draw.rect(screen, gray1, (100+i*85, 105+100*i1, 60, 90))


with open('words.txt', 'r',  encoding="utf-8") as g:
    lines = g.readlines()

b = random.randint(0, len(lines)-1)
a = lines[b]

print(a)

pygame.init()
  
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 800])
base_font = pygame.font.Font("SourceCodePro-ExtraBold.ttf", 72)
user_text = ''
user_text2=""
w_font=pygame.font.Font("SourceCodePro-ExtraBold.ttf", 28)

#txtsurf = base_font.render("Hello, World", True, black)

#surface1()

screen.fill(gray)

minejums="0"

input_rect = pygame.Rect(100, 95, 225, 72) 

for guess in range(5):
    print(guess)
    while minejums=="0":
        surface1()
        #input_rect = pygame.Rect(100, 95, 225, 72)    
        for event in pygame.event.get():
        # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RETURN:
                    if len(user_text)==10:
                        minejums=user_text.replace(" ", "")
                        print(minejums)
                        pygame.draw.rect(screen, gray, (0, 0, 600, 100))
                        guesses.append(minejums)
                        minejums="0"
                        
                        
                    else: 
                        warning = w_font.render("Nepietiekami daudz burtu", True, black)
                        screen.blit(warning,(100, 60))
                        #time.sleep(2)
                        


                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-2]
                    
                else:
                    if len(user_text)<=9:
                        if ord(event.unicode)>65:
                            user_text += event.unicode + " " 

        txtsurf = base_font.render(user_text, True, black)
        screen.blit(txtsurf,(105, 100))
        pygame.display.flip()

        

        
        #pygame.display.update()
        #text_surface = base_font.render(user_text, True, black)
        #screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))


        
        clock.tick(60)

    


    



      
  
      
