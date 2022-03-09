from collections import Counter
from collections import Counter
import re
import requests
import bs4
import nltk
from nltk.corpus import stopwords


def main():
    url = "http://analytictect.com/mb021/mlk.html"
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    p_elems = [element.text for element in soup.find_all("p")]

    speech = "".join(p_elems)
