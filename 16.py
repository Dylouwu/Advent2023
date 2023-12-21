import time
import sys
sys.setrecursionlimit(100000)
def travel(input_map, x, y, direction, visited, energized):
    if (x, y, direction) in visited or x < 0 or x > len(input_map) - 1 or y < 0 or y > len(input_map[0]) - 1:
        return
    visited.add((x, y, direction))
    energized.add((x, y))
    match input_map[x][y]:
        case '.':
            if direction == 'N':
                travel(input_map, x - 1, y, direction, visited, energized)
            elif direction == 'S':
                travel(input_map, x + 1, y, direction, visited, energized)
            elif direction == 'W':
                travel(input_map, x, y - 1, direction, visited, energized)
            else:
                travel(input_map, x, y + 1, direction, visited, energized)
        case '/':
            if direction == 'N':
                travel(input_map, x, y + 1, 'E', visited, energized)
            elif direction == 'S':
                travel(input_map, x, y - 1, 'W', visited, energized)
            elif direction == 'W':
                travel(input_map, x + 1, y, 'S', visited, energized)
            else:
                travel(input_map, x - 1, y, 'N', visited, energized)
        case '\\':
            if direction == 'N':
                travel(input_map, x, y - 1, 'W', visited, energized)
            elif direction == 'S':
                travel(input_map, x, y + 1, 'E', visited, energized)
            elif direction == 'W':
                travel(input_map, x - 1, y, 'N', visited, energized)
            else:
                travel(input_map, x + 1, y, 'S', visited, energized)
        case '|':
            if direction == 'N':
                travel(input_map, x - 1, y, direction, visited, energized)
            elif direction == 'S':
                travel(input_map, x + 1, y, direction, visited, energized)
            else:
                travel(input_map, x - 1, y, 'N', visited, energized)
                travel(input_map, x + 1, y, 'S', visited, energized)
        case '-':
            if direction == 'W':
                travel(input_map, x, y - 1, direction, visited, energized)
            elif direction == 'E':
                travel(input_map, x, y + 1, direction, visited, energized)
            else:
                travel(input_map, x, y - 1, 'W', visited, energized)
                travel(input_map, x, y + 1, 'E', visited, energized)
                
    return len(energized)


def part1():
    start_time = time.time()
    input_map = []
    visited = set()
    with open("input/16.txt") as f:
        for x in f:
            input_map.append(x.strip())
    result = travel(input_map, 0, 0, 'E', set(), set())
    
    end_time = time.time()
    print(f'Time to run Part 1 : {end_time - start_time}s')
    return result
    

def part2():
    start_time = time.time()
    input_map = []
    result = 0
    with open("input/16.txt") as f:
        for x in f:
            input_map.append(x.strip())
    for i in range(len(input_map)-1):
        temp = travel(input_map, i, 0, 'E', set(), set())
        if temp > result:
            result = temp
        temp = travel(input_map, i, len(input_map[0])-1, 'W', set(), set())
        if temp > result:
            result = temp
    for j in range(len(input_map[0])-1):
        temp = travel(input_map, len(input_map)-1, j, 'N', set(), set())
        if temp > result:
            result = temp
        temp = travel(input_map, 0, j, 'S', set(), set())
        if temp > result:
            result = temp
    
    end_time = time.time()
    print(f'Time to run Part 2 : {end_time - start_time}s')
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())