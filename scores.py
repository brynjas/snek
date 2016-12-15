import pygame 
import os
import text

ScreenSize = 10

Display = pygame.display.set_mode((800, 600))


# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 255, 0)




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
	return text.message_up_screen(str(score), white , 36)
