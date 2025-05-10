def part1():#part1
    sum = 0

    with open("input/1.txt") as f:
        for line in f:
            digit1 = 0
            for ch in line: 
                if ch.isdigit():
                    digit2=ch
                    if digit1 == 0:
                        digit1=ch
                
            sum += int(digit1 + digit2)  
    return sum
    

def part2():#part2
    sum = 0
    with open("input/1.txt") as f:
        for line in f:
            digit1 = 0
            digit2 = 0
            for i in range(len(line)):
                if line[i].isdigit():
                    digit2=line[i]
                elif line[i] == "o" and line[i+1] == "n" and line[i+2] == "e":
                    digit2="1"
                    i += 2
                elif line[i] == "t" and line[i+1] == "w" and line[i+2] == "o":
                    digit2="2"
                    i += 2
                elif line[i] == "t" and line[i+1] == "h" and line[i+2] == "r" and line[i+3] == "e" and line[i+4] == "e":
                    digit2="3"
                    i += 4
                elif line[i] == "f" and line[i+1] == "o" and line[i+2] == "u" and line[i+3] == "r":
                    digit2="4"
                    i += 3
                elif line[i] == "f" and line[i+1] == "i" and line[i+2] == "v" and line[i+3] == "e":
                    digit2="5"
                    i += 3
                elif line[i] == "s" and line[i+1] == "i" and line[i+2] == "x":
                    digit2="6"
                    i += 2
                elif line[i] == "s" and line[i+1] == "e" and line[i+2] == "v" and line[i+3] == "e" and line[i+4] == "n":
                    digit2="7"
                    i += 4
                elif line[i] == "e" and line[i+1] == "i" and line[i+2] == "g" and line[i+3] == "h" and line[i+4] == "t":
                    digit2="8"
                    i += 4
                elif line[i] == "n" and line[i+1] == "i" and line[i+2] == "n" and line[i+3] == "e":
                    digit2="9"
                    i += 3
                if digit1 == 0:
                    digit1=digit2
            sum += int(digit1 + digit2)
    return sum
    
def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()