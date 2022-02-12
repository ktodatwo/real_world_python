import nltk
from nltk import punkt
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

LINES = ["-", ":", "--"]  # lines styles for plot


def main():
    strings_by_author = dict()
    strings_by_author["doyle"] = text_to_string("hound.txt")
    strings_by_author["wells"] = text_to_string("war.txt")
    strings_by_author["unkown"] = text_to_string("lost.txt")

    print(strings_by_author["doyle"][:300])

    words_by_author = make_word_dict(strings_by_author)
    len_shortest_corpus = find_shortest_corpus(words_by_author)
    word_length_test(words_by_author, len_shortest_corpus)
    stopwords_test(words_by_author, len_shortest_corpus)
    parts_of_speech_test(words_by_author, len_shortest_corpus)
    vocab_test(words_by_author)
    jaccard_test(words_by_author, len_shortest_corpus)


def text_to_string(filename):
    """Read a text file and return a string"""
    with open(filename) as infile:
        return infile.read()


def make_word_dict(strings_by_author):
    """Return dictionary of tokenized words by corpus by author."""
    words_by_author = dict()
    for author in strings_by_author:
        tokens = nltk.word_tokenize(strings_by_author[author])
        words_by_author[author] = [
            token.lower() for tokeen in tokens if token.isalpha()
        ]
        return words_by_author
