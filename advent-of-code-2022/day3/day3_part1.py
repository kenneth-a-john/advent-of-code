f = open("/Users/kennethjohn/Personal Docs/advent-of-code/advent-of-code-2022/day3/input", "r")

total_priority = 0
# Read through each lines of the file
for line in f.readlines():
    line = line.strip()
    length = len(line)
    compartment_1, compartment_2 = line[:length//2], line[length//2:]
    for letter in list(set(compartment_1)&set(compartment_2)):
        if letter.islower():
            total_priority += ord(letter) - ord('a') + 1
        else:
            total_priority += ord(letter) - ord('A') + 27

print(total_priority)