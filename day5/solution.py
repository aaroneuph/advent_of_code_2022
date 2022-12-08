count = 0
file = "day5/input"
moves = []
columns = {}
columnlines = []
with open(file) as input:
    for line in input.readlines():

        if "move" not in line and line != "\n":
            columnlines.append(line.replace("\n", ""))

        if "move" in line:
            moves.append(line.replace("\n", ""))

# for every column line split every 4 characters and save that as a column value
for columnline in columnlines[:-1]:
    rowstartposition = 0
    for columnnum in columnlines[-1].replace(" ", ""):
        if columnnum not in columns.keys():
            columns[columnnum] = []
        columnvalue = (
            columnline[rowstartposition : rowstartposition + 4]
            .replace(" ", "")
            .replace("[", "")
            .replace("]", "")
        )
        if columnvalue != "":
            columns[columnnum].append(columnvalue)
        rowstartposition += 4

# process move directions
for moveline in moves:
    mlinesplit = moveline.split(" ")
    num = mlinesplit[1]
    fromcol = mlinesplit[3]
    tocol = mlinesplit[5]
    # interate number of times in move instruction, inserting from column to column
    for i in range(0, int(num)):
        columns[tocol].insert(
            0, columns[fromcol].pop(0)
        )  # insert from beginning of list to beginning of list

# collect list as a string comprise of the first index of each list of column values
result = ""
for c in columns.keys():
    result += columns[c][0]
print(result)
