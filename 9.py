import time

def compute1(x):
    count = 0
    for y in x :
        if y == 0:
            count+=1
    if count == len(x):
        return 0
    element = [x[i+1] - x[i] for i in range(len(x)-1)]
    return compute1(element) + x[-1]
            
def part1():#part1
    st = time.time()
    sum = 0
    with open("input/9.txt") as f:
        for i, x in enumerate(f):
            x = list(map(int, x.strip().split(' ')))
            sum += compute1(x)
    et = time.time()
    print(f'Time to run Part 1 : {et-st}s')      
    return sum

def compute2(x):
    count = 0
    for y in x :
        if y == 0:
            count+=1
    if count == len(x):
        return 0
    element = [x[i+1] - x[i] for i in range(len(x)-1)]
    return -compute2(element) + x[0]

def part2():#part2
    st = time.time()
    sum = 0
    with open("input/9.txt") as f:
        for i, x in enumerate(f):
            x = list(map(int, x.strip().split(' ')))
            sum += compute2(x)
    et = time.time()
    print(f'Time to run Part 2 : {et-st}s')      
    return sum

if __name__ == "__main__":
    print(part1())
    print(part2()) 