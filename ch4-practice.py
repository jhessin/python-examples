def commaCode(someList: list[str]):
    result = ''
    for i in range(len(someList)):
        if i == len(someList) - 1:
            result += 'and ' + someList[i]
        else:
            result += someList[i] + ', '
    return result

def characterPictureGrid(grid: list[list[str]]):
    x = 0
    y = 0
    while y < len(grid[x]):
        while x < len(grid):
            print(grid[x][y], end='')
            x += 1
        print()
        y += 1
        x = 0

print(commaCode(['apples', 'bananas', 'tofu', 'cats']))

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

characterPictureGrid(grid)
