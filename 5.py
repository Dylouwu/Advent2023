def part1():
    with open("input/5.txt") as f:
        seeds = list(map(int, next(f).split(":")[1].strip().split(" ")))
        next(f)
        dest = []
        source = []
        reach = []
        for i in range(7):
            next(f)
            maps = []
            for line in f:
                if line == "\n":
                    break
                maps += line.strip().split(" \n")
            dest.append([int(m.split(" ")[0]) for m in maps])  # Convert to int here
            source.append([int(m.split(" ")[1]) for m in maps])
            reach.append([int(m.split(" ")[2]) for m in maps]) 
        for i in range(len(seeds)):
            for j in range(7):
                for k in range(len(dest[j])):
                    if seeds[i] >= source[j][k] and seeds[i] < source[j][k] + reach[j][k]:
                        seeds[i] += dest[j][k] - source[j][k]
                        break
        
    return min(seeds)

def part2():
    with open("input/5.txt") as f:
        seed = list(map(int, next(f).split(":")[1].strip().split(" ")))
        seeds = []
        mini = 0
        next(f)
        dest = []
        source = []
        reach = []
        for i in range(7):
            next(f)
            maps = []
            for line in f:
                if line == "\n":
                    break
                maps += line.strip().split(" \n")
            dest.append([int(m.split(" ")[0]) for m in maps])
            source.append([int(m.split(" ")[1]) for m in maps])
            reach.append([int(m.split(" ")[2]) for m in maps]) 
        for i in range(0, len(seed)-1, 2):
            for j in range(seed[i+1]):
                seeds = seed[i]+j
                for k in range(7):
                    for m in range(len(dest[k])):
                        if seeds >= source[k][m] and seeds < source[k][m] + reach[k][m]:
                            seeds += dest[k][m] - source[k][m]
                            break
                if mini == 0:
                    mini = seeds
                else:
                    mini = min(mini, seeds)
        
    return mini

def main():
    print(part1())
    print(part2())
    
if __name__ == "__main__":
    main()
    
