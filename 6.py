import string
def part1():
    fact = 1
    with open("input/6.txt") as f:
        dirty_time = next(f).split(":")[1].strip().split(" ")
        dirty_dist = next(f).split(":")[1].strip().split(" ")
        time = list(filter(None, dirty_time))
        dist = list(filter(None, dirty_dist))
        for i, x in enumerate(time):
            WR = 0
            for j in range(int(x)):
                if j*(int(x)-j) > int(dist[i]):
                    WR+=1
            fact*=WR
    return fact
    
def part2():
    t = ""
    d = ""
    WR = 0
    with open("input/6.txt") as f:
        dirty_time = next(f).split(":")[1].strip().split(" ")
        dirty_dist = next(f).split(":")[1].strip().split(" ")
        time = list(filter(None, dirty_time))
        dist = list(filter(None, dirty_dist))
        for i, x in enumerate(time):
            t += x
            d += dist[i]
        for j in range(int(t)):
            if j*(int(t)-j) > int(d):
                WR+=1
    return WR

if __name__ == "__main__":
    print(part1())
    print(part2())