import time

def maxing1(input_map):
    length = len(input_map)
    if length < 2:
        return 0
    maximum = 0
    for i in range(length-1):
        difference = 1
        error = 0
        while True:
            if i - difference + 1 < 0 and length - 1 - (length - difference) > maximum:
                maximum = length - 1 - (length - difference) 
                break
            if length - 1 < i + difference and length - difference + 1 > maximum: 
                maximum = length - difference + 1
                break         
            if input_map[i-difference+1] == input_map[i+difference]:
                difference += 1
            else:
                break
    return maximum
    
def part1():
    start_time = time.time()
    result = 0
    input_maps = []
    with open("input/13.txt") as f:
        input_map = []
        for line in f:
            line = line.strip()
            if line != '':
                input_map.append(line)
            elif input_map != '':
                input_maps.append(input_map)
                input_map = []
    if input_map != '':
        input_maps.append(input_map)
    for x in input_maps:
        maximum_cols = maxing1(x)
        maximum_rows = maxing1(list(map(list, zip(*x))))
        if(maximum_rows >= maximum_cols):
            maximum = maximum_rows
        else:
            maximum = maximum_cols*100
        result += maximum

    end_time = time.time()
    print(f'Time to run Part 1: {end_time - start_time}s')
    return result

def diff(a, b):
    return [i for i in range(len(a)) if a[i] != b[i]]

def maxing2(input_map):
    length = len(input_map)
    if length < 2:
        return 0
    maximum = 0
    for i in range(length-1):
        difference = 1
        error = 0
        while True:
            if length - 1 < i + difference:
                if error == 1 and difference - 1 > maximum:
                    maximum = length - (difference - 1)
                break
            if i - difference + 1 < 0 :
                if error == 1 and difference - 1 > maximum:
                    maximum = difference - 1
                break
            num_diff = diff(input_map[i - difference + 1], input_map[i + difference])
            if input_map[i - difference + 1] == input_map[i + difference]:
                difference += 1
            elif len(num_diff) == 1 and error == 0:
                error += 1
                difference += 1
            else:
                break
    return maximum

def part2():
    start_time = time.time()
    result = 0
    input_maps = []
    with open("input/13.txt") as f:
        input_map = []
        for line in f:
            line = line.strip()
            if line != '':
                input_map.append(line)
            elif input_map != '':
                input_maps.append(input_map)
                input_map = []
    if input_map != '':
        input_maps.append(input_map)
    for x in input_maps:
        maximum_cols = maxing2(x)
        maximum_rows = maxing2(list(map(list, zip(*x))))
        if(maximum_rows >= maximum_cols):
            maximum = maximum_rows
        else:
            maximum = maximum_cols*100
        result += maximum

    end_time = time.time()
    print(f'Time to run Part 2 : {end_time - start_time}s')
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())