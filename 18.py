import time

def getsize_map(direction, units, i, j):
    match direction:
        case 'U':
            for _ in range(units):
                i -= 1
        case 'D':
            for _ in range(units):
                i += 1
        case 'L':
            for _ in range(units):
                j -= 1
        case 'R':
            for _ in range(units):
                j += 1
    return i, j

def travel(input_map, direction, units, i, j):
    match direction:
        case 'U':
            for _ in range(units):
                i -= 1
                input_map[i][j] = '#'
        case 'D':
            for _ in range(units):
                i += 1
                input_map[i][j] = '#'
        case 'L':
            for _ in range(units):
                j -= 1
                input_map[i][j] = '#'
        case 'R':
            for _ in range(units):
                j += 1
                input_map[i][j] = '#'
    return i, j

def fill_inside(dugged_map):#identify how to solve the issue
    for x in dugged_map:
        count = 0
        for i in range(len(x)):
            if x[i] == '#':
                if count < x.count('#') - 1: #this condition should be changed
                    if count == 0:
                        start = i
                    count += 1
                else:
                    for k in range(start+1, i):
                        x[k] = '#'
                    count = 0
    
def part1():
    start_time = time.time()
    result, i, min_i, max_i, j, min_j, max_j = 0, 0, 0, 0, 0, 0, 0
    with open("input/18.txt") as f:
        for x in f:
            i,j = getsize_map(x.split(' ')[0], int(x.split(' ')[1]), i, j)
            if i < min_i: min_i = i
            if j < min_j: min_j = j
            if i > max_i: max_i = i
            if j > max_j: max_j = j
    i, j = 0, 0
    dugged_map = [['.']*(max_j - min_j + 1) for _ in range(max_i - min_i + 1)]
    i -= min_i
    j -= min_j
    with open("input/18.txt") as f:
        for x in f:
            i,j = travel(dugged_map, x.split(' ')[0], int(x.split(' ')[1]), i, j)
    print(dugged_map)
    fill_inside(dugged_map)
    print(dugged_map)
    for x in dugged_map:
        result += x.count('#')
    end_time = time.time()
    print(f'Time to run Part 1 : {end_time - start_time}s')
    return result

def part2():
    start_time = time.time()
    input_map = []
    result = 0
    with open("input/18.txt") as f:
        for x in f:
            input_map.append(x.strip())
            
    end_time = time.time()
    print(f'Time to run Part 2 : {end_time - start_time}s')
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())