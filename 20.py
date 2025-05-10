import time

def part1():
    start_time = time.time()
    input_map = []
    result = 0
    with open("input/20.txt") as f:
        for x in f:
            input_map.append(x.strip())
            
    end_time = time.time()
    print(f'Time to run Part 1 : {end_time - start_time}s')
    return result

def part2():
    start_time = time.time()
    input_map = []
    result = 0
    with open("input/20.txt") as f:
        for x in f:
            input_map.append(x.strip())
            
    end_time = time.time()
    print(f'Time to run Part 2 : {end_time - start_time}s')
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())