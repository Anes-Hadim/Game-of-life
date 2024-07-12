import pygame
import sys
import random

pygame.init()

width, height = 1200, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Game of Life")

white = (255, 255, 255)
grey = (60, 60, 60)

cell_size = 10

grid = []
for i in range(0, height, cell_size):
    row = []
    for j in range(0, width, cell_size):
        # row.append(random.randint(0, 1))
        row.append(0)
    grid.append(row)

gun_pattern = [
    (5, 1), (5, 2), (6, 1), (6, 2),
    (5, 11), (6, 11), (7, 11), (4, 12), (8, 12), (3, 13), (9, 13),
    (3, 14), (9, 14), (6, 15), (4, 16), (8, 16), (5, 17), (6, 17), (7, 17),
    (6, 18),
    (3, 21), (4, 21), (5, 21), (3, 22), (4, 22), (5, 22), (2, 23), (6, 23),
    (1, 25), (2, 25), (6, 25), (7, 25),
    (3, 35), (4, 35), (3, 36), (4, 36)
]

# Set the gun pattern on the grid
for (i, j) in gun_pattern:
    grid[i][j] = 1

def counts(grid, i, j):
    counter = 0
    for vert in range(-1, 2):
        for horz in range(-1, 2):
           if vert == 0 and horz == 0:
               continue
           else:
               new_i = i + vert
               new_j = j + horz
               if new_i in range(height // cell_size) and new_j in range(width // cell_size) and grid[new_i][
                   new_j] == 1:
                   counter = 1 + counter
    return counter

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(grey)

    for i in range(height // cell_size):
        for j in range(width // cell_size):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, white, (j*cell_size, i*cell_size, cell_size, cell_size))
            if grid[i][j] == 0:
                pygame.draw.rect(screen, grey, (j*cell_size, i*cell_size, cell_size, cell_size))

    for i in range(0, height, cell_size):
        pygame.draw.line(screen, white, (0, i), (width, i), 1)

    for i in range(0, width, cell_size):
        pygame.draw.line(screen, white, (i, 0), (i, height), 1)

    # game logic
    copy_grid = []
    for i in grid:
        copy_grid.append(i[:])

    for i in range(height // cell_size):
        for j in range(width // cell_size):
            if copy_grid[i][j] == 1:
               counter = counts(copy_grid, i, j)
               if counter != 2 and counter != 3:
                   grid[i][j] = 0
            else:
               counter = counts(copy_grid, i, j)
               if counter == 3:
                  grid[i][j] = 1


    pygame.display.flip()
    clock.tick(10)


pygame.quit()
sys.exit()
