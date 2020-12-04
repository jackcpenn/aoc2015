import hashlib 

puzzle_input = "iwrupvqb"

i = 1
while True:
    secrey_key = puzzle_input + str(i)

    hash = hashlib.md5(secrey_key.encode())
    hash_hex = hash.hexdigest()

    if "".join(list(hash_hex)[:6]) == "000000": # part 2 just change to [:6] and add 0
        print(secrey_key, hash_hex)
        break
    i += 1
