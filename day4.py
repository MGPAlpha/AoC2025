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

adjacency_grid = [[0 for _ in range(width)] for __ in range(height)] # Build blank grid of 0's

for y in range(height):
    for x in range(width):
        if sample_grid_location(input,x,y):
            apply_adjacency_kernel(adjacency_grid,x,y,width,height)

total_accessible_rolls = 0

for y in range(height):
    for x in range(width):
        if sample_grid_location(input,x,y) and adjacency_grid[y][x] < 4:
            total_accessible_rolls += 1

print(total_accessible_rolls)
