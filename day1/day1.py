with open('day1/input.txt') as file:
    text = list(file.readline())

def part_1():
    floor = 0
    for t in text:
        if t =='(':
            floor += 1
        else:
            floor -= 1
    return floor

def part_2():
    floor = 0
    for i in range(len(text)):
        print(i)
        if text[i] =='(':
            floor += 1
        elif floor == 0:
            return i+1
        else:
            floor -= 1

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))
