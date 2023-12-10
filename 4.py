def part1():#part1
    sum = 0
    count = 0
    with open("input/4.txt") as f: 
        for line in f:       
            given = line.split("|")[0].strip().split(" ")
            won = line.split("|")[1].strip().strip("\n").split(" ")
            for i in given:
                if i in won and i != '' and count>=1:
                    count*=2
                elif i in won and i != '':
                    count = 1
            sum += count
            count = 0
    return sum
                    
def part2():#part2                
    sum = 1
    count = [1] * 209
    with open("input/4.txt") as f: 
        for k, line in enumerate(f):
            while count[k] > 0:     
                j = k
                given = line.split("|")[0].strip().split(" ")
                won = line.split("|")[1].strip().strip("\n").split(" ")
                for i in given:
                    if i in won and i != '' and j < 208:
                        count[j+1] += 1
                        j+=1
                count[k] -= 1
            if k < 208 :
                sum += count[k+1]
    return sum
    
def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()