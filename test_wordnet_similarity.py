from automate import *

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

similar = 0.0;word_count = 0.0;flag=0
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
