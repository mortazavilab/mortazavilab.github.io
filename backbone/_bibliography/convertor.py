import numpy as np
import pandas as pd

bibtex = open("papers.bib", "r")
file = bibtex.read()

papers = file.split("@")[1:]
title = []
author = []
journal = []
year = []

for i in range(len(papers)):
    papers[i] = papers[i].replace(":", ";")
    tmp = papers[i].split("\n")
    for t in tmp:
        if "title=" in t and "booktitle" not in t:
            title.append(t[9:-2])
        if "author=" in t:
            author.append(t[10:-2])
        if "journal=" in t:
            journal.append(t[11:-2])
        if "year=" in t:
            if "," in t:
                year.append(int(t[8:-2]))
            else:
                year.append(int(t[8:-1]))

    if len(title) != len(author):
        author.append("")

    if len(title) != len(journal):
        journal.append("")

    if len(title) != len(year):
        year.append(0)

data = {'name': title, 'author': author, 'journal': journal, 'year': year}
results = pd.DataFrame(data)

results = results.sort_values(by=['year'], ascending=False).values

res = ""

for i in range(len(results)):
    res = res + "      - title: " + results[i, 0]\
          + "\n        author: " + results[i, 1]\
          + "\n        journal: " + results[i, 2]\
          + "\n        year: " + str(results[i, 3]) + "\n\n"

file = open('text', 'w')
file.write(res)
file.close()

