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
    for cordinates in sneklist:
        pygame.draw.rect(Display, green, [cordinates[0], cordinates[1], ScreenSize, ScreenSize])

#reference https://pythonprogramming.net/displaying-text-pygame-screen/
def text_objects(msg, font, color):
    textSurface = font.render(msg, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color):
    largeText = pygame.font.SysFont("comicsansms", 24)
    TextSurf, TextRect = text_objects(msg, largeText,color)
    TextRect.center = ((800/2), (600/2))
    Display.blit(TextSurf, TextRect)

def message_up_screen(msg, color, size):
	font = pygame.font.Font(None, size)
	text = font.render(msg, 1, (color))
	textpos = text.get_rect(centerx=Display.get_width()/2)
	Display.blit(text, textpos)
    

def get_high_score():
    try:
        high_score_file = open("top_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
    except:
        print("There is no high score yet.")

    return (high_score)
  
def save_high_score(new_high_score):
	top_score = get_high_score()
	if new_high_score > top_score:
		try:
			high_score_file = open("top_score.txt", "w")
			high_score_file.write(str(new_high_score))
			high_score_file.close()
		except:
			print("Unable to save the high score.")

def scoreboard(score):
	return message_up_screen(str(score), white , 36)

def gameOver(running, game_over , score):
	#Display.fill(white)
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
				game_over = False
	return(running,game_over)

def paused(pause):
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
    # game variables
	score = 0

	running = True
	game_over = False
	pause = False
	#TopScore = high_score

	# snek lead variables
	snekX = 800 / 2
	snekY = 600 / 2
	snekXupdate = 0
	snekYupdate = 0
	snekLst = []
	snekLength = 1

    # apple stuff
	rand_apple_x = round(random.randrange(0, 800 - ScreenSize * 2) / 10) * 10
	rand_apple_y = round(random.randrange(0, 600 - ScreenSize * 2) /10) * 10
   
	while running:
       # event handling
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
		while game_over:
			gameOver(running, game_over, score)


        # snek speed
		snekX += snekXupdate
		snekY += snekYupdate

        # outter boundaries
		if (snekX > 800 - ScreenSize or
			snekX < 0 or
			snekY > 600 - ScreenSize or
			snekY < 0):
				save_high_score(score)
				game_over = True

        # draw and updoot
		Display.fill(black)
		pygame.draw.rect(Display, red, [rand_apple_x, rand_apple_y,ScreenSize, ScreenSize])

		snek_head = []
		snek_head.append(snekX)
		snek_head.append(snekY)
		snekLst.append(snek_head)

        # prevent snek from increasing length constantly
		if len(snekLst) > snekLength:
			del snekLst[0]

		for part in snekLst[:-1]:
			if part == snek_head:
				save_high_score(score)
				game_over = True

		snek(ScreenSize, snekLst)
		
		scoreboard(score)
		pygame.display.update()



        # snek eat apple
		if snekX == rand_apple_x and snekY == rand_apple_y:
			rand_apple_x = round(random.randrange(0, 800 - ScreenSize * 2) / 10) * 10
			rand_apple_y = round(random.randrange(0, 600 - ScreenSize * 2) /10) * 10
			snekLength += 5
			score += 10
			scoreboard(score)
     

		clock.tick(FPS)
#get_high_score()
game_loop()
pygame.quit()
quit()
