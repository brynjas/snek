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

def message_to_screen(msg, color):
	# this is text in the middle center
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects(msg, largeText,color)
    TextRect.center = ((800/2), (600/2))
    Display.blit(TextSurf, TextRect)

def message_up_screen(msg, color, size):
	# this is text in the top center
	font = pygame.font.Font(None, size)
	text = font.render(msg, 1, (color))
	textpos = text.get_rect(centerx=Display.get_width()/2)
	Display.blit(text, textpos)
