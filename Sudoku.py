import pgzrun #run pygame zero w/o using terminal!

WIDTH = 1100
HEIGHT = 650
HOME = 0
CREDITS = 0
HOWTO = 0
EXIT = 0
BACK = 0
PLAY = 0
LEVEL = 0
EASY = 0
NORMAL = 0
EXTREME = 0
#it has to be 650 for the screen to fit on the size of the computer screen
#each box will be 66x66 in the board

def draw():
	global HOME
	global CREDITS
	global HOWTO
	global EXIT
	global BACK
	global PLAY
	global LEVEL
	global EASY
	global NORMAL
	global EXTREME

	screen.fill((255, 255, 255))
	blue = 190, 210, 230
	purple = 229, 194, 237
	black = 0, 0, 0
	white = 255, 255, 255
	grey = 238, 238, 238

	if CREDITS != 0:
		HOME = 2
		screen.clear()
		screen.fill((255, 255, 255))
		#credits title
		credits = Rect ((50, 50), (350, 100))
		screen.draw.filled_rect(credits, purple)
		screen.draw.rect(credits, black)
		screen.draw.text("CREDITS", (75, 67), color = "black", fontname = "arial", fontsize = 65)
		back_button = Rect((750, 50), (300, 100))
		screen.draw.filled_rect(back_button, blue)
		screen.draw.rect(back_button, black)
		screen.draw.text("BACK", (850, 78), color = "black", fontname = "arial", fontsize = 42)
		credits_text = Rect ((50, 180), (1000, 450))
		screen.draw.filled_rect(credits_text, white)
		screen.draw.rect(credits_text, black)
		screen.draw.text("-  Home screen image: https://tinyurl.com/y9cbazvx\n-  Play screen examples: https://tinyurl.com/ybzp7bjw\n-  Boards: https://tinyurl.com/y9onnnsp\n-  Inspiration: https://tinyurl.com/ycw6n2hv", (75, 200), color = "black", fontname = "arial", fontsize = 38)
		screen.draw.text("Made by: Elina Lee, Sophia Liang, Celine Wu", (270, 550), color = "black", fontname = "arial", fontsize = 38)
	
	elif PLAY != 0:
		HOME = 4
		LEVEL = 1
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
		screen.draw.text("EASY", (140, 210), color = "black", fontname = "arial", fontsize = 50)	
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
		board = Actor('normal')
		board.pos = 550, 500
		board.draw()
		board = Actor('extreme')
		board.pos = 900, 500
		board.draw()
		
	elif HOWTO != 0:
		HOME = 3
		screen.clear()
		screen.fill((255, 255, 255))
		howto = Rect ((50, 50), (500, 100))
		screen.draw.filled_rect(howto, purple)
		screen.draw.rect(howto, black)
		back_button = Rect((750, 50), (300, 100))
		screen.draw.filled_rect(back_button, blue)
		screen.draw.rect(back_button, black)
		howto_text = Rect ((50, 180), (1000, 450))
		screen.draw.filled_rect(howto_text, white)
		screen.draw.rect(howto_text, black)
		screen.draw.text("HOW TO PLAY", (75, 67), color = "black", fontname = "arial", fontsize = 65)
		screen.draw.text("BACK", (850, 78), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("1.  Each row and column must contain the numbers from\n1-9 (cannot repeat numbers).\n2.  Each 3x3 box with a darker outline must also contain the\nnumbers from 1-9 (cannot repeat numbers).\n3.  In the shaded boxes, the number must be even. In the unshaded\nboxes, the numbers have to be odd.\n4.  If you need a hint, click the 'Hint' button.\n5.  If you want to check your answers after you are finished, press\nthe 'Check' button.\n6.  If you feel as if you cannot continue, please hit the 'Rage Quit'\nbutton.", (75, 200), color = "black", fontname = "arial", fontsize = 32)
	
	elif EASY != 0:
		HOME = 5
		screen.clear()
		screen.fill((255, 255, 255))
		easy_title = Rect((750, 50), (300, 100))
		screen.draw.filled_rect(easy_title, purple)
		screen.draw.rect(easy_title, black)
		enter_number = Rect((750, 175), (175, 75))
		screen.draw.filled_rect(enter_number, white)
		screen.draw.rect(enter_number, black)
		number = Rect((950, 175), (100, 75))
		screen.draw.filled_rect(number, white)
		screen.draw.rect(number, black)
		hint_button = Rect((750, 275), (300, 100))
		screen.draw.filled_rect(hint_button, blue)
		screen.draw.rect(hint_button, black)
		check_button = Rect((750, 400), (300, 100))
		screen.draw.filled_rect(check_button, blue)
		screen.draw.rect(check_button, black)
		ragequit_button = Rect((750, 525), (300, 100))
		screen.draw.filled_rect(ragequit_button, blue)
		screen.draw.rect(ragequit_button, black)
		#text on butttons and title
		screen.draw.text("EASY", (845, 78), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("ENTER THE\n  NUMBER", (755, 180), color = "black", fontname = "arial", fontsize = 30)
		screen.draw.text("HINT", (855, 300), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("CHECK", (832, 425), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("RAGE QUIT", (785, 550), color = "black", fontname = "arial", fontsize = 42)
		
		#draw 81 boxes
		y = 28; z = 66
		for i in range(9):
			x = 78
			for j in range(9):
				b = Rect((x,y), (z,z))
				screen.draw.rect(b, (200,200,200))
				x += z
			y += z

		#draw gridlines
		y = 28; z *= 3
    
		for k in range(3):
			x = 78
			for l in range(3):
				b = Rect((x,y), (z,z))
				screen.draw.rect(b, (0,0,0))
				x += z
			y += z
		data_ea = [[0, 0, 0, 3, 4, 0, 8, 7, 6],
			[9, 0, 0, 1, 0, 0, 5, 0, 0],
			[0, 0, 0, 0, 5, 7, 0, 0, 0],
			[1, 0, 2, 0, 0, 0, 0, 3, 0],
			[0, 0, 0, 0, 0, 5, 0, 0, 0],
			[8, 7, 0, 0, 0, 0, 0, 2, 4],
			[0, 5, 8, 0, 7, 3, 0, 0, 1],
			[3, 0, 9, 6, 1, 8, 0, 0, 7],
			[0, 0, 0, 0, 0, 0, 4, 0, 0]]

		data_ea_shade = [[0, 1, 0, 0, 1, 0, 1, 0, 1],
				[0, 0, 0, 0, 1, 1, 0, 1, 1],
				[1, 1, 1, 1, 0, 0, 0, 0, 0],
				[0, 0, 1, 1, 1, 1, 0, 0, 0],
				[1, 1, 0, 0, 1, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 1, 1, 1],
				[1, 0, 1, 1, 0, 0, 0, 1, 0],
				[0, 1, 0, 1, 0, 1, 1, 0, 0],
				[0, 0, 1, 0, 0, 1, 1, 1, 0]]
		
		ans_ea = [[5, 2, 1, 3, 4, 9, 8, 7, 6],
                         [9, 3, 7, 1, 8, 6, 5, 4, 2],
                         [6, 8, 4, 2, 5, 7, 3, 1, 9],
                         [1, 9, 2, 8, 6, 4, 7, 3, 5],
                         [4, 6, 3, 7, 2, 5, 1, 9, 8],
                         [8, 7, 5, 9, 3, 1, 6, 2, 4],
                         [2, 5, 8, 4, 7, 3, 9, 6, 1],
                         [3, 4, 9, 6, 1, 8, 2, 5, 7],
                         [7, 1, 6, 5, 9, 2, 4, 8, 3]]

		m = 79
		n = 29
		p = 64
		q = 66
		r = 50		
		for x in range (9):
			for y in range (9):
				if data_ea_shade[x][y] == 1 :
					grey_box = Rect((m + y*q, n + x*q), (p, p))
					screen.draw.filled_rect(grey_box, grey)
				if data_ea[x][y] > 0:
					screen.draw.text(str(data_ea[x][y]), (m + y*q + 16, n + x*q + 2), color = "black", fontname = "arial", fontsize = r)	
		
	elif NORMAL != 0:
		HOME = 6
		screen.clear()
		screen.fill((255, 255, 255))
		normal_title = Rect((750, 50), (300, 100))
		screen.draw.filled_rect(normal_title, purple)
		screen.draw.rect(normal_title, black)
		enter_number = Rect((750, 175), (175, 75))
		screen.draw.filled_rect(enter_number, white)
		screen.draw.rect(enter_number, black)
		number = Rect((950, 175), (100, 75))
		screen.draw.filled_rect(number, white)
		screen.draw.rect(number, black)
		hint_button = Rect((750, 275), (300, 100))
		screen.draw.filled_rect(hint_button, blue)
		screen.draw.rect(hint_button, black)
		check_button = Rect((750, 400), (300, 100))
		screen.draw.filled_rect(check_button, blue)
		screen.draw.rect(check_button, black)
		ragequit_button = Rect((750, 525), (300, 100))
		screen.draw.filled_rect(ragequit_button, blue)
		screen.draw.rect(ragequit_button, black)
		#text on butttons and title
		screen.draw.text("NORMAL", (815, 78), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("ENTER THE\n  NUMBER", (755, 180), color = "black", fontname = "arial", fontsize = 30)
		screen.draw.text("HINT", (855, 300), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("CHECK", (832, 425), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("RAGE QUIT", (785, 550), color = "black", fontname = "arial", fontsize = 42)
		
		#draw 81 boxes
		y = 28; z = 66

		for i in range(9):
			x = 78
			for j in range(9):
				b = Rect((x,y), (z,z))
				screen.draw.rect(b, (200,200,200))
				x += z
			y += z

		#draw gridlines
		y = 28; z *= 3
    
		for k in range(3):
			x = 78
			for l in range(3):
				b = Rect((x,y), (z,z))
				screen.draw.rect(b, (0,0,0))
				x += z
			y += z
		
		data_no = [[9, 0, 0, 7, 0, 6, 3, 2, 0],
			[3, 0, 0, 0, 0, 5, 0, 9, 0],
			[1, 0, 8, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 8, 9, 0, 0, 0],
			[0, 0, 9, 0, 0, 2, 4, 0, 0],
			[6, 0, 2, 5, 0, 0, 0, 0, 0],
			[2, 6, 0, 0, 0, 8, 9, 0, 0],
			[0, 9, 0, 0, 2, 0, 0, 0, 1],
			[8, 0, 0, 0, 0, 1, 5, 0, 0]]

		data_no_shade = [[0, 0, 1, 0, 0, 1, 0, 1, 1],
				[0, 1, 1, 1, 1, 0, 0, 0, 0],
				[0, 0, 1, 1, 0, 0, 1, 0, 1],
				[0, 1, 0, 1, 1, 0, 1, 0, 0],
				[0, 1, 0, 0, 0, 1, 1, 0, 1],
				[1, 0, 1, 0, 0, 1, 0, 1, 0],
				[1, 1, 0, 1, 0, 1, 0, 0, 0],
				[1, 0, 0, 0, 1, 0, 1, 1, 0],
				[1, 0, 0, 0, 1, 0, 0, 1, 1]]
		
		ans_no = [[9, 5, 4, 7, 1, 6, 3, 2, 8],
                          [3, 2, 6, 8, 4, 5, 1, 9, 7],
                          [1, 7, 8, 2, 9, 3, 6, 5, 4],
                          [7, 4, 3, 6, 8, 9, 2, 1, 5],
                          [5, 8, 9, 1, 7, 2, 4, 3, 6],
                          [6, 1, 2, 5, 3, 4, 7, 8, 9],
                          [2, 6, 1, 4, 5, 8, 9, 7, 3],
                          [4, 9, 5, 3, 2, 7, 8, 6, 1],
                          [8, 3, 7, 9, 6, 1, 5, 4, 2]]

		m = 79
		n = 29
		p = 64
		q = 66
		r = 50
		
		for x in range (9):
			for y in range (9):
				if data_no_shade[x][y] == 1 :
					grey_box = Rect((m + y*q, n + x*q), (p, p))
					screen.draw.filled_rect(grey_box, grey)
				if data_no[x][y] > 0:
					screen.draw.text(str(data_no[x][y]), (m + y*q + 16, n + x*q + 2), color = "black", fontname = "arial", fontsize = r)
	elif EXTREME != 0:
		HOME = 7
		screen.clear()
		screen.fill((255, 255, 255))
		extreme_title = Rect((750, 50), (300, 100))
		screen.draw.filled_rect(extreme_title, purple)
		screen.draw.rect(extreme_title, black)
		enter_number = Rect((750, 175), (175, 75))
		screen.draw.filled_rect(enter_number, white)
		screen.draw.rect(enter_number, black)
		number = Rect((950, 175), (100, 75))
		screen.draw.filled_rect(number, white)
		screen.draw.rect(number, black)
		hint_button = Rect((750, 275), (300, 100))
		screen.draw.filled_rect(hint_button, blue)
		screen.draw.rect(hint_button, black)
		check_button = Rect((750, 400), (300, 100))
		screen.draw.filled_rect(check_button, blue)
		screen.draw.rect(check_button, black)
		ragequit_button = Rect((750, 525), (300, 100))
		screen.draw.filled_rect(ragequit_button, blue)
		screen.draw.rect(ragequit_button, black)
		#text on butttons and title
		screen.draw.text("EXTREME", (800, 75), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("ENTER THE\n  NUMBER", (755, 180), color = "black", fontname = "arial", fontsize = 30)
		screen.draw.text("HINT", (855, 300), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("CHECK", (832, 425), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("RAGE QUIT", (785, 550), color = "black", fontname = "arial", fontsize = 42)
		
		#draw 81 boxes
		y = 28; z = 66

		for i in range(9):
			x = 78
			for j in range(9):
				b = Rect((x,y), (z,z))
				screen.draw.rect(b, (200,200,200))
				x += z
			y += z

		#draw gridlines
		y = 28; z *= 3
    
		for k in range(3):
			x = 78
			for l in range(3):
				b = Rect((x,y), (z,z))
				screen.draw.rect(b, (0,0,0))
				x += z
			y += z
		data_ex = [[0, 0, 0, 0, 0, 0, 0, 7, 5],
			[4, 0, 0, 0, 6, 0, 0, 0, 0],
			[0, 0, 0, 0, 6, 0, 0, 1, 0],
			[0, 0, 2, 1, 0, 5, 0, 0, 0],
			[0, 0, 0, 7, 0, 0, 0, 4, 0],
			[9, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 3, 9, 0, 8, 0, 0],
			[0, 1, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 2, 0, 0]]

		data_ex_shade = [[0, 0, 1, 1, 1, 0, 1, 0, 0],
				[1, 0, 0, 1, 1, 0, 0, 1, 0],
				[1, 0, 1, 0, 0, 0, 1, 0, 1],
				[1, 1, 1, 0, 0, 0, 0, 1, 0],
				[0, 1, 0, 0, 1, 0, 0, 1, 1],
				[0, 0, 0, 1, 1, 1, 0, 0, 1],
				[0, 1, 0, 0, 0, 1, 1, 1, 0],
				[1, 0, 0, 1, 0, 1, 0, 0, 1],
				[0, 1, 1, 0, 0, 1, 1, 0, 0]]					

		m = 79
		n = 29
		p = 64
		q = 66
		r = 50
		
		for x in range (9):
			for y in range (9):
				if data_ex_shade[x][y] == 1 :
					grey_box = Rect((m + y*q, n + x*q), (p, p))
					screen.draw.filled_rect(grey_box, grey)
				if data_ex[x][y] > 0:
					screen.draw.text(str(data_ex[x][y]), (m + y*q + 16, n + x*q + 2), color = "black", fontname = "arial", fontsize = r)
					
	elif BACK != 0 or CREDITS == 0 or HOWTO == 0 or PLAY ==0 or LEVEL == 0:
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
			exit_popup = Rect((320, 170), (480, 350))
			screen.draw.filled_rect(exit_popup, blue)
			screen.draw.rect(exit_popup,black)
			screen.draw.text("Click anywhere\nto continue\npress control-Q;\ncommand-Q on Mac;\nto exit the game.", (360, 220), color = "black", fontname = "arial", fontsize = 42)
			EXIT = 0
			
			
def on_mouse_down(pos):
	global HOME
	global CREDITS
	global HOWTO
	global EXIT
	global BACK
	global PLAY
	global LEVEL
	global EASY
	global NORMAL
	global EXTREME
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
		LEVEL = 0
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 200 and pos[1] < 300 and HOME == 1 and LEVEL == 0:
		HOWTO = 1
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 350 and pos[1] < 450 and HOME == 1 and LEVEL == 0:
		CREDITS = 1
	if pos[0]> 750 and pos[0] < 1050 and pos[1] > 500 and pos[1] < 600 and HOME == 1:
		EXIT = 1
	if pos[0] > 50 and pos[0] < 350 and pos[1] > 200 and pos[1] < 350 and LEVEL == 1:
		EASY = 1
		PLAY = 0
		LEVEL = 2
	if pos[0] > 400 and pos[0] < 700 and pos[1] > 200 and pos[1] < 350 and LEVEL == 1:
		NORMAL = 1
		PLAY = 0
		LEVEL = 3
	if pos[0] > 750 and pos[0] < 1050 and pos[1] > 200 and pos[1] < 350 and LEVEL == 1:
		EXTREME = 1
		PLAY = 0
		LEVEL = 4
	if pos[0] > 750 and pos[0] < 1050 and pos[1] > 525 and pos[1] < 625 and HOME > 4 and HOME < 8:
		EASY = 0
		NORMAL = 0
		EXTREME = 0
		LEVEL = 0
		PLAY = 0
		BACK = 1
		

pgzrun.go()
