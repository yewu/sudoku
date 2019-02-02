WIDTH = 1100
HEIGHT = 650
#it has to be 650 for the screen to fit on the size of the computer screen
#each box will be 66x66 in the board

def draw():
    screen.fill((255, 255, 255))
    blue = 190,210,230
    purple = 229,194,237
    black = 0,0,0
    #four different blue buttons
    play_button = Rect((750,50), (300,100))
    screen.draw.filled_rect(play_button, blue)
    instructions_button = Rect((750,200), (300,100))
    screen.draw.filled_rect(instructions_button, blue)
    credits_button = Rect((750,350), (300,100))
    screen.draw.filled_rect(credits_button, blue)
    exit_button = Rect((750,500), (300,100))
    screen.draw.filled_rect(exit_button, blue)
    #title
    title = Rect ((50,50), (625, 200))
    screen.draw.filled_rect(title, purple)
    #sudoku on home screen
    board = Actor('sudoku')
    board.pos = 350, 450
    board.draw()
    #text on butttons and title
    screen.draw.text("PLAY", (843,78), color = "black", fontname = "arial", fontsize = 42)
    screen.draw.text("HOW TO PLAY", (755, 225), color = "black", fontname = "arial", fontsize = 42)
    screen.draw.text("CREDITS", (803, 375), color = "black", fontname = "arial", fontsize = 42)
    screen.draw.text("EXIT", (853, 520), color = "black", fontname = "arial", fontsize = 42)

"""
    blue = 190,210,230
    pretend_board = Rect((28,28), (594,594))
    screen.draw.filled_rect(pretend_board, blue)
    #The box represents the board
    #we can do a rectangle sprite for each small box in the board
"""

    
