import time

def north(rock: str, input_map: list, i: int, j: int) -> list:
    if i - 1 < 0:
        return input_map
    if input_map[i-1][j] == '.' and rock == 'O':
        above = list(input_map[i-1])
        above[j] = 'O'
        current = list(input_map[i])
        current[j] = '.'
        input_map[i-1] = ''.join(above)
        input_map[i] = ''.join(current)
        north('O', input_map, i-1, j)
    
    return input_map

def south(rock: str, input_map: list, i: int, j: int) -> list:
    if i + 1 > len(input_map)-1:
        return input_map
    if input_map[i+1][j] == '.' and rock == 'O':
        below = list(input_map[i+1])
        below[j] = 'O'
        current = list(input_map[i])
        current[j] = '.'
        input_map[i+1] = ''.join(below)
        input_map[i] = ''.join(current)
        south('O', input_map, i+1, j)
    
    return input_map

def west(rock: str, input_map: list, i: int, j: int) -> list:
    if j - 1 < 0:
        return input_map
    if input_map[i][j-1] == '.' and rock == 'O':
        left = list(input_map[i])
        left[j-1] = 'O'
        input_map[i] = ''.join(left)
        input_map[i] = input_map[i][:j] + '.' + input_map[i][j + 1:]
        west('O', input_map, i, j-1)

    return input_map

def east(rock: str, input_map: list, i: int, j: int) -> list:
    if j + 1 > len(input_map[i]) - 1:
        return input_map
    if input_map[i][j + 1] == '.' and rock == 'O':
        right = list(input_map[i])
        right[j + 1] = 'O'
        input_map[i] = ''.join(right)
        input_map[i] = input_map[i][:j] + '.' + input_map[i][j + 1:]
        east('O', input_map, i, j + 1)

    return input_map

def part1():
    start_time = time.time()
    result = 0
    input_map = []
    with open("input/14.txt") as f:
        for x in f:
            input_map.append(x.strip())
    for i, x in enumerate(input_map):
        for j, y in enumerate(x):
            input_map = north(y, input_map, i, j)
    for i, x in enumerate(input_map):
        result += x.count('O')*(len(x)-i)
    end_time = time.time()
    print(f'Time to run Part 1 : {end_time - start_time}s')
    return result

def part2():
    start_time = time.time()
    result = 0
    input_map = []
    with open("input/14.txt") as f:
        for x in f:
            input_map.append(x.strip())
    for _ in range(1000):
        for i, x in enumerate(input_map):
            for j, y in enumerate(x):
                input_map = north(y, input_map, i, j)
        for i, x in enumerate(input_map):
            for j, y in enumerate(x):
                input_map = west(y, input_map, i, j)
        for i in reversed(range(len(input_map))):
            for j, y in enumerate(input_map[i]):
                input_map = south(y, input_map, i, j)
        for i in reversed(range(len(input_map[0]))):
            for j in range(len(input_map)):
                input_map = east(input_map[j][i], input_map, j, i)
    for i, x in enumerate(input_map):
        result += x.count('O')*(len(x)-i)
    end_time = time.time()
    print(f'Time to run Part 2 : {end_time - start_time}s')
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())