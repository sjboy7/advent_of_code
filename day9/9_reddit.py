with open('9_input') as f:
    rawinput = f.read()[:50]

lengths = [int(num) for num in rawinput]

grid = [i//2 if i%2==0 else -1 for i,num in enumerate(lengths) for _ in range(num)]

while -1 in grid:
    if grid[-1] == (-1):
        grid.pop()
    else:
        index = grid.index(-1)
        grid[index] = grid.pop()
print(grid)
# answer = sum(i*num for i,num in enumerate(grid))
# print(answer)