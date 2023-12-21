import time

def ascii(i, val):
    val += ord(i)
    val *= 17
    val %= 256
    return val
    
def part1():
    start_time = time.time()
    val = 0
    result = 0
    input_map = []
    with open("input/15.txt") as f:
        for x in f:
            input_map.append(x.strip())
    for i in input_map[0]:  
        if i != ',':
            val = ascii(i, val)
        else :
            result += val
            val = 0
    result += val
    end_time = time.time()
    print(f'Time to run Part 1 : {end_time - start_time}s')
    return result

def part2():
    start_time = time.time()
    result = 0
    key_hash = 0
    input_map = []
    hash_map = {}
    char = ''
    with open("input/15.txt") as f:
        for x in f:
            input_map.append(x.strip())
    i = 0 
    while i < len(input_map[0]):
        if input_map[0][i] not in '=-':
            char += input_map[0][i]
            key_hash = ascii(input_map[0][i], key_hash)
        elif input_map[0][i] == '=':
            i += 1
            if key_hash in hash_map:
                if char not in hash_map[key_hash]:
                    hash_map[key_hash] += f'[{char} {input_map[0][i]}] '
                else:
                    for j in range(1, 10):
                        hash_map[key_hash] = hash_map[key_hash].replace(f"[{char} {j}] ", f'[{char} {input_map[0][i]}] ')
            else:
                hash_map[key_hash] = f'[{char} {input_map[0][i]}] '
            i += 1 
            key_hash = 0
            char = ''
        else:
            i += 1
            for key, value in hash_map.items():
                if char in value:
                    for j in range(1, 10):
                        value = value.replace(f"[{char} {j}] ", '')
                        hash_map[key] = value
            char = ''
            key_hash = 0
        i += 1

    for key, value in hash_map.items():
        count = 1
        for i in value:
            if i.isdigit():
                result += int(i)*count*(key+1)
                count += 1
    end_time = time.time()
    print(f'Time to run Part 2 : {end_time - start_time}s')
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())