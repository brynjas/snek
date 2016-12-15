import pygame 
import os


def music_play(song):
    _path = os.path.join('doc', 'sound', song)
    pygame.mixer.music.load(_path)
    pygame.mixer.music.play(-1)


def music_stop():
    pygame.mixer.music.stop()


def eat_apple():
    sound = pygame.mixer.Sound(os.path.join('doc', 'sound', 'eatapple.ogg'))
    sound.play()


def begin():
    sound = pygame.mixer.Sound(os.path.join('doc', 'sound', 'beginning.ogg'))
    sound.play()


def game_over():
    sound = pygame.mixer.Sound(os.path.join('doc', 'sound', 'gameover.ogg'))
    sound.play()



def scream():
    sound = pygame.mixer.Sound(os.path.join('doc', 'sound', 'scream.ogg'))
    sound.play()


def startgame():
    sound = pygame.mixer.Sound(os.path.join('doc', 'sound', 'startgame.ogg'))
    sound.play()



