def type_hand1(hands):
    hand = {}
    for card in hands:
        if card in hand:
            hand[card] += 1
        else:
            hand[card] = 1
    if 5 in hand.values():
        return 6
    elif 4 in hand.values():
        return 5
    elif 3 in hand.values():
        if 2 in hand.values():
            return 4
        else:
            return 3
    elif 2 in hand.values():
        if list(hand.values()).count(2) == 2:
            return 2
        else:
            return 1
    else:
        return 0
          
def part1():#part1
    hands = []
    ranked = [[] for _ in range(7)] 
    values = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
    rank = 1
    sum = 0
    with open("input/7.txt") as f:
        for i, x in enumerate(f):
            hands.append(x.split(" "))
            hands[i][1] = hands[i][1].strip()
            k = type_hand1(hands[i][0])
            ranked[k].append(hands[i])
        for i in range(7):
            ranked[i].sort(key=lambda x: [values[card] for card in x[0]])
            for x in ranked[i][::-1]:
                sum += int(x[1])*rank
                rank+=1     
    return sum
        
def type_hand2(hands):
    hand = {}
    max = 0
    best = 0
    for card in hands:
        if card in hand:
            hand[card] += 1
        else:
            hand[card] = 1
        if hand[card] > max and card != 'J':
            best = card
            max = hand[card]
    for card in hands:
        if card == 'J' and best != 0:
            hand[card] -= 1
            card = best
            hand[card] += 1
    if 5 in hand.values():
        return 6
    elif 4 in hand.values():
        return 5
    elif 3 in hand.values():
        if 2 in hand.values():
            return 4
        else:
            return 3
    elif 2 in hand.values():
        if list(hand.values()).count(2) == 2:
            return 2
        else:
            return 1
    else:
        return 0
     
def part2():#part2
    hands = []
    ranked = [[] for _ in range(7)] 
    values = {'A': 1, 'K': 2, 'Q': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12, 'J': 99}
    rank = 1
    sum = 0
    with open("input/7.txt") as f:
        for i, x in enumerate(f):
            hands.append(x.split(" "))
            hands[i][1] = hands[i][1].strip()
            k = type_hand2(hands[i][0])
            ranked[k].append(hands[i])
        for i in range(7):
            ranked[i].sort(key=lambda x: [values[card] for card in x[0]])
            for x in ranked[i][::-1]:
                sum += int(x[1])*rank
                rank+=1     
    return sum
            
    
if __name__ == "__main__":
    print(part1())
    print(part2())