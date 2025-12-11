def sample_grid_location(grid,x,y):
    if grid[y][x] == "@":
        return True
    return False

def increment_adjacency_grid(grid,x,y,w,h):
    if x < 0 or x >= w or y < 0 or y >= h:
        return
    grid[y][x] += 1

def apply_adjacency_kernel(grid,x,y,w,h):
    for j in [-1,0,1]:
        for i in [-1,0,1]:
            if i == 0 and j == 0: continue
            increment_adjacency_grid(grid,x+i,y+j,w,h)

input = []

with open("day4input.txt", "r") as file:
    input = file.read().split("\n")[:-1]

width = len(input[0])
height = len(input)

grid = [[input[j][i] for i in range(width)] for j in range(height)]

total_removed_rolls = 0
more_rolls_removable = True

while more_rolls_removable:

    more_rolls_removable = False
    adjacency_grid = [[0 for _ in range(width)] for __ in range(height)] # Build blank grid of 0's

    for y in range(height):
        for x in range(width):
            if sample_grid_location(grid,x,y):
                apply_adjacency_kernel(adjacency_grid,x,y,width,height)


    for y in range(height):
        for x in range(width):
            if sample_grid_location(grid,x,y) and adjacency_grid[y][x] < 4:
                grid[y][x] = "."
                total_removed_rolls += 1
                more_rolls_removable = True


print(total_removed_rolls)
