left:   list[int]   = []
right:  list[int]   = []
score:  int         = 0

with open("input.txt", "r") as input_file:
    for line in input_file:
        left_value, d, right_value = line.strip().partition("   ")
        
        left.append(int(left_value))
        right.append(int(right_value))

left = list(set(left))

for i in range(len(left)):
    score += int(left[i] * right.count(left[i]))

print(score)