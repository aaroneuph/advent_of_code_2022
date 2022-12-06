me = ["X", "Y", "Z"]
them = ["A", "B", "C"]

file = "day2/input"
score = 0
with open(file) as input:
    for line in input:
        themi = line[0]
        mei = line[2]

        mshape = me.index(mei) + 1
        tshape = them.index(themi) + 1

        # and my shape nmber to score
        score += mshape

        # add tie score
        if mshape == tshape:
            score += 3

        # rock beats scissors
        elif mshape == 1 and tshape == 3:
            score += 6

        elif mshape == 2 and tshape == 1:
            score += 6

        elif mshape == 3 and tshape == 2:
            score += 6
print(score)
