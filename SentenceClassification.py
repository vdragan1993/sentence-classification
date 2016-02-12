__author__ = 'Nenad Todorovic'
__author__ = 'Dragan Vidakovic'

import os
import json


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

    if "\t" in line:
        splits = line.split("\t")
        category = splits[0]
        sentence = splits[1].lower()
        return category, sentence
    else:
        splits = line.split(" ")
        category = splits[0]
        sentence = line[len(category)+1:].lower()
        return category, sentence


tr_folder = list_files_from_directory("training_set")
all_json = []
for file in tr_folder:
    lines = read_file(file)
    for line in lines:
        c, s = process_line(line)
        json_data = {
            'text': s,
            'label': c
        }

        all_json.append(json_data)

with open("jsonFile.txt", "w") as outfile:
    json.dump(all_json, outfile)
