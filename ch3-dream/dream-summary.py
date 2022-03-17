import requests
import bs4
from nltk.tokenize import sent_tokenize
from sympy import bspline_basis
from gensim.summarization import summarize

url = "https://jamesclear.com/great-speeches/make-your-bed-by-admiral-william-h-mcraven"

page = requests.get(url)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, "html.parser")
p_elems = [element.text for element in soup.find_all("p")]

speech = "".join(p_elems)
