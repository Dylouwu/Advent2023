import time
#Bruteforce all possible combinations define a list . # according to the right combination
def is_possible(springs: str, sizes: list[int]) -> int:
    if not sizes:
        return int(all(char != '#' for char in springs))
    if sum(sizes) > len(springs):
        return 0
    char = springs[0]
    current_size = sizes[0]
    if char == '.':
        return is_possible(springs[1:], sizes)
    count = 0
    if char == '?':
        count += is_possible(springs[1:], sizes)
    condition = (springs[current_size] if len(springs) > current_size else '.') != '#' and all(char != '.' for char in springs[:current_size])
    if condition:
        count += is_possible(springs[current_size + 1:], sizes[1:])

    return count

    
def part1():
    start_time = time.time()
    result = 0
    input_map = []
    with open("input/12.txt") as f:
        input_map = [line.strip() for line in f]
    for line in input_map:
        springs, sizes = line.split(" ")
        sizes = [int(x) for x in sizes.split(",")]
        result += is_possible(springs, sizes)

    end_time = time.time()
    print(f'Time to run Part 1 : {end_time - start_time}s')
    return result

def part2():
    start_time = time.time()
    result = 0
    input_map = []
    with open("input/12.txt") as f:
        input_map = [line.strip() for line in f]
    for line in input_map:
        springs, sizes = line.split(" ")
        sizes = [int(x) for x in sizes.split(",")]*5
        result += is_possible(springs, sizes)

    end_time = time.time()
    print(f'Time to run Part 2 : {end_time - start_time}s')
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())