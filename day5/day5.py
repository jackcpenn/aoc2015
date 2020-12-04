import re

with open("day5/input.txt") as file:
    strings = [line.strip() for line in file]

def part_1():
    def nice(string):
        string = list(string)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        naughty_substrings = {"ab", "cd", "pq", "xy"}
        twice = False
        vowels_count = 0

        for i in range(len(string)-1):
            if string[i] in vowels:
                vowels_count += 1
            
            if string[i] == string[i+1]:
                twice = True

            if "".join([string[i], string[i+1]]) in naughty_substrings:
                return False
        
        # check vowel on last char
        if string[-1] in vowels:
            vowels_count += 1

        return vowels_count >= 3 and twice == True
            

    count = 0    
    for string in strings:
        if nice(string):
            count += 1

    return count

def part_2():
    def nice(string):
        return bool(re.search(ABA, string)) and bool(re.search(DOUBLE_PAIR, string))

    DOUBLE_PAIR = re.compile(r"(..).*\1")
    ABA = re.compile(r"(.).\1")

    return sum(1 for string in strings if nice(string))



print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))