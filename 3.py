#Making that many conditions is not the solution as it is tedious and making mistakes can happen very easily, however I dont know how to do it otherwise
def gear_test(i, j, x, lines):
    if i > 0 and j > 0:
        if lines[i-1][j-1].isdigit() :
            if lines[i-1][j-2].isdigit():
                if lines[i-1][j-3].isdigit():
                    return lines[i-1][j-3]*100 + lines[i-1][j-2]*10 + lines[i-1][j-1]
                elif lines[i-1][j].isdigit():
                    return lines[i-1][j-2]*100 + lines[i-1][j-1]*10 + lines[i-1][j]
            
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