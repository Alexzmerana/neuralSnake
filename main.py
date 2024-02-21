import pygame
from pynput import keyboard
from game import Game

pygame.init()

game = Game()

game.run_loop()

pygame.quit()
quit()