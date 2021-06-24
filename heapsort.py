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
		msg="Heap Sort"
		SCREEN.fill(BACKGROUND_COLOR)
		for i, ele in enumerate(array):
		    pygame.draw.rect(SCREEN, ARRAY_COLOR, [0, i, ele, 1])
		text = FONT.render(msg, True, BLACK_COLOR)
		SCREEN.blit(text, (270, 0))
		pygame.display.update()


def heapify(size, index):
    event = check_input()
    if event == "QUIT":
        sys.exit()
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and array[largest] < array[left]:
        largest = left
    if right < size and array[largest] < array[right]:
        largest = right
    if largest != index:
        array[index], array[largest] = array[largest], array[index] 
        heapify(size, largest)

def heap_sort():
    size = len(array)
    for i in range(size//2 - 1, -1, -1):
        heapify(size, i)
    for i in range(size-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(i, 0)
        display()
        CLOCK.tick(30)

def check_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "QUIT"
heap_sort()
