import pygame, sys                                   
pygame.init()  

WIDTH=800      
HEIGHT=0.85*WIDTH                                                   
size=(WIDTH,HEIGHT)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("OLYMPICS LOGO")

BLACK    = (0, 0, 0)                    
WHITE    = (255, 255, 255)
GREEN    = (0, 255, 0)
RED      = (255, 0, 0)
BLUE     = ( 0, 0, 255)
YELLOW = (255, 255, 0)

#Converts the screen into a 14 by 9 grid
xu = WIDTH/14
yu = HEIGHT/9

#FUNCTIONS
def Ring(x, y, color):
    pygame.draw.ellipse(surface, color, (x, y, 4*xu, 4*xu), 10)


def Arc(x, y, color, start, stop):
    pygame.draw.arc(surface, color, (x, y), start, stop, 3)


def showMessage(words, coords, font, font_size, color, bg=None):
    words_font = pygame.font.SysFont(font, font_size, True, False)
    text_image = words_font.render(words, True, color, bg)
    #get a bounding box for centering
    text_bounds = text_image.get_rect()
    #center text - change center of ret to location
    text_bounds.center = coords
    surface.blit(text_image, text_bounds)


def draw_olympics():
    Ring(0,       4.5*yu, BLUE)
    Ring(4.75*xu, 4.5*yu, BLACK)
    Ring(9.5*xu,  4.5*yu, RED)
    Ring(2.3*xu,  6*yu, YELLOW)
    Ring(7.1*xu,  6*yu, GREEN)
    showMessage("2024 Summer Olympics- Paris, France", (WIDTH/2, yu), "Ariel", 60, BLACK)
    

# -------- Main Program Loop -----------
def main():                                           
    while True:
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #end game
                pygame.quit()                          
                sys.exit()

        surface.fill(WHITE)  
        
        draw_olympics()
        
        pygame.display.update() 
#----------------------------------------------------------------            
main()                                                   #runs the game