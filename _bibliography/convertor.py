import numpy as np

bibtex = open("papers.bib", "r")
file = bibtex.read()

papers = file.split("@")[1:]
resluts = np.zeros((len(papers), 4), dtype=object)

for i in range(len(papers)):
    tmp = papers[i].split("\n")
    for t in tmp:
        if "title=" in t:
            resluts[i, 0] = t[9:-2]
        if "author=" in t:
            resluts[i, 1] = t[10:-2]
        if "journal=" in t:
            resluts[i, 2] = t[11:-2]
        if "year=" in t:
            if "," in t:
                resluts[i, 3] = t[8:-2]
            else:
                resluts[i, 3] = t[8:-1]

resluts = resluts[resluts[:, 3][::-1].sort()][0]

res = ""

for result in resluts:
    for i in range(len(result)):
        if result[i] == 0:
            result[i] = ""
    res = res + "      - title: " + result[0]\
          + "\n        author: " + result[1]\
          + "\n        journal: " + result[2]\
          + "\n        year: " + str(result[3]) + "\n"

file = open('text', 'w')
file.write(res)
file.close()

