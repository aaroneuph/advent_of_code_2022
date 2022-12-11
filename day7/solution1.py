import re

# file = "day7/input.example"


class DirDict:
    def __init__(self, input_file):
        self.dirs = {"/": []}
        self.current_dir = "/"
        self.input_file = input_file
        self.root = "/"

    def add_dir(self, dir_to_add: str):
        dir_to_add = dir_to_add.replace("//", "/").replace("//", "/")
        if dir_to_add not in self.dirs.keys():
            self.dirs[dir_to_add] = []
        return dir_to_add

    def add_file(self, file):
        if file not in self.dirs[self.current_dir]:
            self.dirs[self.current_dir].append(file)

    def back_dir(self):
        last_slash_index = self.current_dir.rindex("/")
        if last_slash_index == 0:
            self.current_dir = "/"
        else:
            self.current_dir = self.current_dir[:last_slash_index]

    def get_files(self, directory: str):
        if directory in self.dirs.keys():
            return self.dirs[directory]

    def get_dir_size(self, directory: str, recursive=False) -> int:
        if directory in self.dirs.keys():
            total = 0
            if recursive:
                subdirs = [d for d in self.dirs.keys() if d.startswith(directory)]
                for subdir in subdirs:
                    total += self.get_dir_size(subdir)
            else:
                for file in self.get_files(directory):

                    total += int(file.split(" ")[0])
            return total

    def load_dir_dict(self):
        with open(self.input_file) as input:
            for line in input.readlines():
                line = line.replace("\n", "")
                if line[0:4] == "$ cd":
                    if line == "$ cd ..":
                        self.back_dir()
                    else:
                        dir_name_to_add = line.split(" ")[-1]
                        if self.current_dir == self.root:
                            dir_to_add = f"{self.root}{dir_name_to_add}"
                        else:
                            dir_to_add = f"{self.current_dir}/{dir_name_to_add}"

                        self.current_dir = self.add_dir(dir_to_add)
                elif "$ ls" in line:
                    continue
                elif line[0:3] == "dir":
                    dir_to_add = "{}/{}".format(self.current_dir, line.split(" ")[-1])
                    self.add_dir(dir_to_add)
                    continue
                elif re.search("^\d{1,}", line):  # does the line start with a number
                    self.add_file(line)
                    continue


file = "day7/input"
dir_dict = DirDict(input_file=file)
dir_dict.load_dir_dict()

# solution 1
total = 0
for d in dir_dict.dirs.keys():
    size = dir_dict.get_dir_size(d, recursive=True)
    if size <= 100000:
        total += size

print(total)

# solution 2
total_used_space = dir_dict.get_dir_size("/", recursive=True)
available_space = 70000000 - total_used_space
target = 30000000 - available_space
winner = None
for d in dir_dict.dirs.keys():
    size = dir_dict.get_dir_size(d, recursive=True)
    if winner is None:
        winner = size
    elif size >= target:
        if size < winner:
            winner = size
print(winner)
