import re
import numpy as np
import pandas as pd
import nltk
import pymorphy2
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from razdel import tokenize
df = pd.read_csv('articles.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
stopword_ru = stopwords.words('russian')
print(len(stopword_ru))
morph = pymorphy2.MorphAnalyzer()
with open('stopwords.txt') as f:
    additional_stopwords = [w.strip() for w in f.readlines() if w]
    stopword_ru += additional_stopwords
    len(stopword_ru)

def clean_text(text):
    if not isinstance(text, str):
        text = str(text)
    text = text.lower()
    text = text.strip('\\n').strip('\\r').strip('\\t')

