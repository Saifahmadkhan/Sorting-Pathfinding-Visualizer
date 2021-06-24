import sys
import time
import pygame
import numpy as np

pygame.init()
pygame.display.set_caption("SORTING VISUALIZER")
WINDOW_SIZE = 400, 400
STEP = WINDOW_SIZE[0]/WINDOW_SIZE[1]
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
BLUE_COLOR = (66, 149, 245)
CLOCK = pygame.time.Clock()
FRAMERATE = 30
BACKGROUND_COLOR = WHITE_COLOR
ARRAY_COLOR = BLUE_COLOR
FONT = pygame.font.SysFont("bahnschrift", 30)

array = np.arange(0.0, WINDOW_SIZE[0], STEP)
np.random.shuffle(array)

def display():
	msg="Insertion Sort"
	SCREEN.fill(BACKGROUND_COLOR)
	for i, ele in enumerate(array):
	    pygame.draw.rect(SCREEN, ARRAY_COLOR, [0, i, ele, 1])
	text = FONT.render(msg, True, BLACK_COLOR)
	SCREEN.blit(text, (270, 0))
	pygame.display.update()


def insertion_sort():
	size = WINDOW_SIZE[1]
	for i in range(1, size):
		j = i-1
		key = array[i]
		while j > -1 and array[j] > key:
		    event = check_input()
		    if event == "QUIT":
		        sys.exit()
		    array[j+1] = array[j]
		    j -= 1
		array[j+1] = key
		display()
		CLOCK.tick(30)


def check_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "QUIT"
insertion_sort()
