f = open("/Users/kennethjohn/Personal Docs/advent-of-code/advent-of-code-2022/day3/input", "r")

total_priority = 0
batch = []
prev_line = ""
# Read through each lines of the file
for line in f.readlines():
    line = line.strip()
    print(batch)
    if len(batch) != 3:
        batch.append(line)
    else:
        letter = list(set(batch[0]) & set(batch[1]) & set(batch[2]))
        print(letter)
        letter = letter[0]
        if letter.islower():
            total_priority += ord(letter) - ord('a') + 1
        else:
            total_priority += ord(letter) - ord('A') + 27
        batch = [line]

letter = list(set(batch[0]) & set(batch[1]) & set(batch[2]))
print(letter)
letter = letter[0]
if letter.islower():
    total_priority += ord(letter) - ord('a') + 1
else:
    total_priority += ord(letter) - ord('A') + 27
print(total_priority)
