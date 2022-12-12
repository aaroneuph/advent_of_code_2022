class Forest:
    def __init__(self):
        self.cols = []
        self.rows = []

    def load(self, file):
        with open(file) as input:
            for li, line in enumerate(input.readlines()):
                self.rows.append(list(line.replace("\n", "")))
                for ri, v in enumerate(self.rows[li]):
                    if li == 0:
                        self.cols.append([])
                    self.cols[ri].append(v)

    def check_list_values_great_or_equal(self, list_values: list, value: int) -> bool:
        if list_values == []:
            return True
        else:
            for lv in list_values:
                if int(lv) >= value:
                    return False
        return True

    def get_visible_trees(self, list_values: list, value: int) -> list:
        result = []
        for lv in list_values:
            if lv >= value:
                result.append(lv)
                break
            else:
                result.append(lv)
        return result

    def get_coordinate_scenic_score(self, column_index: int, row_index: int):
        column = self.cols[column_index]
        row = self.rows[row_index]
        value = row[column_index]

        leftvis = self.get_visible_trees(reversed(row[:column_index]), value=value)
        rightvis = self.get_visible_trees(row[column_index + 1 :], value=value)
        upvis = self.get_visible_trees(reversed(column[:row_index]), value=value)
        downvis = self.get_visible_trees(column[row_index + 1 :], value=value)

        return len(leftvis) * len(rightvis) * len(upvis) * len(downvis)

    def get_most_scenic_tree(self):
        winner = 0
        for ri, row in enumerate(self.rows):
            for ci, col in enumerate(self.cols):
                score = self.get_coordinate_scenic_score(int(ci), int(ri))
                if score > winner:
                    winner = score
        return winner, ri, ci

    def check_height(self) -> int:
        total = 0
        coordinates = []
        for ri, row in enumerate(self.rows):
            if ri == 0 or ri == len(row) - 1:
                total += len(row)
                coordinates.append([ri, row, True])
                continue
            for colnum, rv in enumerate(row):
                if colnum == 0 or colnum == len(row) - 1:
                    total += 1
                    coordinates.append([colnum, ri, rv, True])
                    continue
                # for the row value check numbers to the left, right, up, down.
                # if all are smaller, continue

                numleft = row[: int(colnum)]
                if self.check_list_values_great_or_equal(numleft, int(rv)):
                    total += 1
                    coordinates.append([colnum, ri, rv, True])
                    continue

                numright = row[int(colnum) + 1 :]
                if self.check_list_values_great_or_equal(numright, int(rv)):
                    total += 1
                    coordinates.append([colnum, ri, rv, True])
                    continue
                colvalues = self.cols[colnum]

                numup = colvalues[: int(ri)]
                if self.check_list_values_great_or_equal(numup, int(rv)):
                    total += 1
                    coordinates.append([colnum, ri, rv, True])
                    continue

                numdown = colvalues[int(ri) + 1 :]
                if self.check_list_values_great_or_equal(numdown, int(rv)):
                    total += 1
                    coordinates.append([colnum, ri, rv, True])
                    continue

        return total  # , coordinates


frst = Forest()
frst.load("day8/input")

# solution 1
print(frst.check_height())

# solution 2
print(frst.get_most_scenic_tree())
