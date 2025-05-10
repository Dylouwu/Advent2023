import time
import math
def part1():#part1
    st = time.time()
    node = []
    dest = []
    step = 0
    with open("input/8.txt") as f:
        lr = next(f).strip()
        next(f)
        for i, x in enumerate(f):
            x = x.replace('(', '').replace(')', '').replace(' ', '')
            node.append(x.split('=')[0].strip())
            dest.append(x.split('=')[1].strip().split(','))
        index = 0
        curr = node[index]
        while True:
            for x in lr:
                if curr == 'ZZZ': break
                elif x == 'L':
                    curr = dest[index][0]    
                else:
                    curr = dest[index][1]
                for i, y in enumerate(node):
                    if y == curr:
                        index = i
                        step += 1
            if curr == 'ZZZ': break
    et = time.time()
    print(f'Time to run Part 1 : {et-st}s')      
    return step
        

def part2():#part2
    st = time.time()
    node = []
    dest = []
    curr = []
    step = 0
    with open("input/8.txt") as f:
        lr = next(f).strip()
        next(f)
        for i, x in enumerate(f):
            x = x.replace('(', '').replace(')', '').replace(' ', '')
            node.append(x.split('=')[0].strip())
            dest.append(x.split('=')[1].strip().split(','))
            if node[i][2] == 'A':
                curr.append(node[i])
        cd = [0]*len(curr)
        while True:
            for x in lr:
                new_curr = []
                for i, curr2 in enumerate(curr):
                    if curr2[2] == 'Z' and cd[i] == 0:
                        cd[i] = step
                    if x == 'L':
                        new_curr.append(dest[node.index(curr2)][0])
                    else:
                        new_curr.append(dest[node.index(curr2)][1])
                if 0 not in cd: break
                step += 1
                curr = new_curr
            if 0 not in cd: break
    et = time.time()
    print(f'Time to run Part 2 : {et-st}s')                   
    return math.lcm(*cd)

if __name__ == "__main__":
    print(part1())
    print(part2()) 