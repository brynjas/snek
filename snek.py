import pygame
from pygame.locals import *
import random

pygame.init()

ScreenSize = 10
score = 0

Display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('SNEK')
clock = pygame.time.Clock()
FPS = 15

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 255, 0)

def snek(ScreenSize, sneklist):
	# The look of the snek
    for cordinates in sneklist:
        pygame.draw.rect(Display, green, [cordinates[0], cordinates[1], ScreenSize, ScreenSize])

#reference https://pythonprogramming.net/displaying-text-pygame-screen/
def text_objects(msg, font, color):
    textSurface = font.render(msg, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color):
	# this is text in the middle center
    largeText = pygame.font.SysFont("comicsansms", 24)
    TextSurf, TextRect = text_objects(msg, largeText,color)
    TextRect.center = ((800/2), (600/2))
    Display.blit(TextSurf, TextRect)

def message_up_screen(msg, color, size):
	# this is text in the top center
	font = pygame.font.Font(None, size)
	text = font.render(msg, 1, (color))
	textpos = text.get_rect(centerx=Display.get_width()/2)
	Display.blit(text, textpos)
    

def get_high_score():
	#read the higest score from txt file
    try:
        high_score_file = open("top_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
    except:
        print("There is no high score yet.")

    return (high_score)
  
def save_high_score(new_high_score):
	# save the higest score in txt file it's saved 
	top_score = get_high_score()
	if new_high_score > top_score:
		try:
			high_score_file = open("top_score.txt", "w")
			high_score_file.write(str(new_high_score))
			high_score_file.close()
		except:
			print("Unable to save the high score.")

def scoreboard(score):
	#the scoreboard for the game 
	return message_up_screen(str(score), white , 36)

def gameOver(running, GameOver , score):
	# when Game over it will update the score and check if its topscore, then it will display the result 
	# player can quit or try again by hitting space 
	Display.fill(white)
	TopScore = get_high_score()
	message_to_screen('GAME OVER', red)
	message_up_screen(('Top Score: ' + str(TopScore) + ' Score: ' + str(score)), green, 36)
	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				game_loop()

			if event.key == pygame.K_q:
				running = False
				GameOver = False
	return(running,GameOver)

def paused(pause):
	# when the player hit p it will pause the game until he hit any other key
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText, red)
    TextRect.center = ((800/2),(600/2))
    Display.blit(TextSurf, TextRect)    
    while pause:
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		pygame.quit()
        		quit()
        	if event.type == pygame.KEYDOWN:
        		pause = False
        		return pause 

        pygame.display.update()
        clock.tick(15)  

def game_loop():
    # Varibles
	score = 0

	Running = True
	GameOver = False
	pause = False
	#TopScore = high_score

	# Snek variables
	snekX = 800 / 2
	snekY = 600 / 2
	snekXupdate = 0
	snekYupdate = 0
	snekLst = []
	snekLength = 1

    # The apple
	AppleX = round(random.randrange(0, 800 - ScreenSize * 2) / 10) * 10
	AppleY = round(random.randrange(0, 600 - ScreenSize * 2) /10) * 10
   
	while Running:
		# for the events in the game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()          
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					pause = True
					paused(pause)
				if event.key == pygame.K_DOWN:
					if snekYupdate != -ScreenSize:
						snekXupdate = 0
						snekYupdate = ScreenSize
				if event.key == pygame.K_LEFT:
					if snekXupdate != ScreenSize:
						snekYupdate = 0
						snekXupdate = -ScreenSize
				if event.key == pygame.K_UP:
					if snekYupdate != ScreenSize:
						snekXupdate = 0
						snekYupdate = -ScreenSize
				if event.key == pygame.K_RIGHT:
					if snekXupdate != -ScreenSize:
						snekYupdate = 0
						snekXupdate = ScreenSize
		while GameOver:
			gameOver(Running, GameOver, score)

        # snek speed
		snekX += snekXupdate
		snekY += snekYupdate

        # outter boundaries
		if (snekX > 800 - ScreenSize or
			snekX < 0 or
			snekY > 600 - ScreenSize or
			snekY < 0):
				save_high_score(score)
				GameOver = True

		#Draw and update changes
		Display.fill(black)
		pygame.draw.rect(Display, red, [AppleX, AppleY,ScreenSize, ScreenSize])

		snekHead = []
		snekHead.append(snekX)
		snekHead.append(snekY)
		snekLst.append(snekHead)

		if len(snekLst) > snekLength:
			del snekLst[0]

		#if the snek is on him self
		for part in snekLst[:-1]:
			if part == snekHead:
				save_high_score(score)
				GameOver = True
		#updating the snek
		snek(ScreenSize, snekLst)
		
		scoreboard(score)
		pygame.display.update()

		# when the snek eats the apple
		if snekX == AppleX and snekY == AppleY:
			AppleX = round(random.randrange(0, 800 - ScreenSize * 2) / 10) * 10
			AppleY = round(random.randrange(0, 600 - ScreenSize * 2) /10) * 10
			snekLength += 5
			score += 10
			scoreboard(score)
     

		clock.tick(FPS)
game_loop()
pygame.quit()
quit()
