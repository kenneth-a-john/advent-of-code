# Crates input
#     [C]         [Q]         [V]    
#     [D]         [D] [S]     [M] [Z]
#     [G]     [P] [W] [M]     [C] [G]
#     [F]     [Z] [C] [D] [P] [S] [W]
# [P] [L]     [C] [V] [W] [W] [H] [L]
# [G] [B] [V] [R] [L] [N] [G] [P] [F]
# [R] [T] [S] [S] [S] [T] [D] [L] [P]
# [N] [J] [M] [L] [P] [C] [H] [Z] [R]
#  1   2   3   4   5   6   7   8   9 

# Creating the input
stack_1 = ["N", "R", "G", "P"]
stack_2 = ["J", "T", "B", "L", "F", "G", "D", "C"]
stack_3 = ["M", "S", "V"]
stack_4 = ["L", "S", "R", "C", "Z", "P"]
stack_5 = ["P", "S", "L", "V", "C", "W", "D", "Q"]
stack_6 = ["C", "T", "N", "W", "D", "M", "S"]
stack_7 = ["H", "D", "G", "W", "P"]
stack_8 = ["Z", "L", "P", "H", "S", "C", "M", "V"]
stack_9 = ["R", "P", "F", "L", "W", "G", "Z"]

# Adding to dict for easy access
stack_dict = {
    "1": stack_1,
    "2": stack_2,
    "3": stack_3,
    "4": stack_4,
    "5": stack_5,
    "6": stack_6,
    "7": stack_7,
    "8": stack_8,
    "9": stack_9
}

# input now has the operations only and not the initial crate positions
f = open("/Users/kennethjohn/Personal Docs/advent-of-code/advent-of-code-2022/day5/input.txt", "r")

# Read through each lines of the file
for line in f.readlines():
    count, stacks = line.split("from", 1)
    # Strip move and convert to int
    count = int(count.lstrip("move").strip())
    # Split on 'to', to get intial and final crate position
    from_stack, to_stack = stacks.split("to")
    from_stack = from_stack.lstrip("from")
    from_stack, to_stack = from_stack.strip(), to_stack.strip()

    while(count):
        crate = stack_dict[from_stack].pop()
        stack_dict[to_stack].append(crate)
        count -= 1

res = ""

for i in range(len(stack_dict)):
    res += stack_dict[str(i+1)][-1]

print(res)


