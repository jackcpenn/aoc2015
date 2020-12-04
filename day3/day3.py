with open("day3/input.txt") as file:
    directions = [line.strip() for line in file.readline()]

def part_1():
    loc = (0, 0) # (horizontal, verticle)
    visited_houses = set() 

    visited_houses.add(loc)

    for d in directions:
        if d == '>':
            loc = (loc[0]+1, loc[1])
        elif d == '<':
            loc = (loc[0]-1, loc[1])
        elif d == '^':
            loc = (loc[0], loc[1]+1)
        else: # d == 'v'
            loc = (loc[0], loc[1]-1)
        

        if loc not in visited_houses:
            visited_houses.add(loc)
    
    return len(visited_houses)

def part_2():

    return -1


print("Part 1: " + part_1)
