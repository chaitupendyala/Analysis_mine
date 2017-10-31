from automate import *
from datasketch import MinHash, MinHashLSH

url1 = raw_input("Enter the first URL:")
url2 = raw_input("Enter the second URL:")
text1='';text2='';text1_main='';text2_main=''
text1 = main_text(url1)
text2 = main_text(url2)
word_count = 0;similar = 0
#text1_main = text1 + ' '
#text2_main = text2 + ' '
text1_split = text1.split(' ');text2_split = text2.split(' ')

text1_split = [x.upper() for x in text1_split if x]
text1_split = [x for x in text1_split if len(x) > 1]

text2_split = [x.upper() for x in text2_split if x]
text2_split = [x for x in text2_split if len(x) > 1]

text1_main = []
for i in text1_split:
    synonyms = wordnet.synsets(i)
    synonyms = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    text1_main.append(i)
    for k in synonyms:
        text1_main.append(k)

text2_main = []
for i in text2_split:
    synonyms = wordnet.synsets(i)
    synonyms = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    text2_main.append(i)
    for k in synonyms:
        text2_main.append(k)

set1 = set(text1_main)
set2 = set(text2_main)

m1 = MinHash(num_perm=100)
m2 = MinHash(num_perm=100)

for d in set1:
    m1.update(d.encode('utf8'))
for d in set2:
    m2.update(d.encode('utf8'))

print m2.jaccard(m1)
