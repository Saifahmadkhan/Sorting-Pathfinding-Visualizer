import pygame, sys, random, math
from collections import deque

WHITE = 255, 255, 255
BLACK = 0, 0, 0
LIGHT_BLUE = 25, 120, 250
RED = 255, 0, 0
GREEN = 0, 255, 0

size = (width, height) = 1280, 720
pygame.init()

win = pygame.display.set_mode(size)
pygame.display.set_caption('Breadth First Search')
clock = pygame.time.Clock()

cols, rows = 64, 48

w = width//cols
h = height//rows

grid = []
queue, visited = deque(), []
path = []

class Spot:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False
        # if random.randint(0, 100) < 20:
        #     self.wall = True
        
    def show(self, win, col):
        if self.wall == True:
            col = (0, 0, 0)
        pygame.draw.rect(win, col, (self.x*w, self.y*h, w-1, h-1))
    
    def add_neighbors(self, grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])
        #Add Diagonals
        # if self.x < cols - 1 and self.y < rows - 1:
        #     self.neighbors.append(grid[self.x+1][self.y+1])
        # if self.x < cols - 1 and self.y > 0:
        #     self.neighbors.append(grid[self.x+1][self.y-1])
        # if self.x > 0 and self.y < rows - 1:
        #     self.neighbors.append(grid[self.x-1][self.y+1])
        # if self.x > 0 and self.y > 0:
        #     self.neighbors.append(grid[self.x-1][self.y-1])


def clickWall(pos, state):
    i = pos[0] // w
    j = pos[1] // h
    grid[i][j].wall = state

def place(pos):
    i = pos[0] // w
    j = pos[1] // h
    return w, h

for i in range(cols):
    arr = []
    for j in range(rows):
        arr.append(Spot(i, j))
    grid.append(arr)

for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)

    
start = grid[cols//2][rows//2]
end = grid[cols-1][rows - cols//2]
start.wall = False
end.wall = False

queue.append(start)
start.visited = True

def main():
    flag = False
    noflag = True
    startflag = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # If they press the mouse (any button)
                if event.button in (1, 3):  # And it's a left or right click
                    clickWall(pygame.mouse.get_pos(), event.button==1)  # Click a wall with either (True as a left click or False as not a left click (a right click)
            if event.type == pygame.MOUSEMOTION:
                # event.buttons is a tuple of (x, y, z) e.g. (1, 0, 0) if they're holding a button, x = left click, y = middle and z = right click
                if event.buttons[0] or event.buttons[2]:  # If they're holding left or right click while dragging the mouse
                    clickWall(pygame.mouse.get_pos(), event.buttons[0])  # if the left click is being held, send True, else False (Right click)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    startflag = True

        if startflag:
            if len(queue) > 0:
                current = queue.popleft()
                if current == end:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev 
                    if not flag:
                        flag = True
                        print("Solution found")
                    elif flag:
                        continue
                if flag == False:
                    for i in current.neighbors:
                        if not i.visited and not i.wall:
                            i.visited = True
                            i.prev = current
                            queue.append(i)
            else:
                if noflag and not flag:
                    print("There was no solution")
                    noflag = False
                else:
                    continue


        win.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(win, WHITE)
                if spot in path:
                    spot.show(win, (25, 120, 250))
                elif spot.visited:
                    spot.show(win, (255, 0, 0))
                if spot in queue:
                    spot.show(win, (0, 255, 0))
                if spot == end:
                    spot.show(win, (0, 120, 255))
                
                
        pygame.display.flip()


main()
