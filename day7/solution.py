class Folders:
    def __init__(self, root):
        self.root = root
        self.folders = []
        self.cur_index = 0
        self.cur_folder = {0:root}

    def get_folders(self, index=None, name=None):
        if name is None and index is None:
            return self.folder
        elif name is not None and index is None:
            return [f for f in self.folders if f.name == name]
        elif name is None and index is not None:
            return [f for f in self.folders if f.index == index]
        else:
            return self.folders

    def add_folder(self, name, parent_index, index):
        if [f for f in self.folders if name == self.name and index == self.index] == []:
            folder = Folder(name=name, parent_index=parent_index, index=index)
            self.folders.append(folder)


class Folder:
    def __init__(self, name, parent_index, index):
        self.name = name
        self.parent_index = parent_index
        self.index = index
        self.files = []

    def add_file(self, file):
        self.files.append(file)


class File:
    def __init__(self, name, size: int):
        self.name = name
        self.size = size

    def get_file_name(self):
        return self.name


file = "day7/input.example"
ls = False
# load Folders
with open(file) as input:
    for line in input.readlines():
        folders = Folders()
        if line[0] == "$":
            if line[0:5] == "$ cd":
                if line[-2] == "''":
                    folders.cur_index -= 1
                else:
                    folders.cur_index += 1
                    foldername = line.split(" ")[-1]
                    folders.add_folder(
                        parent_index=folders.cur_index - 1,
                        name=foldername,
                        index=folders.cur_index,
                    )
            elif line == "$ ls":
                continue
        elif line[0:4] == dir:
                folders.cur_index += 1
                foldername = line.split(" ")[-1]
                folders.add_folder(
                    parent_index=folders.cur_index - 1,
                    name=foldername,
                    index=folders.cur_index,
                ) 
       else:
       

