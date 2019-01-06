import pygame
pygame.init()

white = [255,255,255]
black = [0,0,0]
blue = [190,210,230]
purple = [229,194,237]

bright_blue = [210,230,250]

(width, height) = (1300, 1000)
screen = pygame.display.set_mode((width, height))
screen.fill(white)

pygame.display.set_caption("Even and Odd Sudoku")
pygame.display.update()

def main():
    home()

def home():
    mouse = pygame.mouse.get_pos() # doesn't work
    print (mouse)
    pygame.draw.rect(screen, blue,(900, 100, 350, 125))
    pygame.draw.rect(screen, blue,(900, 325, 350, 125))
    pygame.draw.rect(screen, blue,(900, 550, 350, 125))
    pygame.draw.rect(screen, blue,(900, 775, 350, 125))
    pygame.draw.rect(screen, purple,(100, 110, 650, 300))
    pygame.display.update()

    while 900 + 350 > mouse[0] > 900 and 100 + 125 > mouse [1] > 100:
        pygame.draw.rect(screen, bright_blue,(900, 100, 350, 125))
        pygame.draw.rect(screen, blue,(900, 325, 350, 125))
        pygame.draw.rect(screen, blue,(900, 550, 350, 125))
        pygame.draw.rect(screen, blue,(900, 775, 350, 125))
        pygame.display.update()

    while 900 + 350 > mouse[0] > 900 and 325 + 125 > mouse [1] > 325:
        pygame.draw.rect(screen, blue,(900, 100, 350, 125))
        pygame.draw.rect(screen, bright_blue,(900, 325, 350, 125))
        pygame.draw.rect(screen, blue,(900, 550, 350, 125))
        pygame.draw.rect(screen, blue,(900, 775, 350, 125))
        pygame.display.update()

    while 900 + 350 > mouse[0] > 900 and 550 + 125 > mouse [1] > 550:
        pygame.draw.rect(screen, blue,(900, 100, 350, 125))
        pygame.draw.rect(screen, blue,(900, 325, 350, 125))
        pygame.draw.rect(screen, bright_blue,(900, 550, 350, 125))
        pygame.draw.rect(screen, blue,(900, 775, 350, 125))
        pygame.display.update()

    while 900 + 350 > mouse[0] > 900 and 775 + 125 > mouse [1] > 775:
        pygame.draw.rect(screen, blue,(900, 100, 350, 125))
        pygame.draw.rect(screen, blue,(900, 325, 350, 125))
        pygame.draw.rect(screen, bright_blue,(900, 550, 350, 125))
        pygame.draw.rect(screen, blue,(900, 775, 350, 125))
        pygame.display.update()
    
main()
        
