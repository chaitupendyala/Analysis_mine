from automate import main_text
from datasketch import MinHash, MinHashLSH
from nltk.corpus import wordnet
from itertools import chain

f = open("urls_for_clustering.txt","r")
urls = [x for x in f.read().split('\n')]
text_in_all_urls = []
temp_text = ''
set_for_url = None
m = MinHash(num_perm=100)
lsh = MinHashLSH(threshold=0.5, num_perm=100)

for url in urls[:len(urls)-1:]:
    temp_text = ''
    set_for_url = None
    temp_text = main_text(url)
    temp_text = temp_text.split(' ')
    temp_text = [x.lower() for x in temp_text if x]
    temp_text = [x for x in temp_text if (len(x) > 1)]
    temp_text_main = []
    for i in temp_text:
        synonyms = wordnet.synsets(i)
        synonyms = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
        temp_text_main.append(i)
        for k in synonyms:
            temp_text_main.append(k)
    set_for_url = set(temp_text_main)
    for d in set_for_url:
        m.update(d.encode('utf8'))
    lsh.insert(url,m)
    print lsh.query(m)
    print
