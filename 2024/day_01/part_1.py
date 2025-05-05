left:   list[int]   = []
right:  list[int]   = []
total:  int         = 0

with open("input.txt", "r") as input_file:
    for line in input_file:
        left_value, d, right_value = line.strip().partition("   ")
        
        left.append(int(left_value))
        right.append(int(right_value))

left.sort()
right.sort()

for i in range(len(left)):
    total += abs(right[i] - left[i])

print(total)