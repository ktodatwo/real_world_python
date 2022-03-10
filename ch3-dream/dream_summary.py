from collections import Counter
from collections import Counter
import re
from prometheus_client import Summary
import requests
import bs4
import nltk
from nltk.corpus import stopwords


def main():
    url = "http://analytictect.com/mb021/mlk.html"
    page = requests.get(url)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    p_elems = [element.text for element in soup.find_all("p")]

    speech = "".join(p_elems)
    speech = speech.replace(")mowing", "knowing")
    speech = re.sub("\s+", " ", speech)
    speech_edit = re.sub("[^a-zA-Z]", " ", speech)
    speech_edit = re.sub("\s+", " ", speech_edit)

    while True:
        max_words = input("Enter max words per sentance for summary: ")
        num_sents = input("Enter number of sentances for summary: ")
        if max_words.isdigit() and num_sents.isdigit():
            break
        else:
            print("\nInput must be in whole numbers\n")

    speech_edit_no_stop = remove_stop_words(speech_edit)
    word_freq = get_word_freq(speech_edit_no_stop)
    sent_scores = score_sentences(speech, word_freq, max_words)

    counts = Counter(sent_scores)
    summary = counts.most_common(int(num_sents))
    print("\nSummary:")
    for i in summary:
        print(i[0])


def remove_stop_words(speech_edit):
    """Remove stop words from string and return string"""
    stop_words = set(stopwords.words("english"))
    speech_edit_no_stop = ""
    for word in nltk.word_tokenize(speech_edit):
        if word.lower() not in stop_words:
            speech_edit_no_stop += word + " "
    return speech_edit_no_stop
