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
INSTRUCTIONS = 0
HINT = 0
CHECK = 0
x_pos = 0
y_pos = 0
board_num = 0
hints = 0
#height has to be 650 for the screen to fit on the size of the computer screen
#each box will be 66x66 in the board

current_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

data_ea1 = [[0, 0, 0, 3, 4, 0, 8, 7, 6],
            [9, 0, 0, 1, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 5, 7, 0, 0, 0],
            [1, 0, 2, 0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 5, 0, 0, 0],
            [8, 7, 0, 0, 0, 0, 0, 2, 4],
            [0, 5, 8, 0, 7, 3, 0, 0, 1],
            [3, 0, 9, 6, 1, 8, 0, 0, 7],
            [0, 0, 0, 0, 0, 0, 4, 0, 0]]


shade_ea1 = [[0, 1, 0, 0, 1, 0, 1, 0, 1],
             [0, 0, 0, 0, 1, 1, 0, 1, 1],
             [1, 1, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 1, 0, 0, 0],
             [1, 1, 0, 0, 1, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 1, 1],
             [1, 0, 1, 1, 0, 0, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 1, 0, 0],
             [0, 0, 1, 0, 0, 1, 1, 1, 0]]

ans_ea1 = [[5, 2, 1, 3, 4, 9, 8, 7, 6],
           [9, 3, 7, 1, 8, 6, 5, 4, 2],
           [6, 8, 4, 2, 5, 7, 3, 1, 9],
           [1, 9, 2, 8, 6, 4, 7, 3, 5],
           [4, 6, 3, 7, 2, 5, 1, 9, 8],
           [8, 7, 5, 9, 3, 1, 6, 2, 4],
           [2, 5, 8, 4, 7, 3, 9, 6, 1],
           [3, 4, 9, 6, 1, 8, 2, 5, 7],
           [7, 1, 6, 5, 9, 2, 4, 8, 3]]
		
data_ea2 = [[0, 0, 8, 4, 0, 7, 6, 0, 0],
            [0, 0, 2, 0, 0, 0, 4, 1, 0],
            [0, 5, 6, 0, 0, 3, 0, 0, 2],
            [0, 0, 3, 0, 0, 8, 1, 2, 0],
            [0, 0, 0, 0, 0, 0, 5, 0, 0],
            [0, 1, 7, 0, 0, 2, 0, 8, 9],
            [6, 0, 0, 0, 3, 9, 0, 0, 0],
            [0, 7, 0, 0, 5, 0, 9, 0, 3],
            [0, 2, 0, 0, 1, 0, 0, 0, 6]]

shade_ea2 = [[0, 0, 1, 1, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 1, 0, 1, 1],
             [1, 1, 1, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 1, 1, 0, 1, 0],
             [1, 1, 0, 1, 0, 0, 1, 0, 0],
             [1, 0, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 0, 0, 1, 1, 0, 1]]

ans_ea2 = [[1, 9, 8, 4, 2, 7, 6, 3, 5],
           [7, 3, 2, 9, 6, 5, 4, 1, 8],
           [4, 5, 6, 1, 8, 3, 7, 9, 2],
           [9, 6, 3, 5, 7, 8, 1, 2, 4],
           [2, 8, 4, 3, 9, 1, 5, 6, 7],
           [5, 1, 7, 6, 4, 2, 3, 8, 9],
           [6, 4, 5, 8, 3, 9, 2, 7, 1],
           [8, 7, 1, 2, 5, 6, 9, 4, 3],
           [3, 2, 9, 7, 1, 4, 8, 5, 6]]
		
data_ea3 = [[0, 0, 3, 0, 6, 0, 8, 0, 4],
	    [0, 0, 0, 0, 0, 0, 0, 0, 2],
	    [0, 0, 9, 0, 0, 3, 0, 7, 0],
	    [2, 5, 0, 3, 8, 1, 0, 9, 0],
	    [0, 0, 0, 0, 0, 6, 0, 5, 0],
	    [9, 0, 6, 0, 0, 0, 0, 0, 3],
	    [0, 0, 4, 0, 0, 0, 0, 0, 9],
	    [0, 0, 8, 5, 2, 0, 0, 6, 0],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0]]

shade_ea3 = [[0, 1, 0, 0, 1, 0, 1, 0, 1],
	     [1, 0, 0, 1, 1, 0, 0, 0, 1],
	     [1, 1, 0, 1, 0, 0, 1, 0, 0],
	     [1, 0, 0, 0, 1, 0, 1, 0, 1],
	     [1, 0, 0, 1, 0, 1, 1, 0, 0],
	     [0, 1, 1, 0, 0, 1, 0, 1, 0],
	     [0, 1, 1, 0, 0, 1, 0, 1, 0],
	     [0, 0, 1, 0, 1, 1, 0, 1, 0],
	     [0, 0, 1, 1, 0, 0, 0, 1, 1]]
	
ans_ea3 = [[7, 2, 3, 9, 6, 5, 8, 1, 4],
	   [6, 1, 5, 8, 4, 7, 9, 3, 2],
	   [4, 8, 9, 2, 1, 3, 6, 7, 5],
	   [2, 5, 7, 3, 8, 1, 4, 9, 6],
	   [8, 3, 1, 4, 9, 6, 2, 5, 7],
	   [9, 4, 6, 7, 5, 2, 1, 8, 3],
	   [5, 6, 4, 1, 7, 8, 3, 2, 9],
	   [3, 9, 8, 5, 2, 4, 7, 6, 1],
	   [1, 7, 2, 6, 3, 9, 5, 4, 8]]

data_ea4 = [[2, 0, 3, 0, 0, 6, 4, 0, 0],
            [0, 0, 0, 1, 9, 4, 0, 5, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 6, 0, 0, 0, 7, 0, 0, 8],
            [0, 0, 0, 5, 0, 0, 1, 0, 0],
            [0, 0, 0, 4, 0, 1, 9, 6, 0],
            [0, 9, 0, 0, 4, 0, 3, 0, 0],
            [0, 0, 0, 6, 0, 0, 8, 1, 0],
            [0, 0, 7, 0, 0, 0, 0, 0, 0]]

