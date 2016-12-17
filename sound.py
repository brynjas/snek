import pygame 
import os


def music_play():
    
    _path = os.path.join('doc', 'sound', 'title.mp3')
    pygame.mixer.music.load(_path)
    pygame.mixer.music.play(-1)


def music_stop():
    pygame.mixer.music.stop()


def eat_apple():
    sound = pygame.mixer.Sound(os.path.join('doc', 'sound', 'eatapple.ogg'))
    sound.play()


def game_over():
    music_stop()
    sound = pygame.mixer.Sound(os.path.join('doc', 'sound', 'gameover.mp3'))
    sound.play()


def scream():
    sound = pygame.mixer.Sound(os.path.join('doc', 'sound', 'scream.ogg'))
    sound.play()






