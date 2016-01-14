__author__ = 'Nenad Todorovic'
__author__ = 'Dragan Vidakovic'

import os


def list_files_from_directory(directory):
    """Lists all file paths from given directory"""

    ret_val = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            ret_val.append(str(directory) + "/" + str(file))
    return ret_val


def read_file(path):
    """Reads all lines from file on given path"""

    f = open(path, "r")
    read = f.readlines()
    ret_val = []
    for line in read:
        if line.startswith("#"):
            pass
        else:
            ret_val.append(line)
    return ret_val


def process_line(line):
    """Returns sentence category and sentence in given line"""

    splits = line.split("\t")
    category = splits[0]
    sentence = splits[1]
    return category, sentence





