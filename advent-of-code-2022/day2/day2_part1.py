f = open("/Users/kennethjohn/Personal Docs/advent-of-code/advent-of-code-2022/day2/input", "r")

# Rock      :   A and X
# Paper     :   B and Y
# Scissors  :   C and Z

# For rock
map_A = {
    'X': 3 + 1,
    'Y': 6 + 2,
    'Z': 0 + 3
}
# For paper
map_B = {
    'X': 0 + 1,
    'Y': 3 + 2,
    'Z': 6 + 3
}
# For scissors
map_C = {
    'X': 6 + 1,
    'Y': 0 + 2,
    'Z': 3 + 3
}

dict_ = {
    'A': map_A,
    'B': map_B,
    'C': map_C
}

score = 0
# Read through each lines of the file
for line in f.readlines():
    line = line.strip()
    opponent, player = line.split(" ", 1)
    score += dict_[opponent][player]

print(score)