#!/usr/env/bin 
import time

# grid size 
COLS = 25
ROWS = 25  

# symbols for the status
ALIVE = '*'
DEAD = '.'

# GRID CELLS is just COLS * ROWS
GRID_CELLS = COLS * ROWS


# the function sets the specified sell at x,y to the specified state 
def set_cell(grid: str,x: int,y: int,state: int):
    grid[cell_to_index(x,y)] = state


# returns the state of the grid at x,y 
def get_cell(grid: str,x: int,y: int):
    return grid[cell_to_index(x,y)]


# translate the specified x,y grid point into a index in the linear array
# this function implements wrapping, so both negative and positive coordinates
# that are out of the grid will wrap around  
def cell_to_index(x: int,y: int):
    if x >= COLS:
        x = x % COLS
    if y >= ROWS:
        y = y % ROWS

    # for the negative case
    if x < 0:
        x = (-x) % COLS 
        x = COLS - x

    if y < 0:
        y = (-y) % ROWS
        y = ROWS - y 
    

    return y*COLS+x

#render the grid on the screen
def print_grid(grid: str):
    # clear the screen; using some magic numbers for VT100 terminal escape sequence
    print("\x1b[3J\x1b[H\x1b[2J",end='')
    for y in range(0,ROWS):
        for x in range(0,COLS):
            print(f"{get_cell(grid,x,y)}",end='')
        print('\n',end='')


# set all the grid cells to the specified state
def set_grid(grid: str,state: str):
    for y in range(0,ROWS):
        for x in range(0,COLS):
            set_cell(grid,x,y,state)


# return the number of living cells neighbours of x,y
def count_living_neighbours(grid: str,x: int,y: int):
    alive = 0
    for y0 in range(-1,2):
        for x0 in range(-1,2):
            if (x0 == 0 and y0 == 0):
                continue
            if (get_cell(grid,x+x0,y+y0) == ALIVE):
                alive+=1

    return alive  

# compute the new state of Game of life from the rules
def compute_new_state(old: str, new: str):
    for y in range(0,ROWS):
        for x in range(0,COLS):
            n_alive = count_living_neighbours(old,x,y)
            new_state = DEAD
            if (get_cell(old,x,y) == ALIVE):
                if(n_alive == 2 or n_alive == 3):
                    new_state = ALIVE
            else:
                if n_alive == 3:
                    new_state = ALIVE

            set_cell(new,x,y,new_state)

def main():
    old_grid = [''] * GRID_CELLS
    new_grid = [''] * GRID_CELLS

    set_grid(old_grid,DEAD)
    set_cell(old_grid,10,10,ALIVE)
    set_cell(old_grid,9,10,ALIVE)
    set_cell(old_grid,11,10,ALIVE)
    set_cell(old_grid,11,9,ALIVE)
    set_cell(old_grid,10,9,ALIVE)

    while True:
        compute_new_state(old_grid,new_grid)
        print_grid(new_grid)
        time.sleep(100)
        compute_new_state(new_grid,old_grid)
        print_grid(old_grid)
        time.sleep(100)        

    

if __name__ == "__main__":
    main()
