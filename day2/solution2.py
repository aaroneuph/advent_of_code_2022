dec = ["X", "Y", "Z"]
them = ["A", "B", "C"]
matrix = {1: {"win": 3, "lose": 2}, 2: {"win": 1, "lose": 3}, 3: {"win": 2, "lose": 1}}

file = "day2/input"
score = 0
with open(file) as input:
    for line in input:
        themi = line[0]
        dei = line[2]

        dshape = dec.index(dei) + 1
        tshape = them.index(themi) + 1

        # handle draw
        if dei == "Y":
            score += tshape
            score += 3
        # handle lose
        elif dei == "X":
            mshape = matrix[tshape]["win"]
            score += mshape
        # handle win
        elif dei == "Z":
            mshape = matrix[tshape]["lose"]
            score += mshape
            score += 6
            # rock beats scissors
print(score)
