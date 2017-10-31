import urllib
from bs4 import BeautifulSoup
import csv
import urllib2
import re
import string
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import wordnet
from itertools import chain
from nltk.corpus import stopwords
from DatumBox import DatumBox
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
datum_box = DatumBox("2a13913dda346761765020c1f66e34f8")
TAG_RE = re.compile(r"<[^>]+>")
nltk.download('punkt')
stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
cachedStopWords = stopwords.words("english")

def remove_tags(text):
    return TAG_RE.sub('', text)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def main_text(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text = ' '.join([word for word in text.split() if word not in cachedStopWords])
    for char in text:
        if(not((ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90))):
            text = text.replace (char," ")
    return text

def openfile(f):
    x = []
    y = []
    finial = []; i=2
    csvfile = open(f,'rb')
    reader = csv.DictReader(csvfile)
    similar = 0.0;word_count = 0.0;flag=0
    text1='';text2='';text1_main='';text2_main=''
    text1_split = []
    text2_split = []
    synonyms=None
    word_count = 0;similar = 0
    for row in reader:
        synonyms=None
        if i==0:
            for j in text1_split:
                flag = 0
                if j not in text2_split:
                    synonyms = wordnet.synsets(j)
                    synonyms = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
                    for k in synonyms:
                        if k in text2_split:
                            flag = 1
                else:
                    similar += 1
                if flag == 1:
                    similar += 1
                word_count += 1

            for j in text2_split:
                flag = 0
                if j not in text1_split:
                    synonyms = wordnet.synsets(j)
                    synonyms = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
                    for k in synonyms:
                        if k in text1_split:
                            flag = 1
                else:
                    similar += 1
                if flag == 1:
                    similar += 1
                word_count += 1
            print similar/word_count
            i=2
            word_count = 0;similar = 0
            similar = 0.0;word_count = 0.0;flag=0
            text1='';text1_main=''
            text2='';text2_main=''
        elif i==1:
            text1 = main_text(row['url'])
            text1_split = text1.split(' ')
            text1_split = [x.upper() for x in text1_split if x]
        elif i==2:
            text2 = main_text(row['url'])
            text2_split = text2.split(' ')
            text2_split = [x.upper() for x in text2_split if x]
    print a
    csvfile.close()

#openfile('/home/chaitanya/Documents/Codes/IR_Vidhya mam/resources/input/10.csv')
