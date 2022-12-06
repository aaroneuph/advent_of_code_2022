al = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
file = "day3/input"
total = 0
count = 0
with open(file) as input:

    for line in input.readlines():
        if count == 3:
            count = 1
        else:
            count += 1

        if count == 1:
            list1 = set(line)
        elif count == 2:
            list2 = set(line)
        elif count == 3:
            list3 = set(line)

        if count == 3:
            same = [s for s in list1 if s in list2 and s in list3 and s != "\n"]
            print(list1, list2, list3, same)
            total += al.index(same[0]) + 1
print(total)
