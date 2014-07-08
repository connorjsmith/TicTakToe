"""
Connor Smith
Basic Tic-Tak-Toe Program
"""


import pygame
import sys
import time #used for pauses
"""
To do:
	AI
	Keep Score on restart?
"""

pygame.init() #initializes the font
window = pygame.display.set_mode((600,620))
player = "X"
global board
global n
n = 0
board = [ [' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]


def winner(player):
#	display winner screen
	pygame.draw.rect (window,(255,255,255), ((0,200),(600,200)),0)
#	Display winner text
	myfont = pygame.font.SysFont ("monospace", 15) #creates font and font size
	winnerText = 'Player ' +player + ' wins!'
	label = myfont.render(winnerText, 1, (0,0,0)) #draws the text image on a new screen
	textpos = label.get_rect() #centres text in x direction
	textpos.centerx = window.get_rect().centerx #gets the center of the window in the x direction (in this case 300)
	textpos.centery = 300 #sets y position of text
	window.blit (label, textpos) #displays the text, copies the new screen to the main window
	pygame.display.flip()
#Draws Empty Board
def draw():
	#	display endgame screen
	pygame.draw.rect (window,(255,255,255), ((0,200),(600,200)),0)
#	Display winner text
	myfont = pygame.font.SysFont ("monospace", 15) #creates font and font size
	text = 'Draw!'
	label = myfont.render(text, 1, (0,0,0)) #draws the text image on a new screen
	textpos = label.get_rect() #centres text in x direction
	textpos.centerx = window.get_rect().centerx #gets the center of the window in the x direction (in this case 300)
	textpos.centery = 300 #sets y position of text
	window.blit (label, textpos) #displays the text, copies the new screen to the main window
	pygame.display.flip()
def drawBoard ():
	global n
	n = 0
	pygame.draw.rect (window,(0,0,0), ((0,0),(600,600)),0)
	pygame.draw.line (window,(255,255,255), (200,600),(200,0),3)
	pygame.draw.line (window,(255,255,255), (400,600),(400,0),3)
	pygame.draw.line (window,(255,255,255), (0,200),(600,200),3)
	pygame.draw.line (window,(255,255,255), (0,400),(600,400),3)
	
	
#	show the board
	pygame.display.flip()

def checkBoard (n):
	if board[0][0] == board [1][0] and board[1][0] == board[2][0] and board[0][0] != ' ':
		return 1
	elif board[0][1] == board [1][1] and board[1][1] == board[2][1] and board[0][1] != ' ':
		return 1
	elif board[0][2] == board [1][2] and board[1][2] == board[2][2] and board[0][2] != ' ':
		return 1
	elif board[0][0] == board[0][1] and board [0][1] == board[0][2] and board[0][0] != ' ':
		return 1
	elif board[1][0] == board[1][1] and board [1][1] == board[1][2] and board[1][0] != ' ':
		return 1
	elif board[2][0] == board[2][1] and board [2][1] == board[2][2] and board[2][0] != ' ':
		return 1
	elif board [0][0] == board [1][1] and board [1][1] == board [2][2] and board [0][0] != ' ':
		return 1
	elif board [0][2] == board[1][1] and board[1][1] == board [2][0] and board [1][1] != ' ':
		return 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	elif n == 9: #9 moves made with no winner = draw
		return 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	else:
		return 0
def mark (row, col, playerLetter):
	global player
	if playerLetter == "O":
		x = col * 200 + 100
		y = row * 200 + 100
		pygame.draw.circle (window, (255,255,255), (x,y), 95, 3)
		player = "X"
	elif playerLetter == "X":
		x = col * 200 + 5
		y = row * 200 + 5
		pygame.draw.line (window, (255,255,255), (x,y),(x+190,y+190), 3)
		pygame.draw.line (window, (255,255,255), (x,y+190),(x+190,y), 3)
		player = "O"
#
	pygame.draw.rect (window, (0,0,0), (0,600,600,20),0)
	myfont = pygame.font.SysFont ("monospace", 15) #creates font and font size
	text = 'Player ' +player + "'s turn"
	label = myfont.render(text, 1, (255,255,255)) #draws the text image on a new screen
	textpos = label.get_rect() #centres text in x direction
	textpos.centerx = 520 #sets x position of text
	textpos.centery = 610 #sets y position of text
	window.blit (label, textpos) #displays the text, copies the new screen to the main window
#
	pygame.display.flip() #display the marks
def placeMarker (x, y, playerLetter):
	global n
	if x < 200:
		col = 0
	elif x < 400:
		col = 1
	elif x < 600:
		col = 2

	if y < 200:
		row = 0
	elif y < 400:
		row = 1
	elif y < 600:
		row = 2
	if board[row][col] == ' ':
		mark (row, col, playerLetter)
		board [row][col] = playerLetter
		n += 1
	else:
		#display a message that it is occupied
		print "Occupied"
	if checkBoard(n)==1:
		winner(playerLetter)
	elif checkBoard(n)==2:
		draw()
drawBoard()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0) #close the window and return 0
		elif event.type == pygame.MOUSEBUTTONDOWN: #click detected
			print pygame.mouse.get_pos()
			#while event.type != pygame.MOUSEBUTTONUP: #wait till they stop clicking
			x,y = event.pos
			placeMarker (x,y,player)
		else:
			print (event)
	if checkBoard(n) != 0:
		time.sleep(5)
		board = [ [' ',' ',' '], [' ',' ',' '], [' ',' ',' ']] #reset board
		drawBoard() #erase screen and reset