shade_ea4 = [[1, 0, 0, 0, 1, 1, 1, 0, 0],
             [1, 0, 1, 0, 0, 1, 1, 0, 0],
             [1, 0, 0, 1, 0, 0, 0, 1, 1],
             [0, 1, 0, 0, 1, 0, 0, 1, 1],
             [0, 1, 1, 0, 1, 1, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 1, 1],
             [0, 0, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 1, 1, 0, 0, 1, 0, 1],
             [1, 1, 0, 0, 0, 0, 1, 1, 0]]

ans_ea4 = [[2, 5, 3, 7, 8, 6, 4, 9, 1],
           [6, 7, 8, 1, 9, 4, 2, 5, 3],
           [4, 1, 9, 2, 5, 3, 7, 8, 6],
           [3, 6, 1, 9, 2, 7, 5, 4, 8],
           [9, 2, 4, 5, 6, 8, 1, 3, 7],
           [7, 8, 5, 4, 3, 1, 9, 6, 2],
           [1, 9, 6, 8, 4, 2, 3, 7, 5],
           [5, 3, 2, 6, 7, 9, 8, 1, 4],
           [8, 4, 7, 3, 1, 5, 6, 2, 9]]

data_ea5 = [[0, 1, 0, 0, 8, 4, 0, 0, 0],
	    [0, 3, 2, 9, 0, 0, 0, 0, 0],
	    [4, 7, 0, 0, 2, 0, 8, 0, 0],
            [0, 5, 0, 0, 9, 8, 0, 0, 1],
            [3, 0, 0, 0, 0, 0, 6, 7, 2],
            [0, 0, 4, 0, 0, 7, 0, 0, 0],
            [0, 0, 1, 0, 4, 0, 0, 0, 6],
            [0, 0, 9, 0, 0, 0, 3, 0, 0],
            [7, 0, 0, 0, 0, 2, 0, 5, 4]]

shade_ea5 = [[0, 0, 0, 0, 1, 1, 1, 1, 0],
             [1, 0, 1, 0, 1, 0, 0, 1, 0],
             [1, 0, 1, 0, 1, 0, 1, 0, 0],
             [1, 0, 0, 1, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0, 1, 0, 1],
             [0, 1, 1, 1, 0, 0, 0, 1, 0],
             [0, 1, 0, 0, 1, 0, 0, 1, 1],
             [1, 1, 0, 0, 0, 1, 0, 0, 1],
             [0, 1, 0, 1, 0, 1, 0, 0, 1]]
	    
ans_ea5 = [[9, 1, 5, 7, 8, 4, 2, 6, 3],
	   [8, 3, 2, 9, 6, 5, 1, 4, 7],
	   [4, 7, 6, 1, 2, 3, 8, 9, 5],
           [6, 5, 7, 2, 9, 8, 4, 3, 1],
           [3, 9, 8, 4, 5, 1, 6, 7, 2],
           [1, 2, 4, 6, 3, 7, 5, 8, 9],
           [5, 8, 1, 3, 4, 9, 7, 2, 6],
           [2, 4, 9, 5, 7, 6, 3, 1, 8],
           [7, 6, 3, 8, 1, 2, 9, 5, 4]]

data_ea6 = [[0, 3, 0, 0, 0, 4, 1, 9, 5],
            [0, 0, 1, 0, 0, 0, 4, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 9, 4, 6, 0, 7, 0, 0],
            [7, 0, 0, 0, 9, 5, 0, 0, 3],
            [0, 0, 5, 0, 1, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 9, 6, 0, 2],
            [4, 0, 0, 0, 0, 0, 0, 0, 8]]

shade_ea6 = [[1, 0, 1, 0, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 1, 1, 1],
             [0, 1, 1, 1, 0, 0, 1, 0, 0],
             [0, 1, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 1, 1, 0, 0, 1, 1, 0],
             [1, 1, 0, 0, 0, 0, 0, 1, 1],
             [0, 1, 1, 0, 1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 1, 1, 1],
             [1, 0, 0, 1, 0, 1, 0, 0, 1]]

ans_ea6 = [[6, 3, 8, 7, 2, 4, 1, 9, 5],
           [5, 7, 1, 9, 8, 3, 4, 2, 6],
           [9, 4, 2, 6, 5, 1, 8, 3, 7],
           [3, 8, 9, 4, 6, 2, 7, 5, 1],
           [7, 1, 4, 8, 9, 5, 2, 6, 3],
           [2, 6, 5, 3, 1, 7, 9, 8, 4],
           [1, 2, 6, 5, 4, 8, 3, 7, 9],
           [8, 5, 3, 1, 7, 9, 6, 4, 2],
           [4, 9, 7, 2, 3, 6, 5, 1, 8]]
	     
data_no1 = [[9, 0, 0, 7, 0, 6, 3, 2, 0],
            [3, 0, 0, 0, 0, 5, 0, 9, 0],
            [1, 0, 8, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 8, 9, 0, 0, 0],
            [0, 0, 9, 0, 0, 2, 4, 0, 0],
            [6, 0, 2, 5, 0, 0, 0, 0, 0],
            [2, 6, 0, 0, 0, 8, 9, 0, 0],
            [0, 9, 0, 0, 2, 0, 0, 0, 1],
            [8, 0, 0, 0, 0, 1, 5, 0, 0]]

shade_no1 = [[0, 0, 1, 0, 0, 1, 0, 1, 1],
             [0, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 1, 1, 0, 0, 1, 0, 1],
             [0, 1, 0, 1, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 0, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 1, 0, 1, 0],
             [1, 1, 0, 1, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 1, 0, 1, 1, 0],
             [1, 0, 0, 0, 1, 0, 0, 1, 1]]				

ans_no1 = [[9, 5, 4, 7, 1, 6, 3, 2, 8],
           [3, 2, 6, 8, 4, 5, 1, 9, 7],
           [1, 7, 8, 2, 9, 3, 6, 5, 4],
           [7, 4, 3, 6, 8, 9, 2, 1, 5],
           [5, 8, 9, 1, 7, 2, 4, 3, 6],
           [6, 1, 2, 5, 3, 4, 7, 8, 9],
           [2, 6, 1, 4, 5, 8, 9, 7, 3],
           [4, 9, 5, 3, 2, 7, 8, 6, 1],
           [8, 3, 7, 9, 6, 1, 5, 4, 2]]
			
