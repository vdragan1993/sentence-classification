__author__ = 'Nenad Todorovic'
__author__ = 'Dragan Vidakovic'

import os
import json
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import DecisionTreeClassifier
import time


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
        s_category = splits[0]
        sentence = splits[1].lower()
        return s_category, sentence
    else:
        splits = line.split(" ")
        s_category = splits[0]
        sentence = line[len(s_category)+1:].lower()
        return s_category, sentence


def create_json_file(input_folder, destination_file):
    tr_folder = list_files_from_directory(input_folder)
    all_json = []
    for file in tr_folder:
        lines = read_file(file)
        for line in lines:
            c, s = process_line(line)
            if s.endswith('\n'):
                s = s[:-1]
            json_data = {
                'text': s,
                'label': c
            }
            all_json.append(json_data)

    with open(destination_file, "w") as outfile:
        json.dump(all_json, outfile)


def prepare_test_data(input_folder):
    test_folder = list_files_from_directory(input_folder)
    t_sentences = []
    t_categories = []
    for file in test_folder:
        lines = read_file(file)
        for line in lines:
            c, s = process_line(line)
            if s.endswith('\n'):
                s = s[:-1]
            t_sentences.append(s)
            t_categories.append(c)
    return t_categories, t_sentences

# main
# prepare training and test data
create_json_file("training_set", "training.json")
categories, sentences = prepare_test_data("test_set")
# Bayes Classifier
print("Training Naive Bayes Classifier...")
start_nbc = time.time()
with open('training.json', 'r') as training:
    nbc = NaiveBayesClassifier(training, format="json")
stop_nbc = time.time()
print("Training Naive Bayes Classifier completed...")
elapsed = stop_nbc - start_nbc
print("Training time (in seconds): " + str(elapsed))
print("Testing Naive Bayes Classifier...")
correct = 0
start_nbc = time.time()
for i in range(0, len(sentences)):
    category = str(nbc.classify(sentences[i])).lower()
    expected = str(categories[i]).lower()
    if category == expected:
        correct += 1
stop_nbc = time.time()
elapsed = stop_nbc - start_nbc
print("Number of tests: " + str(len(sentences)))
print("Correct tests: " + str(correct))
accuracy = correct / len(sentences)
print("Naive Bayes Classifier accuracy: " + str(accuracy))
print("Testing time (in seconds): " + str(elapsed))

print()
# Decision Tree Classifier
print("Training Decision Tree Classifier...")
start_dtc = time.time()
with open('training.json', 'r') as training:
    dtc = DecisionTreeClassifier(training, format="json")
stop_dtc = time.time()
print("Training Decision Tree Classifier completed...")
elapsed = stop_dtc - start_dtc
print("Training time (in seconds): " + str(elapsed))
print("Testing Decision Tree Classifier...")
correct = 0
start_dtc = time.time()
for i in range(0, len(sentences)):
    category = str(dtc.classify(sentences[i])).lower()
    expected = str(categories[i]).lower()
    if category == expected:
        correct += 1
stop_dtc = time.time()
elapsed = stop_dtc - start_dtc
print("Number of tests: " + str(len(sentences)))
print("Correct tests: " + str(correct))
accuracy = correct / len(sentences)
print("Decision Tree Classifier accuracy: " + str(accuracy))
print("Testing time (in seconds): " + str(elapsed))