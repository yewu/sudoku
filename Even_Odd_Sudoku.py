def main():
    import pygame
    pygame.init()
    black = (0,0,0)
    grey = (220,220,220)
    white = (255,250,250)
    blue = (190,210,230)
    purple = (229,194,237)
    size = (1200, 1000)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Even and Odd Sudoku")
    home()

def home():
    pygame.draw.rect (gameDisplay, blue, (800, 30, 300, 150))
    
main()
        
