grid = [['x' for i in range(4)] for j in range(6)]
px,py = 0,0
grid[py][px] = 'O'
while True:
    for row in grid:
        print(row)
    grid[py][px] = 'x'
    coordinates = input('Please eneter a coordinate in the format: x,y > ')
    px = int(coordinates[0])-1
    py = int(coordinates[-1])-1
    grid[py][px] = 'O'