data_no2 = [[6, 1, 0, 0, 2, 0, 9, 0, 3],
            [9, 4, 2, 8, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 2, 6],
            [0, 0, 4, 0, 0, 0, 8, 6, 0],
            [5, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 8, 5, 0, 0, 0],
            [0, 0, 0, 7, 0, 0, 0, 0, 2],
            [7, 0, 1, 6, 0, 0, 0, 4, 0],
            [2, 0, 0, 0, 0, 0, 1, 0, 0]]

shade_no2 = [[1, 0, 0, 0, 1, 1, 0, 1, 0],
             [0, 1, 1, 1, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 1, 1, 1],
             [0, 1, 1, 0, 0, 0, 1, 1, 0],
             [0, 1, 0, 1, 1, 0, 0, 0, 1],
             [0, 0, 1, 1, 1, 0, 1, 0, 0],
             [1, 0, 1, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 0, 1, 1, 0, 0, 0]]				

ans_no2 = [[6, 1, 7, 5, 2, 4, 9, 8, 3],
           [9, 4, 2, 8, 3, 6, 5, 1, 7],
           [8, 5, 3, 1, 9, 7, 4, 2, 6],
           [1, 2, 4, 9, 7, 3, 8, 6, 5],
           [5, 8, 9, 2, 6, 1, 7, 3, 4],
           [3, 7, 6, 4, 8, 5, 2, 9, 1],
           [4, 3, 8, 7, 1, 9, 6, 5, 2],
           [7, 9, 1, 6, 5, 2, 3, 4, 8],
           [2, 6, 5, 3, 4, 8, 1, 7, 9]]
			
data_no3 = [[2, 9, 0, 3, 0, 0, 0, 0, 0],
	    [0, 0, 8, 0, 0, 9, 0, 0, 0],
	    [0, 0, 6, 2, 5, 0, 4, 0, 0],
	    [0, 8, 0, 0, 0, 0, 0, 0, 0],
	    [9, 0, 0, 7, 0, 8, 0, 3, 5],
	    [1, 7, 0, 0, 0, 0, 0, 0, 0],
	    [0, 2, 0, 0, 0, 3, 0, 0, 0],
	    [0, 0, 0, 0, 4, 0, 9, 0, 0],
	    [6, 4, 7, 0, 0, 0, 0, 8, 1]]

shade_no3 = [[1, 0, 0, 0, 1, 1, 1, 0, 0],
	     [1, 0, 1, 1, 0, 0, 1, 0, 0],
	     [0, 0, 1, 1, 0, 0, 1, 0, 1],
	     [0, 1, 1, 1, 0, 0, 0, 1, 0],
	     [0, 1, 1, 0, 1, 1, 0, 0, 0],
	     [0, 0, 0, 0, 0, 1, 1, 1, 1],
	     [1, 1, 0, 0, 1, 0, 0, 0, 1],
	     [0, 0, 0, 1, 1, 0, 0, 1, 1],
	     [1, 1, 0, 0, 0, 1, 0, 1, 0]]

ans_no3 =  [[2, 9, 1, 3, 8, 4, 6, 5, 7],
	    [4, 5, 8, 6, 7, 9, 2, 1, 3],
	    [7, 3, 6, 2, 5, 1, 4, 9, 8],
	    [3, 8, 2, 4, 1, 5, 7, 6, 0],
	    [9, 6, 4, 7, 2, 8, 1, 3, 5],
	    [1, 7, 5, 9, 3, 6, 8, 4, 2],
	    [8, 2, 9, 1, 6, 3, 5, 7, 4],
	    [5, 1, 3, 8, 4, 7, 9, 2, 6],
	    [6, 4, 7, 5, 7, 2, 3, 8, 1]]

data_no4 = [[1, 0, 0, 0, 7, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0, 1, 5, 0],
            [8, 0, 2, 9, 1, 0, 0, 0, 0],
            [4, 0, 0, 0, 0, 2, 3, 7, 0],
            [6, 0, 0, 0, 0, 0, 9, 0, 0],
            [0, 0, 0, 3, 0, 7, 0, 6, 0],
            [0, 6, 0, 0, 5, 0, 8, 3, 0],
            [0, 0, 5, 7, 0, 0, 0, 9, 0],
            [0, 8, 9, 0, 0, 0, 0, 0, 6]]

shade_no4 = [[0, 1, 0, 1, 0, 0, 1, 1, 0],
             [0, 0, 1, 1, 1, 0, 0, 0, 1],
             [1, 0, 1, 0, 0, 1, 0, 1, 0],
             [1, 0, 0, 1, 1, 1, 0, 0, 0],
             [1, 0, 0, 0, 1, 0, 0, 1, 1],
             [0, 1, 1, 0, 0, 0, 1, 1, 0],
             [1, 1, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 1, 1, 0, 1],
             [0, 1, 0, 1, 0, 1, 0, 0, 1]]			

ans_no4 = [[1, 4, 3, 8, 7, 5, 6, 2, 9],
           [9, 7, 6, 4, 2, 3, 1, 5, 8],
           [8, 5, 2, 9, 1, 6, 7, 4, 3],
           [4, 9, 1, 6, 8, 2, 3, 7, 5],
           [6, 3, 7, 5, 4, 1, 9, 8, 2],
           [5, 2, 8, 3, 9, 7, 4, 6, 1],
           [2, 6, 4, 1, 5, 9, 8, 3, 7],
           [3, 1, 5, 7, 6, 8, 2, 9, 4],
           [7, 8, 9, 2, 3, 4, 5, 1, 6]]

data_no5 = [[0, 0, 0, 0, 0, 0, 0, 1, 0],
            [4, 0, 0, 9, 6, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 8, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 6, 0],
            [0, 0, 0, 0, 1, 7, 0, 3, 0],
            [0, 0, 0, 4, 0, 0, 7, 0, 0],
            [6, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 5, 0, 0, 0, 8, 0, 2, 0],
            [3, 1, 0, 0, 4, 0, 0, 0, 9]] 
	     
shade_no5 = [[1, 0, 0, 0, 1, 1, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 0, 1, 1, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 1, 0, 1, 0],
            [1, 0, 1, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 0]]
	    
