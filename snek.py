import pygame
from pygame.locals import *
import random
import os

#other files
import sound
import text
import scores

pygame.init()

ScreenSize = 10
score = 0

FirstLoop = True
Display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('SNEK')
clock = pygame.time.Clock()
FPS = 15

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


def snek(ScreenSize, sneklist):
	# The look of the snek
    for cordinates in sneklist:
        pygame.draw.rect(Display, green, [cordinates[0], cordinates[1], ScreenSize, ScreenSize])

def gameOver(running, GameOver , score):
	# when Game over it will update the score and check if its topscore, then it will display the result 
	# player can quit or try again by hitting space 
		
	image_load("gameover2.png")
	TopScore = scores.get_high_score()
	text.message_centerHigh_screen(('Top Score: ' + str(TopScore) + ' Score: ' + str(score)), green , 30)
	pygame.display.update()
	global FirstLoop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				FirstLoop = False
				game_loop()

			if event.key == pygame.K_q:
				running = False
				GameOver = False
	return(running,GameOver, FirstLoop)


def paused(pause):
	# when the player hit p it will pause the game until he hit any other key
	text.message_CenterCenter_screen("Paused", red )
	sound.music_stop()

	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				sound.music_play()				
				pause = False
				return pause 

		pygame.display.update()
		clock.tick(15)  

def image_load(img):
	# function to load img on the screen
	img = 'doc/img/' + img
	title = pygame.image.load(img)
	Display.blit(title, (0, 0))
	pygame.display.flip()

	

def title():
	# function for the intro when played first 
	waitGame = True
	image_load('start2.png')
	pygame.display.update()
	while waitGame:
		for event in pygame.event.get():         
			if event.type == pygame.KEYDOWN:
				sound.music_play()
				waitGame = False
def game_loop():
    # Varibles
	score = 0
	Running = True
	GameOver = False
	pause = False

	# Snek variables
	snekX = 800 / 2
	snekY = 600 / 2
	snekXupdate = 0
	snekYupdate = 0
	snekLst = []
	snekLength = 1
	# FirstLoop is varible to see if its the firstloop of the game
	global FirstLoop
	# if its the first game then play the intro else not
	if FirstLoop:
		title()
	
	sound.music_play()

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
			gameOver(Running, GameOver, score )

        # snek speed
		snekX += snekXupdate
		snekY += snekYupdate

        # outter boundaries
		if (snekX > 800 - ScreenSize or
			snekX < 0 or
			snekY > 600 - ScreenSize or
			snekY < 0):
				scores.save_high_score(score)
				sound.scream()
				GameOver = True
				sound.music_stop()

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
				sound.scream()
				scores.save_high_score(score)
				GameOver = True
		#updating the snek
		snek(ScreenSize, snekLst)
		
		scores.scoreboard(score)
		pygame.display.update()

		# when the snek eats the apple
		if snekX == AppleX and snekY == AppleY:
			AppleX = round(random.randrange(0, 800 - ScreenSize * 2) / 10) * 10
			AppleY = round(random.randrange(0, 600 - ScreenSize * 2) /10) * 10
			snekLength += 5
			score += 10
			sound.eat_apple()
			scores.scoreboard(score)
     
		clock.tick(FPS)
game_loop()
pygame.quit()
quit()
