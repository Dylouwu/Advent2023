import time
import sys
sys.setrecursionlimit(100000)
def travel(input_map, point, count, direction, start):
    if count > 0 and start == point :
        return count/2
    count+=1
    match input_map[point[0]][point[1]]:
        case '|':
            if direction == 'N':
                return travel(input_map, (point[0] - 1, point[1]), count, direction, start)
            return travel(input_map, (point[0] + 1, point[1]), count, direction, start)
        case '-':
            if direction == 'W':
                return travel(input_map, (point[0], point[1] - 1), count, direction, start)
            return travel(input_map, (point[0], point[1] + 1), count, direction, start)
        case 'L':
            if direction == 'S':
                return travel(input_map, (point[0], point[1] + 1), count, 'E', start)
            return travel(input_map, (point[0] - 1, point[1]), count, 'N', start)                 
        case 'J':
            if direction == 'S':
                return travel(input_map, (point[0], point[1] - 1), count, 'W', start)
            return travel(input_map, (point[0] - 1, point[1]), count, 'N', start)
        case '7':
            if direction == 'N':
                return travel(input_map, (point[0], point[1] - 1), count, 'W', start)
            return travel(input_map, (point[0] + 1, point[1]), count, 'S', start)
        case 'F':
            if direction == 'N':
                return travel(input_map, (point[0], point[1] + 1), count, 'E', start)
            return travel(input_map, (point[0] + 1, point[1]), count, 'S', start)
            
    
def part1():#part1
    st = time.time()
    total = 0
    input_map = []
    with open("input/10.txt") as f:
        for i, x in enumerate(f):
            input_map.append(x.strip())
        for i, x in enumerate(input_map):
            for j, y in enumerate(x):
                if y == 'S':
                    input_map[i] = input_map[i][:j] + '7' + input_map[i][j+1:]
                    start = (i,j)
                    print(start)
        total = travel(input_map, start, 0, 'N', start)
        
    et = time.time()
    print(f'Time to run Part 1 : {et-st}s')      
    return total

def part2():#part2
    st = time.time()
    sum = None
    #with open("input/10.txt") as f:
        
    et = time.time()
    print(f'Time to run Part 2 : {et-st}s')      
    return sum

if __name__ == "__main__":
    print(part1())
    print(part2()) 