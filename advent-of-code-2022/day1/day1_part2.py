import heapq
f = open("/Users/kennethjohn/Personal Docs/advent-of-code/day1/input", "r")

# Variable to get the sum of top N
topN = 3
h = []

curr_cal = 0

# Read through the input file
for line in f.readlines():
    line = line.strip()
    if line == "":
        # Insert into the min heap if length is less than topN
        if len(h) < topN:
            heapq.heappush(h, curr_cal)
        # Push the sum into the heap and then take the min sum
        # Now the heap will be left with the topN sum at any point in time
        else:
            heapq.heappushpop(h, curr_cal)
        curr_cal = 0
        # Add the calories
    else:
        curr_cal += int(line)

heapq.heappushpop(h, curr_cal)

# Print out the sum of the heap
print(sum(h))

f.close()