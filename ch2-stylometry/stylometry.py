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
