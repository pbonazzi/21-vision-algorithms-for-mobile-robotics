from os import walk


def all_files(path):
    names = []
    for files in walk(path):
        names.append(files)
    return names[0][2]
