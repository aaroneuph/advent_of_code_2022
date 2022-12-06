count = 0
file = "day4/input"
with open(file) as input:

    for line in input.readlines():
        line = line.replace("\n", "")
        p1 = line.split(",")[0].split("-")
        p2 = line.split(",")[1].split("-")
        p1r = set([r for r in range(int(p1[0]), int(p1[1]) + 1)])
        p2r = set([r for r in range(int(p2[0]), int(p2[1]) + 1)])
        if p2r.issuperset(p1r) or p1r.issuperset(p2r):
            count += 1
print(count)
