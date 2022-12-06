file = "input"
sums = []
current_sum = 0
with open(file) as input:
    for line in input:
        if line == "\n":
            sums.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(float(line))

print(max(sums))
sums.sort(reverse=True)
print(sum(sums[0:3]))
