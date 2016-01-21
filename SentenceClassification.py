__author__ = 'Nenad Todorovic'
__author__ = 'Dragan Vidakovic'

import os
import gensim as gs

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
        sentence_array = sentence.split(" ")
        return category, sentence_array
    else:
        splits = line.split(" ")
        category = splits[0]
        sentence = line[len(category)+1:].lower()
        sentence_array = sentence.split(" ")
        return category, sentence_array


tr_folder = list_files_from_directory("training_set")
all_sentences = []
for file in tr_folder:
    lines = read_file(file)
    for line in lines:
        c, s = process_line(line)
        all_sentences.append(s)
#        print(s)

#print(len(all_sentences))

#model = gs.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
model = gs.models.Word2Vec()
model = gs.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
print(model.similarity('examine', 'examination'))
