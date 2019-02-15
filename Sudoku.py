WIDTH = 1100
HEIGHT = 650
CREDITS = 0
EXIT = 0
#it has to be 650 for the screen to fit on the size of the computer screen
#each box will be 66x66 in the board

def draw():
	global CREDITS
	global EXIT
	print(CREDITS)
	print(EXIT)
	screen.fill((255, 255, 255))
	blue = 190,210,230
	purple = 229,194,237
	black = 0,0,0
	if CREDITS != 0:
		screen.clear()
		
	else:
		#four different blue buttons
		play_button = Rect((750,50), (300,100))
		screen.draw.filled_rect(play_button, blue)
		screen.draw.rect(play_button,(0,0,0))
		instructions_button = Rect((750,200), (300,100))
		screen.draw.filled_rect(instructions_button, blue)
		screen.draw.rect(instructions_button,(0,0,0))
		credits_button = Rect((750,350), (300,100))
		screen.draw.filled_rect(credits_button, blue)
		screen.draw.rect(credits_button,(0,0,0))
		exit_button = Rect((750,500), (300,100))
		screen.draw.filled_rect(exit_button, blue)
		screen.draw.rect(exit_button,(0,0,0))
		#title
		title = Rect ((50,50), (625, 200))
		screen.draw.filled_rect(title, purple)
		screen.draw.rect(title,(0,0,0))
		#sudoku on home screen
		board = Actor('sudoku')
		board.pos = 350, 450
		board.draw()
		#text on butttons and title
		screen.draw.text("PLAY", (863,78), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("HOW TO PLAY", (755, 225), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("CREDITS", (806, 375), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("EXIT", (858, 525), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("ODD & EVEN", (150, 80), color = "black", fontname = "arial", fontsize = 65)
		screen.draw.text("SUDOKU", (222, 165), color = "black", fontname = "arial", fontsize = 65)

		if EXIT != 0:
			exit_popup = Rect((320,170), (500,350))
			screen.draw.filled_rect(exit_popup, blue)
			screen.draw.rect(exit_popup,(0,0,0))
			screen.draw.text("CLICK ANYWHERE\nTO CONTINUE\nPRESS CONTROL-Q\nCOMMAND-Q ON MAC\nTO EXIT THE GAME", (350,220), color = "black", fontname = "arial", fontsize = 42)
			EXIT = 0
			
			
def on_mouse_down(pos):
	global CREDITS
	global EXIT
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 50 and pos[1] < 150:
		print ("play button clicked")
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 200 and pos[1] < 300:
		print ("How to play button clicked")
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 350 and pos[1] < 450:
		CREDITS = 1
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 500 and pos[1] < 600:
		EXIT = 1

