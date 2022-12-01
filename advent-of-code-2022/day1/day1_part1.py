f = open("/Users/kennethjohn/Personal Docs/advent-of-code/day1/input", "r")

# Initialize current and maximum calories to zero
max_cal = 0
curr_cal = 0

# Read through each lines of the file
for line in f.readlines():
    line = line.strip()
    # Update maximum calories by comparing it with current cal
    if line == "":
        max_cal = max(max_cal, curr_cal)
        curr_cal = 0
    # Add the calories
    else:
        curr_cal += int(line)

# Update the maximum for the last batch of input
max_cal = max(max_cal, curr_cal)

f.close()
print(max_cal)
