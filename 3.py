def gear_test(i, j, x, lines):
    if i > 0 and j > 0:
        if lines[i-1][j-1].isdigit() :
            print(lines[i-1][j-1])
            #return lines[i-1][j-1] + if lines[i-1][j-2].isdigit()  add function number that returns the number
    if i > 0:
        if lines[i-1][j].isdigit() :
            print(lines[i-1][j])
    if i > 0 and j < len(x)-1:
        if lines[i-1][j+1].isdigit() :
            print(lines[i-1][j+1])
    if j > 0:
        if x[j-1].isdigit() :
            print(x[j-1])
    if j < len(x)-1:
        if x[j+1].isdigit() :
            print(x[j+1])
    if i < len(lines)-1 and j > 0:
        if lines[i+1][j-1].isdigit() :
            print(lines[i+1][j-1])
    if i < len(lines)-1:
        if lines[i+1][j].isdigit() :
            print(lines[i+1][j])
    if i < len(lines)-1 and j < len(x)-1:
        if lines[i+1][j+1].isdigit() :
            print(lines[i+1][j+1])        

def part1():#part1
    lines = []
    with open("input/3.txt") as f:
        for i, x in enumerate(f):
            lines.append(x.strip())
        for i, x in enumerate(lines):
            for j, y in enumerate(x):
                if y not in "0123456789.":
                    gear_test(i, j, x, lines)                    
    return 0
        
def part2():#part2
    with open("input/3.txt") as f:
        print("fill")    
    return 0

if __name__ == "__main__":
    print(part1())
    print(part2())