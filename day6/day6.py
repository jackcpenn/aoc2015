with open("day6/input.txt") as file:
    ops = [line.split() for line in file]

def part_1():
    grid = [[False for i in range(1000)] for j in range(1000)]

    def do_instruction(instruction, top_left_x, top_left_y, bot_right_x, bot_right_y):
        for i in range(top_left_x, bot_right_x+1):
            for j in range(top_left_y, bot_right_y+1):
                if instruction == "toggle":
                    grid[i][j] = not grid[i][j]
                elif instruction == "on":
                    grid[i][j] = True
                else:
                    grid[i][j] = False
        
    for op in ops:
        instruction = op[-4]
        top_left_x, top_left_y = int(op[-3].split(',')[0]), int(op[-3].split(',')[1])
        bot_right_x, bot_right_y = int(op[-1].split(',')[0]), int(op[-1].split(',')[1])

        do_instruction(instruction, top_left_x, top_left_y, bot_right_x, bot_right_y)

    return sum([row.count(True) for row in grid])

def part_2():
    grid = [[0 for i in range(1000)] for j in range(1000)]

    def do_instruction(instruction, top_left_x, top_left_y, bot_right_x, bot_right_y):
        for i in range(top_left_x, bot_right_x+1):
            for j in range(top_left_y, bot_right_y+1):
                if instruction == "toggle":
                    grid[i][j] += 2
                elif instruction == "on":
                    grid[i][j] += 1
                elif instruction == "off" and grid[i][j] > 0:
                    grid[i][j] -= 1
        
    for op in ops:
        instruction = op[-4]
        top_left_x, top_left_y = int(op[-3].split(',')[0]), int(op[-3].split(',')[1])
        bot_right_x, bot_right_y = int(op[-1].split(',')[0]), int(op[-1].split(',')[1])

        do_instruction(instruction, top_left_x, top_left_y, bot_right_x, bot_right_y)

    return sum([sum(row) for row in grid])

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))