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
    msg="Quick Sort"
    SCREEN.fill(BACKGROUND_COLOR)
    for i, ele in enumerate(array):
        pygame.draw.rect(SCREEN, ARRAY_COLOR, [0, i, ele, 1])
    text = FONT.render(msg, True, BLACK_COLOR)
    SCREEN.blit(text, (270, 0))
    pygame.display.update()

def partition(low, high):
    i = (low-1)
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quick_sort(low, high):
    if len(array) == 1:
        return
    event = check_input()
    if event == "QUIT":
        sys.exit()
    if low < high: 
        index = partition(low, high)
        display()
        quick_sort(low, index-1)
        display()
        quick_sort(index+1, high)
        display()
        CLOCK.tick(30)

def check_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "QUIT"
quick_sort(0, WINDOW_SIZE[1]-1)