ans_no5 = [[2, 9, 7, 3, 8, 4, 5, 1, 6],
            [4, 8, 1, 9, 6, 5, 2, 7, 3],
            [5, 6, 3, 2, 7, 1, 8, 9, 4],
            [7, 2, 5, 8, 9, 3, 4, 6, 1],
            [8, 4, 6, 5, 1, 7, 9, 3, 2],
            [1, 3, 9, 4, 2, 6, 7, 8, 3],
            [6, 7, 2, 1, 5, 9, 3, 4, 8],
            [9, 5, 4, 6, 3, 8, 1, 2, 7],
            [3, 1, 8, 7, 4, 2, 6, 5, 9]] 
	     
data_no6 = [[1, 2, 0, 9, 0, 0, 0, 0, 0],
            [5, 0, 6, 0, 8, 0, 2, 0, 0],
            [9, 0, 0, 0, 0, 0, 0, 5, 0],
            [0, 0, 5, 8, 0, 0, 0, 0, 9],
            [0, 0, 4, 0, 5, 2, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 0, 0, 0],
            [0, 0, 0, 0, 6, 0, 0, 7, 0],
            [0, 1, 0, 0, 3, 0, 4, 0, 0],
            [0, 7, 0, 0, 0, 0, 8, 6, 3]]
	    
shade_no6 = [[0, 1, 0, 0, 1, 0, 0, 1, 1],
             [0, 1, 1, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 1, 1, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0, 1, 1, 0, 1],
             [1, 1, 0, 1, 0, 0, 0, 0, 1],
             [0, 0, 1, 1, 1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 1, 1, 1, 0],
             [1, 0, 1, 0, 0, 0, 1, 1, 0]]
	    
ans_no6 = [[1, 2, 7, 9, 4, 5, 3, 8, 6],
           [5, 4, 6, 1, 8, 4, 2, 9, 7],
           [9, 8, 3, 6, 2, 7, 1, 5, 4],
           [2, 3, 5, 8, 1, 6, 7, 4, 9],
           [7, 9, 4, 3, 5, 2, 6, 1, 8],
           [8, 6, 1, 4, 7, 9, 5, 3, 2],
           [3, 5, 8, 2, 6, 4, 9, 7, 1],
           [6, 1, 9, 7, 3, 8, 4, 2, 5],
           [4, 7, 2, 5, 9, 1, 8, 6, 3]]
	   
data_ex1 = [[0, 0, 0, 0, 0, 0, 0, 7, 5],
            [4, 0, 0, 0, 6, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 2, 1, 0, 5, 0, 0, 0],
            [0, 0, 0, 7, 0, 0, 0, 4, 0],
            [9, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 3, 9, 0, 8, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0]]

shade_ex1 = [[0, 0, 1, 1, 1, 0, 1, 0, 0],
             [1, 0, 0, 1, 1, 0, 0, 1, 0],
             [1, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 1, 1, 0, 0, 0, 0, 1, 0],
             [0, 1, 0, 0, 1, 0, 0, 1, 1],
             [0, 0, 0, 1, 1, 1, 0, 0, 1],
             [0, 1, 0, 0, 0, 1, 1, 1, 0],
             [1, 0, 0, 1, 0, 1, 0, 0, 1],
             [0, 1, 1, 0, 0, 1, 1, 0, 0]]

ans_ex1 = [[1, 9, 8, 2, 4, 3, 6, 7, 5],
           [4, 5, 7, 8, 6, 1, 9, 2, 3],
           [2, 3, 6, 9, 5, 7, 4, 1, 8],
           [6, 4, 2, 1, 3, 5, 7, 8, 9],
           [5, 8, 3, 7, 2, 9, 1, 4, 6],
           [9, 7, 1, 4, 8, 6, 3, 5, 2],
           [7, 2, 5, 3, 9, 4, 8, 6, 1],
           [8, 1, 9, 6, 7, 2, 5, 3, 4],
           [3, 6, 4, 5, 1, 8, 2, 9, 7]]

data_ex2 = [[1, 0, 0, 0, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 3, 0, 8],
            [0, 0, 0, 0, 0, 7, 0, 0, 0],
            [7, 0, 0, 6, 0, 0, 0, 1, 0],
            [0, 0, 0, 8, 0, 5, 2, 0, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 0, 2, 0, 0, 0, 0],
            [0, 8, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0]]

shade_ex2 = [[0, 0, 0, 0, 1, 1, 0, 1, 1],
             [0, 1, 0, 0, 1, 1, 0, 0, 1],
             [1, 1, 1, 0, 0, 0, 1, 0, 0],
             [0, 1, 1, 1, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 0, 0, 1, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 1, 1],
             [1, 0, 0, 1, 1, 0, 1, 0, 0],
             [0, 1, 1, 0, 0, 1, 0, 1, 0],
             [1, 0, 0, 0, 1, 0, 1, 1, 0]]

ans_ex2 = [[1, 7, 3, 5, 4, 8, 9, 6, 2],
           [5, 4, 9, 1, 6, 2, 3, 7, 8],
           [8, 6, 2, 9, 3, 7, 4, 5, 1],
           [7, 2, 8, 6, 9, 4, 5, 1, 3],
           [3, 1, 6, 8, 7, 5, 2, 9, 4],
           [4, 9, 5, 2, 1, 3, 7, 8, 6],
           [6, 5, 7, 4, 2, 1, 8, 3, 9],
           [9, 8, 4, 3, 5, 6, 1, 2, 7],
           [2, 3, 1, 7, 8, 9, 6, 4, 5]]


data_ex3 = [[0, 0, 0, 0, 8, 0, 0, 3, 4],
            [0, 0, 2, 7, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, 3, 0, 9, 0, 0],
            [0, 0, 0, 0, 0, 4, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 5, 7, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 0, 1, 0, 0, 0, 0, 0]]

	
shade_ex3 = [[0, 0, 0, 1, 1, 1, 0, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 1, 0],
             [1, 0, 1, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 1, 1, 1, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1],
             [0, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 1, 1, 1],
             [1, 1, 0, 0, 0, 1, 1, 0, 0]]

ans_ex3 = [[5, 7, 9, 6, 8, 2, 1, 3, 4],
           [4, 3, 2, 7, 1, 5, 6, 8, 9],
           [6, 1, 8, 3, 4, 9, 7, 5, 2],
           [8, 2, 6, 5, 3, 1, 9, 4, 7],
           [1, 9, 3, 8, 7, 4, 2, 6, 5],
           [7, 4, 5, 9, 2, 6, 3, 1, 8],
           [9, 8, 4, 2, 6, 3, 5, 7, 1],
           [3, 5, 1, 4, 9, 7, 8, 2, 6],
           [2, 6, 7, 1, 5, 8, 4, 9, 3]]

