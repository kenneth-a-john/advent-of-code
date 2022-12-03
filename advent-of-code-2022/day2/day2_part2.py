f = open("/Users/kennethjohn/Personal Docs/advent-of-code/advent-of-code-2022/day2/input", "r")

# Rock      :   A 1
# Paper     :   B 2
# Scissors  :   C 3

# Lose  : X
# Draw  : Y
# Win   : Z

# For rock
map_A = {
    'X': 0 + 3,
    'Y': 3 + 1,
    'Z': 6 + 2
}
# For paper
map_B = {
    'X': 0 + 1,
    'Y': 3 + 2,
    'Z': 6 + 3
}
# For scissors
map_C = {
    'X': 0 + 2,
    'Y': 3 + 3,
    'Z': 6 + 1
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
    opponent, res = line.split(" ", 1)
    score += dict_[opponent][res]

print(score)