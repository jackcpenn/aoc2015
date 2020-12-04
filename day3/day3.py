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

    robo_turn = False
    santa_loc = (0,0)
    robo_loc = (0,0)

    visited_houses = {(0,0)}

    for d in directions:

        if robo_turn:
            loc = robo_loc
        else:
            loc = santa_loc

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
        
        if robo_turn:
            robo_loc = loc
        else:
            santa_loc = loc
        
        robo_turn = not robo_turn
    
    return len(visited_houses)


print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))
