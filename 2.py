def part1():#part1
    sum = 0
    max_red = 12
    max_green = 13
    max_blue = 14
    number = ""
    with open("input/2.txt") as f:
        for line in f:
            id = 0
            red = 0
            green = 0
            blue = 0
            for i in range(len(line)):
                if line[i].isdigit() and id == 0:
                    id = line[i]
                    while line[i+1].isdigit():
                        i+=1
                        id += line[i]
                elif line[i].isdigit() and line[i+1] != ":":
                    number += line[i]
                    if line[i+2] == "r":
                        red += int(number)
                        number = ""
                    elif line[i+2] == "g":
                        green += int(number)
                        number = ""
                    elif line[i+2] == "b":
                        blue += int(number)
                        number = ""
                elif line[i] == ";" or line[i] == "\n" or line[i] == " ":
                    if red > max_red or green > max_green or blue > max_blue:
                        sum += int(id)
                        break
                    red, blue, green = 0, 0, 0

    return (5050 - sum)

def part2():#part2
    sum = 0
    number = ""
    max_red = 0
    max_green = 0
    max_blue = 0
    with open("input/2.txt") as f:
        for line in f:
            id = 0
            red = 0
            green = 0
            blue = 0
            for i in range(len(line)):
                if line[i].isdigit() and id == 0:
                    id = line[i]
                    while line[i+1].isdigit():
                        i+=1
                        id += line[i]
                elif line[i].isdigit() and line[i+1] != ":":
                    number += line[i]
                    if line[i+2] == "r":
                        red += int(number)
                        number = ""
                    elif line[i+2] == "g":
                        green += int(number)
                        number = ""
                    elif line[i+2] == "b":
                        blue += int(number)
                        number = ""  
                elif line[i] == ";" or line[i] == "\n" or line[i] == " ":
                    if red > max_red: max_red = red
                    if green > max_green: max_green = green
                    if blue > max_blue: max_blue = blue
                    red, blue, green = 0, 0, 0
            sum+=(max_red*max_green*max_blue)
            max_red, max_green, max_blue = 0, 0, 0 
              
    return sum

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()