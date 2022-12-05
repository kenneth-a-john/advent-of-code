f = open("/Users/kennethjohn/Personal Docs/advent-of-code/advent-of-code-2022/day4/input", "r")

count = 0

# Read through each lines of the file
for line in f.readlines():
    # 2-4,6-8
    line = line.strip()
    # 2-4     6-8
    range_1, range_2 = line.split(',')
    # 2 4     6 8
    range_1, range_2 = range_1.split('-'), range_2.split('-')
    # [2, 3, 4]  [6, 7, 8]
    range_1 = [*range(int(range_1[0]), int(range_1[1]) + 1)]
    range_2 = [*range(int(range_2[0]), int(range_2[1]) + 1)]
    if len(set(range_1).intersection(range_2)) > 0:
        count += 1

print(count)

