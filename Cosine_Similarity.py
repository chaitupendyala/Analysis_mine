import text_extract as te
import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def find_cos_sim(url1,url2):

    text1 = te.text_extract(url1)
    text2 = te.text_extract(url2)

    from nltk.corpus import stopwords

    cachedStopWords = stopwords.words("english")
    text1= ' '.join([word for word in text1.split() if word not in stopwords.words("english")])
    text2= ' '.join([word for word in text2.split() if word not in stopwords.words("english")])


    from nltk import PorterStemmer
    text1 = PorterStemmer().stem(text1)
    text2 = PorterStemmer().stem(text2)

    text1_vec = text1.split(' ')
    text2_vec = text2.split(' ')

    for i in range(0,len(text1_vec)):
        text1_vec[i] = PorterStemmer().stem(text1_vec[i])

    for i in range(0,len(text2_vec)):
        text2_vec[i] = PorterStemmer().stem(text2_vec[i])


    text1_str = ""
    text2_str = ""

    for i in text1_vec:
        text1_str = text1_str + " " + i

    for i in text2_vec:
        text2_str = text2_str + " " + i

    vector1 = text_to_vector(text1_str)
    vector2 = text_to_vector(text2_str)

    cosine = get_cosine(vector1, vector2)

    return cosine
    
print find_cos_sim("http://www.omgubuntu.co.uk/2016/05/install-gnome-3-20-ubuntu-16-04-lts","http://www.omgubuntu.co.uk/2016/05/install-gnome-3-20-ubuntu-16-04-lts")