data_ex4 = [[3, 0, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 2, 6],
            [8, 0, 0, 0, 0, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 0, 0, 1, 0, 7, 3, 0, 0],
            [0, 4, 2, 0, 0, 0, 1, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 0, 0]]

shade_ex4 = [[0, 1, 1, 0, 0, 1, 0, 0, 1],
             [1, 0, 0, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 1, 0, 1, 1, 0, 0],
             [0, 0, 0, 0, 1, 1, 0, 1, 1],
             [1, 0, 1, 1, 0, 0, 1, 0, 0],
             [1, 0, 1, 1, 0, 0, 0, 1, 0],
             [0, 1, 0, 0, 1, 0, 0, 1, 1],
             [0, 1, 1, 0, 1, 0, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 1, 0, 0]]

ans_ex4 = [[3, 2, 8, 7, 1, 6, 5, 9, 4],
           [4, 5, 7, 3, 2, 9, 6, 1, 8],
           [6, 1, 9, 8, 5, 4, 2, 7, 3],
           [5, 3, 1, 9, 4, 8, 7, 2, 6],
           [8, 9, 6, 2, 7, 5, 4, 3, 1],
           [2, 7, 4, 6, 3, 1, 9, 8, 5],
           [9, 8, 5, 1, 6, 7, 3, 4, 2],
           [7, 4, 2, 5, 8, 3, 1, 6, 9],
           [1, 6, 3, 4, 9, 2, 8, 5, 7]]

