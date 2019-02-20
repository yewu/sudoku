WIDTH = 1100
HEIGHT = 650
HOME = 0
CREDITS = 0
HOWTO = 0
EXIT = 0
BACK = 0
PLAY = 0
#it has to be 650 for the screen to fit on the size of the computer screen
#each box will be 66x66 in the board

def draw():
	global HOME
	global CREDITS
	global HOWTO
	global EXIT
	global BACK
	global PlAY

	screen.fill((255, 255, 255))
	blue = 190, 210, 230
	purple = 229, 194, 237
	black = 0, 0, 0

	if CREDITS != 0:
		HOME = 2
		screen.clear()
		screen.fill((255, 255, 255))
		#credits titles tingky
		credits = Rect ((50, 50), (350, 100))
		screen.draw.filled_rect(credits, purple)
		screen.draw.rect(credits, black)
		screen.draw.text("CREDITS", (75, 67), color = "black", fontname = "arial", fontsize = 65)
		back_button = Rect((750, 50), (300, 100))
		screen.draw.filled_rect(back_button, blue)
		screen.draw.rect(back_button, black)
		screen.draw.text("BACK", (850, 78), color = "black", fontname = "arial", fontsize = 42)
	
	elif PLAY != 0:
		HOME = 4
		screen.clear()
		screen.fill((255,255,255))
		heading = Rect((50,50), (650,100))
		screen.draw.filled_rect(heading, purple)
		screen.draw.rect(heading,(0,0,0))
		back = Rect((750,50), (300,100))
		screen.draw.filled_rect(back, blue)
		screen.draw.rect(back,(0,0,0))
		Extreme = Rect((750,200), (300,150))
		screen.draw.filled_rect(Extreme, blue)
		screen.draw.rect(Extreme,(0,0,0))
		Normal = Rect((400,200), (300,150))
		screen.draw.filled_rect(Normal, blue)
		screen.draw.rect(Normal,(0,0,0))
		Easy = Rect((50,200), (300,150))
		screen.draw.filled_rect(Easy, blue)
		screen.draw.rect(Easy,(0,0,0))
		screen.draw.text("CHOOSE A LEVEL", (95, 67), color = "black", fontname = "arial", fontsize = 65)
		screen.draw.text("BACK", (850, 78), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("Easy", (150, 210), color = "black", fontname = "arial", fontsize = 50)	
		screen.draw.text("SOPHIA", (140, 262), color = "black", fontname = "arial", fontsize = 35)
		screen.draw.text("(EXAMPLE BELOW)", (51, 300), color = "black", fontname = "arial", fontsize = 32)	
		screen.draw.text("NORMAL", (450, 210), color = "black", fontname = "arial", fontsize = 50)	
		screen.draw.text("ELINA", (508, 262), color = "black", fontname = "arial", fontsize = 35)
		screen.draw.text("(EXAMPLE BELOW)", (401, 300), color = "black", fontname = "arial", fontsize = 32)
		screen.draw.text("EXTREME", (780, 210), color = "black", fontname = "arial", fontsize = 50)	
		screen.draw.text("CELINE", (834, 262), color = "black", fontname = "arial", fontsize = 35)
		screen.draw.text("(EXAMPLE BELOW)", (751, 300), color = "black", fontname = "arial", fontsize = 32)	
		board = Actor('easy')
		board.pos = 200, 500
		board.draw()
		'''
		board = Actor('normal')
		board.pos = 500, 500
		board.draw()
		'''
	elif HOWTO != 0:
		HOME = 3
		screen.clear()
		screen.fill((255, 255, 255))
		#credits titles tingky
		credits = Rect ((50, 50), (500, 100))
		screen.draw.filled_rect(credits, purple)
		screen.draw.rect(credits, black)
		screen.draw.text("HOW TO PLAY", (75, 67), color = "black", fontname = "arial", fontsize = 65)
		back_button = Rect((750, 50), (300, 100))
		screen.draw.filled_rect(back_button, blue)
		screen.draw.rect(back_button, black)
		screen.draw.text("BACK", (850, 78), color = "black", fontname = "arial", fontsize = 42)
	
	elif BACK != 0 or CREDITS == 0 or HOWTO == 0:
		HOME = 1
		screen.clear()
		screen.fill((255, 255, 255))
		#four different blue buttons
		play_button = Rect((750, 50), (300, 100))
		screen.draw.filled_rect(play_button, blue)
		screen.draw.rect(play_button, black)
		instructions_button = Rect((750, 200), (300, 100))
		screen.draw.filled_rect(instructions_button, blue)
		screen.draw.rect(instructions_button, black)
		credits_button = Rect((750, 350), (300, 100))
		screen.draw.filled_rect(credits_button, blue)
		screen.draw.rect(credits_button, black)
		exit_button = Rect((750, 500), (300, 100))
		screen.draw.filled_rect(exit_button, blue)
		screen.draw.rect(exit_button, black)
		#title
		title = Rect ((50, 50), (625, 200))
		screen.draw.filled_rect(title, purple)
		screen.draw.rect(title,black)
		#sudoku on home screen
		board = Actor('sudoku')
		board.pos = 350, 450
		board.draw()
		#text on butttons and title
		screen.draw.text("PLAY", (845, 78), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("HOW TO PLAY", (755, 225), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("CREDITS", (806, 375), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("EXIT", (858, 525), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("ODD & EVEN", (150, 80), color = "black", fontname = "arial", fontsize = 65)
		screen.draw.text("SUDOKU", (222, 165), color = "black", fontname = "arial", fontsize = 65)

		if EXIT != 0:
			exit_popup = Rect((320, 170), (500, 350))
			screen.draw.filled_rect(exit_popup, blue)
			screen.draw.rect(exit_popup,black)
			screen.draw.text("CLICK ANYWHERE\nTO CONTINUE\nPRESS CONTROL-Q\nCOMMAND-Q ON MAC\nTO EXIT THE GAME", (350,220), color = "black", fontname = "arial", fontsize = 42)
			EXIT = 0
			
			
def on_mouse_down(pos):
	global HOME
	global CREDITS
	global HOWTO
	global EXIT
	global BACK
	global PLAY
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 50 and pos[1] < 150 and HOME == 1:
		PLAY = 1
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 50 and pos[1] < 150 and HOME == 2:
		BACK = 1
		CREDITS = 0
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 50 and pos[1] < 150 and HOME == 3:
		BACK = 1
		HOWTO = 0
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 50 and pos[1] < 150 and HOME == 4:
		BACK = 1
		PLAY = 0
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 200 and pos[1] < 300 and HOME == 1:
		print ("How to play button clicked")
		HOWTO = 1
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 350 and pos[1] < 450 and HOME == 1:
		CREDITS = 1
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 500 and pos[1] < 600 and HOME == 1:
		EXIT = 1

