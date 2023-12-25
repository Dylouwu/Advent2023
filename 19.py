import time
import re

def check_parts(entry, workflow, rating, next):
    output = int(rating[0].split('=')[1]) + int(rating[1].split('=')[1]) + int(rating[2].split('=')[1]) + int(rating[3].split('=')[1])
    if next == 'A':
        return output
    elif next == ' R':
        return 0
    for i, x in enumerate(entry):
        if x == next:
            for y in workflow[i]:
                if ':' in y:
                    letter = re.findall(r"[\w']+", y)
                    for char in rating:
                        if letter[0] in char:
                            if ('<' in y and int(letter[1]) > int(char.split('=')[1])) or ('>' in y and int(letter[1]) < int(char.split('=')[1])):
                                return check_parts(entry, workflow, rating, letter[2])
                elif y == 'A':
                    return output
                elif y == ' R':
                    return 0
                else:
                    return check_parts(entry, workflow, rating, y)
    return 0
                 
def part1():
    start_time = time.time()
    entry = []
    workflow = []
    ratings = []
    count = 0
    result = 0
    with open("input/19.txt") as f:
        for x in f:
            if x == '\n':
                count = 1
                continue
            if count == 0:    
                entry.append(x.split("{")[0].strip())
                workflow.append(x.split("{")[1].strip().strip('}').split(','))
            else:
                ratings.append(x.strip().strip('{}').split(','))
    print(ratings)
    for rating in ratings:         
        result += check_parts(entry, workflow, rating, 'in')
    end_time = time.time()
    print(f'Time to run Part 1 : {end_time - start_time}s')
    return result

def part2():
    start_time = time.time()
    entry = []
    workflow = []
    rating = [0]*4
    result = 0
    with open("input/19.txt") as f:
        for x in f:
            if x == '\n':
                break    
            entry.append(x.split("{")[0].strip())
            workflow.append(x.split("{")[1].strip().strip('}').split(','))
    for i in range(1, 4000):#This works but too long.
        print('o')
        rating[0] = f'x={i}'
        for j in range(1, 4000):
            rating[1] = f'x={j}'
            for k in range(1, 4000):
                rating[2] = f'x={k}'
                for l in range(1, 4000):
                    rating[3] = f'x={l}'
                    if check_parts(entry, workflow, rating, 'in') != 0:
                        result += 1
    end_time = time.time()
    print(f'Time to run Part 2 : {end_time - start_time}s')
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())