data_ex5 = [[2, 0, 0, 6, 8, 0, 0, 0, 0],
            [6, 0, 0, 0, 0, 0, 9, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [7, 3, 0, 0, 0, 0, 0, 6, 0],
            [0, 0, 0, 4, 0, 1, 0, 0, 5],
            [0, 0, 0, 9, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 4, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0]]

shade_ex5 = [[1, 0, 0, 1, 1, 0, 0, 1, 0],
             [1, 0, 0, 1, 0, 1, 0, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 1, 1],
             [0, 0, 0, 1, 0, 1, 1, 1, 0],
             [1, 1, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 0, 1, 0, 1],
             [0, 1, 0, 0, 1, 0, 0, 1, 1],
             [0, 1, 1, 0, 0, 1, 1, 0, 0],
             [0, 1, 0, 0, 1, 1, 1, 0, 0]]

ans_ex5 = [[2, 1, 5, 6, 8, 9, 3, 4, 7],
           [6, 7, 3, 2, 1, 4, 9, 5, 8],
           [4, 9, 8, 3, 7, 5, 1, 2, 6],
           [7, 3, 9, 8, 5, 2, 4, 6, 1],
           [8, 2, 6, 4, 3, 1, 7, 9, 5],
           [1, 5, 4, 9, 6, 7, 8, 3, 2],
           [9, 6, 7, 1, 2, 3, 5, 8, 4],
           [5, 4, 2, 7, 9, 8, 6, 1, 3],
           [3, 8, 1, 5, 4, 6, 2, 7, 9]]
	  
data_ex6 = [[0, 3, 9, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 0, 0, 0, 0, 8, 3],
            [4, 0, 0, 7, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 5, 0],
            [1, 0, 0, 0, 0, 0, 7, 0, 0],
            [6, 0, 0, 0, 0, 8, 0, 0, 0]]

shade_ex6 = [[0, 0, 0, 1, 1, 0, 1, 1, 0],
             [1, 1, 0, 1, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 0, 1, 1, 0, 0],
             [0, 0, 0, 0, 1, 1, 1, 1, 0],
             [1, 0, 1, 0, 1, 0, 0, 0, 1],
             [0, 1, 1, 0, 0, 1, 0, 0, 1],
             [0, 1, 1, 1, 0, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 0, 0, 1, 1],
             [1, 0, 0, 1, 0, 1, 0, 1, 0]]

ans_ex6 = [[5, 3, 9, 8, 2, 1, 4, 6, 7],
           [8, 4, 7, 6, 9, 5, 1, 3, 2],
           [2, 1, 6, 3, 7, 4, 8, 9, 5],
           [7, 5, 1, 9, 4, 6, 2, 8, 3],
           [4, 9, 2, 7, 8, 3, 5, 1, 6],
           [3, 6, 8, 1, 5, 2, 9, 7, 4],
           [9, 8, 4, 2, 3, 7, 6, 5, 1],
           [1, 2, 3, 5, 6, 9, 7, 4, 8],
           [6, 7, 5, 4, 1, 8, 3, 2, 9]]
	   
#add to the following data and ans sets when new boards are added
data_ea = [data_ea1, data_ea2, data_ea3, data_ea4, data_ea5, data_ea6]
data_no = [data_no1, data_no2, data_no3, data_no4, data_no5, data_no6]
data_ex = [data_ex1, data_ex2, data_ex3, data_ex4, data_ex5, data_ex6]
shade_ea = [shade_ea1, shade_ea2, shade_ea3, shade_ea4, shade_ea5, shade_ea6]
shade_no = [shade_no1, shade_no2, shade_no3, shade_no4, shade_no5, shade_no6]
shade_ex = [shade_ex1, shade_ex2, shade_ex3, shade_ex4, shade_ex5, shade_ex6]
ans_ea = [ans_ea1, ans_ea2, ans_ea3, ans_ea4, ans_ea5, ans_ea6]
ans_no = [ans_no1, ans_no2, ans_no3, ans_no4, ans_no5, ans_no6]
ans_ex = [ans_ex1, ans_ex2, ans_ex3, ans_ex4, ans_ex5, ans_ex6]

HIGHLIGHTX = -1			
HIGHLIGHTY = -1

def draw():
	global HINT
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
	global CHECK
	global INSTRUCTIONS
	global HIGHLIGHTX
	global HIGHLIGHTY
	global current_board
	global board_num
	global data_ea
	global data_no
	global data_ex
	global ans_ea
	global ans_no
	global ans_ex
	global hints
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
		screen.draw.text("-  Home screen image: https://tinyurl.com/y9cbazvx\n-  Play screen examples: https://tinyurl.com/ybzp7bjw\n-  Boards: https://tinyurl.com/y9onnnsp\n-  More boards: https://tinyurl.com/y6844rhf\n-  Inspiration: https://tinyurl.com/ycw6n2hv", (75, 200), color = "black", fontname = "arial", fontsize = 38)
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
		screen.draw.text("1.  To enter a number, click the square and then the button with the\nnumber you would like to enter.\n2.  Each row and column must contain the numbers from\n1-9 (cannot repeat numbers).\n3.  Each 3x3 box with a darker outline must also contain the\nnumbers from 1-9 (cannot repeat numbers).\n4.  In the shaded boxes, the numbers must be even. In the unshaded\nboxes, the numbers have to be odd.\n5.  If you need a hint, click the square you want a hint in and the 'Hint'\nbutton. Three for easy, two for normal, and only one for extreme.\n6.  If you want to check your answers, press the 'Check' button.\n7.  If you feel as if you cannot continue, hit the 'Rage Quit' button.", (60, 183), color = "black", fontname = "arial", fontsize = 32)
	
	elif EASY != 0:
		HOME = 5
		screen.clear()
		screen.fill((255, 255, 255))
		easy_title = Rect((750, 50), (230, 100))
		screen.draw.filled_rect(easy_title, purple)
		screen.draw.rect(easy_title, black)
		easy_howto = Rect((990, 50), (60, 100))
		screen.draw.filled_rect(easy_howto, blue)
		screen.draw.rect(easy_howto, black)
		for count in range(10):
			if count <= 4:
				button_box = Rect((750 + count * 60, 160), (50, 50))
				screen.draw.rect(button_box, black)
			else:
				button_box = Rect((750 + (count-5) * 60, 215), (50, 50))
				screen.draw.rect(button_box, black)
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
		screen.draw.text("EASY", (810, 78), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("?", (1010, 78), color = "black", fontname = "arial", fontsize = 42)
		for number in range(9):
			num = number + 1
			if number <= 4:
				screen.draw.text(str(num), (765 + number * 60, 165), color = "black", fontname = "arial", fontsize = 36)
			else:
				screen.draw.text(str(num), (765 + (number-5) * 60, 220), color = "black", fontname = "arial", fontsize = 36) 
		screen.draw.text("Clear", (991,227), color = "black", fontname = "arial", fontsize = 20)
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

		m = 79
		n = 29
		p = 64
		q = 66
		r = 50
		
		for x in range (9):
			for y in range (9):
				if shade_ea[board_num][x][y] == 1 :
					grey_box = Rect((m + y*q, n + x*q), (p, p))
					screen.draw.filled_rect(grey_box, grey)
				if 	HIGHLIGHTX != -1 :
					highlight = Rect((HIGHLIGHTY*66 + 79,HIGHLIGHTX*66 +29), (66,66))
					screen.draw.rect(highlight, (26, 15, 251))
				if current_board[x][y] > 0:
					screen.draw.text(str(current_board[x][y]), (m + y*q + 16, n + x*q + 2), color = "black", fontname = "arial", fontsize = r)	
		
	elif NORMAL != 0:
		HOME = 6
		screen.clear()
		screen.fill((255, 255, 255))
		normal_title = Rect((750, 50), (230, 100))
		screen.draw.filled_rect(normal_title, purple)
		screen.draw.rect(normal_title, black)
		normal_howto = Rect((990, 50), (60, 100))
		screen.draw.filled_rect(normal_howto, blue)
		screen.draw.rect(normal_howto, black)
		for count in range(10):
			if count <= 4:
				button_box = Rect((750 + count * 60, 160), (50, 50))
				screen.draw.rect(button_box, black)
			else:
				button_box = Rect((750 + (count-5) * 60, 215), (50, 50))
				screen.draw.rect(button_box, black)
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
		screen.draw.text("NORMAL", (780, 78), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("?", (1010, 78), color = "black", fontname = "arial", fontsize = 42)
		for number in range(9):
			num = number + 1
			if number <= 4:
				screen.draw.text(str(num), (765 + number * 60, 165), color = "black", fontname = "arial", fontsize = 36)
			else:
				screen.draw.text(str(num), (765 + (number-5) * 60, 220), color = "black", fontname = "arial", fontsize = 36)     
		screen.draw.text("Clear", (991,227), color = "black", fontname = "arial", fontsize = 20)
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

		m = 79
		n = 29
		p = 64
		q = 66
		r = 50
		
		for x in range (9):
			for y in range (9):
				if shade_no[board_num][x][y] == 1 :
					grey_box = Rect((m + y*q, n + x*q), (p, p))
					screen.draw.filled_rect(grey_box, grey)
				if 	HIGHLIGHTX != -1 :
					highlight = Rect((HIGHLIGHTY*66 + 79,HIGHLIGHTX*66 +29), (66,66))
					screen.draw.rect(highlight, (26, 15, 251))
				if current_board[x][y] > 0:
					screen.draw.text(str(current_board[x][y]), (m + y*q + 16, n + x*q + 2), color = "black", fontname = "arial", fontsize = r)
	elif EXTREME != 0:
		HOME = 7
		screen.clear()
		screen.fill((255, 255, 255))
		extreme_title = Rect((750, 50), (230, 100))
		screen.draw.filled_rect(extreme_title, purple)
		screen.draw.rect(extreme_title, black)
		extreme_howto = Rect((990, 50), (60, 100))
		screen.draw.filled_rect(extreme_howto, blue)
		screen.draw.rect(extreme_howto, black)
		for count in range(10):
			if count <= 4:
				button_box = Rect((750 + count * 60, 160), (50, 50))
				screen.draw.rect(button_box, black)
			else:
				button_box = Rect((750 + (count-5) * 60, 215), (50, 50))
				screen.draw.rect(button_box, black)
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
		screen.draw.text("EXTREME", (765, 75), color = "black", fontname = "arial", fontsize = 42)
		screen.draw.text("?", (1010, 78), color = "black", fontname = "arial", fontsize = 42)
		for number in range(9):
			num = number + 1
			if number <= 4:
				screen.draw.text(str(num), (765 + number * 60, 165), color = "black", fontname = "arial", fontsize = 36)
			else:
				screen.draw.text(str(num), (765 + (number-5) * 60, 220), color = "black", fontname = "arial", fontsize = 36)    
		screen.draw.text("Clear", (991,227), color = "black", fontname = "arial", fontsize = 20)
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

		m = 79
		n = 29
		p = 64
		q = 66
		r = 50
		
		for x in range (9):
			for y in range (9):
				if shade_ex[board_num][x][y] == 1 :
					grey_box = Rect((m + y*q, n + x*q), (p, p))
					screen.draw.filled_rect(grey_box, grey)
				if 	HIGHLIGHTX != -1 :
					highlight = Rect((HIGHLIGHTY*66 + 79,HIGHLIGHTX*66 +29), (66,66))
					screen.draw.rect(highlight, (26, 15, 251))
				if current_board[x][y] > 0:
					screen.draw.text(str(current_board[x][y]), (m + y*q + 16, n + x*q + 2), color = "black", fontname = "arial", fontsize = r)
					
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

	if CHECK != 0:
		if HOME == 5:
			answer_board = ans_ea[board_num]
		if HOME == 6:
			answer_board = ans_no[board_num]
		if HOME == 7:
			answer_board = ans_ex[board_num]

		wrong = 0
		correct = 0
		for x in range (9):
			for y in range (9):
				if current_board[x][y] != 0:
					if current_board[x][y] != answer_board[x][y]:
						wrong += 1
					else:
						correct += 1

		if correct != 81:
			wrong_count = Rect((350, 200), (390, 100))
			screen.draw.filled_rect(wrong_count, blue)
			screen.draw.rect(wrong_count, black)
			if wrong != 1:
	   			thing = "There are " + str(wrong) + " errors."
			else:
	   			thing = "There is one error."
			screen.draw.text(thing, (360, 220), color = "black", fontname = "arial", fontsize = 42)
			CHECK = 0
		else:
			congrats = Rect((150, 160), (700, 400))
			screen.draw.filled_rect(congrats,white)
			screen.draw.rect(congrats, black)
			screen.draw.text("CONGRATULATIONS!", (300, 200), color = "black", fontname = "arial", fontsize = 42)
			screen.draw.text("You have correctly solved this \nsudoku! Hit the button below to go \nback to the home screen.", (190, 260), color = "black", fontname = "arial", fontsize = 42)
			CHECK = 0
			home_button = Rect((358, 430), (300, 70))
			screen.draw.filled_rect(home_button, blue)
			screen.draw.rect(home_button, black)
			screen.draw.text("HOME", (455, 442), color = "black", fontname = "arial", fontsize = 42)
			HOME = 8
			
	if INSTRUCTIONS != 0:
		instructions_text = Rect ((50, 50), (1000, 480))
		screen.draw.filled_rect(instructions_text, white)
		screen.draw.rect(instructions_text, black)
		screen.draw.text("1. Click on an empty square, then click one of the\nnumbered boxes to the side to enter a number.\n2. Click the \"Clear\" box to erase a number from a square.\n3. Be aware that you can change the given values in the\nsquares, but it is suggested to not change them, as it will\nbe harder for you.\n4. Click on a square, then click \"Hint\" if you want to reveal\nthe correct number of the square.\n5. Click \"Check\" if you are done, and it will tell you how\nmany numbers you entered are wrong. ", (70, 70), color = "black", fontname = "arial", fontsize = 38)
		INSTRUCTIONS = 0
		
	if HINT != 0:
		if hints != 0:
			y = int((x_pos-79)/66)
			x = int((y_pos-29)/66)
			if HOME == 5:
				current_board[x][y] = ans_ea[board_num][x][y]
			elif HOME == 6:
				current_board[x][y] = ans_no[board_num][x][y]
			else:
				current_board[x][y] = ans_ex[board_num][x][y]
			hints -= 1
			left = Rect((270, 200), (540, 100))
			screen.draw.filled_rect(left, blue)
			screen.draw.rect(left, black)
			if hints != 1:
	   			thing = "You have " + str(hints) + " remaining hints."
			else:
	   			thing = "You have one remaining hint."
			screen.draw.text(thing, (280, 225), color = "black", fontname = "arial", fontsize = 42)
		else:
			left = Rect((240, 200), (630, 100))
			screen.draw.filled_rect(left, blue)
			screen.draw.rect(left, black)
			screen.draw.text("You have no remaining hints left.", (250, 225), color = "black", fontname = "arial", fontsize = 42)
		HINT = 0
	
	if EXIT != 0:
		exit_popup = Rect((320, 170), (480, 350))
		screen.draw.filled_rect(exit_popup, blue)
		screen.draw.rect(exit_popup,black)
		screen.draw.text("Click anywhere\nto continue.\nPress control-Q;\ncommand-Q on Mac;\nto exit the game.", (360, 220), color = "black", fontname = "arial", fontsize = 42)
		EXIT = 0
	
	
def on_mouse_down(pos):
        from random import randint
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
        global HINT
        global CHECK
        global INSTRUCTIONS
        global x_pos
        global y_pos
        global current_board
        global board_num
        global data_ea
        global data_no
        global data_ex
        global HIGHLIGHTX
        global HIGHLIGHTY
        global hints
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
                LEVEL = 0
                board_num = randint(0, len(data_ea)-1)
                for i in range (9):
                        for j in range (9):
                                current_board[i][j] = data_ea[board_num][i][j]
                                hints = 3
        if pos[0] > 400 and pos[0] < 700 and pos[1] > 200 and pos[1] < 350 and LEVEL == 1:
                NORMAL = 1
                PLAY = 0
                LEVEL = 0
                board_num = randint(0, len(data_no)-1)
                for i in range (9):
                        for j in range (9):
                                current_board[i][j] = data_no[board_num][i][j]
                                hints = 2
        if pos[0] > 750 and pos[0] < 1050 and pos[1] > 200 and pos[1] < 350 and LEVEL == 1:
                EXTREME = 1
                PLAY = 0
                LEVEL = 0
                board_num = randint(0, len(data_ex)-1)
                for i in range (9):
                        for j in range (9):
                                current_board[i][j] = data_ex[board_num][i][j]
                                hints = 1

        if pos[0] > 750 and pos[0] < 1050 and pos[1] > 525 and pos[1] < 625 and HOME > 4 and HOME < 8:
                EASY = 0
                NORMAL = 0
                EXTREME = 0
                LEVEL = 0
                PLAY = 0
                BACK = 1
                current_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        if pos[0] > 990 and pos[0] < 1050 and pos[1] > 50 and pos[1] < 150 and HOME > 4 and HOME < 8:
                INSTRUCTIONS = 1
        if pos[0] > 750 and pos[0] < 1050 and pos[1] > 275 and pos[1] < 375 and HOME > 4 and HOME < 8:
                HINT = 1
        if pos[0] > 750 and pos[0] < 1050 and pos[1] > 400 and pos[1] < 500 and HOME > 4 and HOME < 8:
                CHECK = 1
       
        #the following are the 1-9 and clear buttons
        if HOME == 5 and pos[0]> 79 and pos[0] < 673 and pos[1] > 29 and pos[1] < 623:
                x_pos = pos[0]
                y_pos = pos[1]
                y = int((x_pos-79)/66)
                x = int((y_pos-29)/66)
                HIGHLIGHTX = x
                HIGHLIGHTY = y
        if HOME == 5 and pos[0]> 750 and pos[0] < 800 and pos[1] > 160 and pos[1] < 210:#number 1 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=1
        if HOME == 5 and pos[0]> 810 and pos[0] < 860 and pos[1] > 160 and pos[1] < 210:#number 2 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=2
        if HOME == 5 and pos[0]> 870 and pos[0] < 920 and pos[1] > 160 and pos[1] < 210:#number 3 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=3
        if HOME == 5 and pos[0]> 930 and pos[0] < 980 and pos[1] > 160 and pos[1] < 210:#number 4 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=4
        if HOME == 5 and pos[0]> 990 and pos[0] < 1040 and pos[1] > 160 and pos[1] < 210:#number 5 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=5
        if HOME == 5 and pos[0]> 750 and pos[0] < 800 and pos[1] > 215 and pos[1] < 265:#number 6 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=6
        if HOME == 5 and pos[0]> 810 and pos[0] < 860 and pos[1] > 215 and pos[1] < 265:#number 7 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=7
        if HOME == 5 and pos[0]> 870 and pos[0] < 920 and pos[1] > 215 and pos[1] < 265:#number 8 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=8
        if HOME == 5 and pos[0]> 930 and pos[0] < 980 and pos[1] > 215 and pos[1] < 265:#number 9 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=9
        if HOME == 5 and pos[0]> 990 and pos[0] < 1040 and pos[1] > 215 and pos[1] < 265:#clear number button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=0
	
        if HOME == 6 and pos[0]> 79 and pos[0] < 673 and pos[1] > 29 and pos[1] < 623:
                x_pos = pos[0]
                y_pos = pos[1]
                y = int((x_pos-79)/66)
                x = int((y_pos-29)/66)
                HIGHLIGHTX = x
                HIGHLIGHTY = y

        if HOME == 6 and pos[0]> 750 and pos[0] < 800 and pos[1] > 160 and pos[1] < 210:#number 1 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=1
        if HOME == 6 and pos[0]> 810 and pos[0] < 860 and pos[1] > 160 and pos[1] < 210:#number 2 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=2
        if HOME == 6 and pos[0]> 870 and pos[0] < 920 and pos[1] > 160 and pos[1] < 210:#number 3 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=3
        if HOME == 6 and pos[0]> 930 and pos[0] < 980 and pos[1] > 160 and pos[1] < 210:#number 4 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=4
        if HOME == 6 and pos[0]> 990 and pos[0] < 1040 and pos[1] > 160 and pos[1] < 210:#number 5 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=5
        if HOME == 6 and pos[0]> 750 and pos[0] < 800 and pos[1] > 215 and pos[1] < 265:#number 6 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=6
        if HOME == 6 and pos[0]> 810 and pos[0] < 860 and pos[1] > 215 and pos[1] < 265:#number 7 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=7
        if HOME == 6 and pos[0]> 870 and pos[0] < 920 and pos[1] > 215 and pos[1] < 265:#number 8 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=8
        if HOME == 6 and pos[0]> 930 and pos[0] < 980 and pos[1] > 215 and pos[1] < 265:#number 9 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=9
        if HOME == 6 and pos[0]> 990 and pos[0] < 1040 and pos[1] > 215 and pos[1] < 265:#clear number button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=0	

        if HOME == 7 and pos[0]> 79 and pos[0] < 673 and pos[1] > 29 and pos[1] < 623:
                x_pos = pos[0]
                y_pos = pos[1]
                y = int((x_pos-79)/66)
                x = int((y_pos-29)/66)
                HIGHLIGHTX = x
                HIGHLIGHTY = y

        if HOME == 7 and pos[0]> 750 and pos[0] < 800 and pos[1] > 160 and pos[1] < 210:#number 1 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=1
        if HOME == 7 and pos[0]> 810 and pos[0] < 860 and pos[1] > 160 and pos[1] < 210:#number 2 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=2
        if HOME == 7 and pos[0]> 870 and pos[0] < 920 and pos[1] > 160 and pos[1] < 210:#number 3 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=3
        if HOME == 7 and pos[0]> 930 and pos[0] < 980 and pos[1] > 160 and pos[1] < 210:#number 4 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=4
        if HOME == 7 and pos[0]> 990 and pos[0] < 1040 and pos[1] > 160 and pos[1] < 210:#number 5 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=5
        if HOME == 7 and pos[0]> 750 and pos[0] < 800 and pos[1] > 215 and pos[1] < 265:#number 6 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=6
        if HOME == 7 and pos[0]> 810 and pos[0] < 860 and pos[1] > 215 and pos[1] < 265:#number 7 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=7
        if HOME == 7 and pos[0]> 870 and pos[0] < 920 and pos[1] > 215 and pos[1] < 265:#number 8 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=8
        if HOME == 7 and pos[0]> 930 and pos[0] < 980 and pos[1] > 215 and pos[1] < 265:#number 9 button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=9
        if HOME == 7 and pos[0]> 990 and pos[0] < 1040 and pos[1] > 215 and pos[1] < 265:#clear number button
                if x_pos!= 0 and y_pos!= 0:
                        y = int((x_pos-79)/66)
                        x = int((y_pos-29)/66)
                        current_board[x][y]=0
        if HOME == 8 and pos[0] > 358 and pos[0] < 658 and pos[1] > 430 and pos[1] < 500:
                EASY = 0
                NORMAL = 0
                EXTREME = 0
                LEVEL = 0
                PLAY = 0
                BACK = 1
		
pgzrun.go()
