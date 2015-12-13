University of Novi Sad
Faculty of Technical Science

Soft Computing 2015/2016 ( https://github.com/ftn-ai-lab )

Nenad Todorović RA 78/2012
Dragan Vidaković RA 134/2012

# Semantic Classification of Sentences

Automatically assigning input sentences to a set of categories. Sentence assigning process is based on it's semantic. Categories are defined with the indicator words.

# Data

"Sentence Classification Data Set" downloaded from Machine Learning Repository of Center for Machine Learning and Intelligent Systems - University of California, Irvine ( http://cml.ics.uci.edu/ ).
Data Set contains data for  classification of sentences in scientific articles into categories:
  1. AIMX - The specific research goal of the paper
  2. OWNX - The author's own work (methods, results, conclusions...)
  3. CONT - Contrast, comparasion or critique of past work
  4. BASE - Past work that provides the basis for the work in the article
  5. MISC - Any other sentences.

Data Set contains sentences from the abstract and introduction of 90 scientific article from three different domains:
  1. PLoS Computational Biology (PLOS)
  2. The Machine Learning repository on arXiv (ARXIV)
  3. The rsychology journal Judgment and Decision Making (JDM).

# Directories

1. "training_set"
  - 24 PLOS articles with 893 sentences
  - 24 ARXIV articles with 793 sentences
  - 24 JDM articles with 814 sentences

2. "test_set"
  - 6 PLOS articles with 220 sentences
  - 6 ARXIV articles with 197 sentences
  - 6 JDM articles with 200 sentences

3. "word_lists"
  This directory contains one plaintext file for each of the 4 categories AIMX, OWNX, CONT and BASE. Each plaintext file lists the indicator words for the corresponding category. This directory also contains a stopwords file. The stopwords file contains stopwords that are not likely to be important for the taske of sentence classification (how, show, our...). File contains a set of stopwords that are not likely to be strong features for this task and thus can be safely removed.
