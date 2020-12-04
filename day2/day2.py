with open("day2/input.txt") as file:
    boxes = [line for line in file]

def part_1():   
    total = 0
    for box in boxes:
        l, w, h = box.split("x")

        side1, side2, side3 = int(l)*int(w), int(w)*int(h), int(h)*int(l)
        slack = min([side1, side2, side3])

        total += 2*(side1 + side2 +side3) + slack
    
    return total

def part_2():
    total = 0
    for box in boxes:
        l, w, h = box.split("x")
        l, w, h = int(l), int(w), int(h)
        dist_1 = 2*int(l) + 2*w
        dist_2 = 2*l + 2*h
        dist_3 = 2*w + 2*h

        wrap = min([dist_1, dist_2, dist_3])

        bow = l*w*h

        total += wrap + bow
    return total


print ("Part 1: " + str(part_1()))
print ("Part 2: " + str(part_2()))

    