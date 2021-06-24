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
		msg="Merge Sort"
		SCREEN.fill(BACKGROUND_COLOR)
		for i, ele in enumerate(array):
		    pygame.draw.rect(SCREEN, ARRAY_COLOR, [0, i, ele, 1])
		text = FONT.render(msg, True, BLACK_COLOR)
		SCREEN.blit(text, (270, 0))
		pygame.display.update()


def merge(start, mid, end):
	  start2 = mid + 1

	  if array[mid] <= array[start2]:
	      return
	  while start <= mid and start2 <= end:
	      if array[start] <= array[start2]:
	          start += 1
	      else:
	          value = array[start2]
	          index = start2
	          while index != start:
	              array[index] = array[index - 1]
	              index -= 1
	          array[start] = value
	          start += 1
	          mid += 1
	          start2 += 1

def merge_sort(left, right):
    event = check_input()
    if event == "QUIT":
        sys.exit()
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        display()  
        merge(left, mid, right)
        display()
        CLOCK.tick(30)

def check_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "QUIT"
merge_sort(0, WINDOW_SIZE[1]-1)
