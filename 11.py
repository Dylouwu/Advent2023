import time

def scan_map(lines, count):
    input_map = []
    for i, line in enumerate(lines):
        line = ''.join(line).replace('\n', '')
        if "#" not in line and count == 0:
            input_map.append(line)
        elif "#" not in line and count == 2:
            input_map.append(i)
        if count != 2:
            input_map.append(line)
        
    return input_map

def part1():
    st = time.time()
    sum = 0
    x_galaxies = []
    y_galaxies = []
    with open("input/11.txt") as f:
        input_map = scan_map(f, 0)
    input_map = scan_map(zip(*input_map), 0)
    for i, x in enumerate(input_map):
        for j, y in enumerate(x):
            if y != ".":
                x_galaxies.append(i)
                y_galaxies.append(j)
    for i, x in enumerate(x_galaxies):
        for j, y in enumerate(x_galaxies[i+1:], i+1):
            sum += (abs(y_galaxies[i] - y_galaxies[j]) + abs(x - y))

    et = time.time()
    print(f'Time to run Part 1 : {et-st}s')      
    return sum

def part2():
    st = time.time()
    sum = 0
    a = 0
    b = 0
    point_lines = []
    point_columns = []
    x_galaxies = []
    y_galaxies = []
    with open("input/11.txt") as f:   
        initial_map = scan_map(f, 1)
    point_lines = scan_map(initial_map, 2)      
    for j, y in enumerate(initial_map[0]):
        hash = False
        for i, x in enumerate(initial_map):
            if x[j] == "#":
                hash = True
        if hash == False:
            point_columns.append(j)

    for i, x in enumerate(initial_map):
        if i in point_lines:
            a += 999999
        b = 0
        for j, y in enumerate(initial_map[0]):
            if j in point_columns:
                b += 999999
            if initial_map[i][j] != ".":
                x_galaxies.append(i + a)
                y_galaxies.append(j + b)

    for i, x in enumerate(x_galaxies):
        for j, y in enumerate(x_galaxies[i+1:], i+1):
            sum += (abs(y_galaxies[i] - y_galaxies[j]) + abs(x - y))

    et = time.time()
    print(f'Time to run Part 2 : {et - st}s')
    return sum 

if __name__ == "__main__":
    print(part1())
    print(part2())