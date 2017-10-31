import Cosine_Similarity as similarity

sim = [0.1,0.2,0.6,0.5,0.9,0.4,0.2,0.004,0.002,0.121,0.112,0.43,0.9,0.67]
flag = 0
def diversion_check(threshold):
    start = end = 0
    final = []
    for i in range(len(sim)):
        if (sim[i] >= threshold):
            if flag == 0:
                start = i
                end = i
                flag = 1
            else:
                end+=1
        else:
            final.append((start,end))
            flag = 0
    return final

final = diversion_check(0.5)
print final
