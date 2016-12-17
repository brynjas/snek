import pygame 
import os


ScreenSize = 10

Display = pygame.display.set_mode((800, 600))


# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 255, 0)

#reference https://pythonprogramming.net/displaying-text-pygame-screen/
def text_objects(msg, font, color):
    textSurface = font.render(msg, True, color)
    return textSurface, textSurface.get_rect()

def message_CenterCenter_screen(msg, color):
	Myfont = pygame.font.Font("doc/fonts/8bit.TTF", 46)
	TextSurf, TextRect = text_objects(msg, Myfont,color)
	TextRect.center = ((800/2), (600/2))
	Display.blit(TextSurf, TextRect)

def message_CenterHiger_screen(msg, color):
	Myfont = pygame.font.Font("doc/fonts/8bit.TTF", 46)
	TextSurf, TextRect = text_objects(msg, Myfont,color)
	text = Myfont.render(msg, 1, (color))
	textpos = text.get_rect(centerx=Display.get_width()/2, centery=Display.get_width()/5)
	Display.blit(TextSurf, TextRect)




def message_up_screen(msg, color, size):
	font = pygame.font.Font("doc/fonts/Peepo.ttf", size)
	text = font.render(msg, 1, (color))
	textpos = text.get_rect(centerx=Display.get_width()/2)

	Display.blit(text, textpos)


def message_centerHigh_screen(msg, color, size):
	font = pygame.font.Font("doc/fonts/upheavtt.ttf", size)
	text = font.render(msg, 1, (color))
	textpos = text.get_rect(centerx=Display.get_width()/2, centery=Display.get_width()/5)

	Display.blit(text, textpos)







