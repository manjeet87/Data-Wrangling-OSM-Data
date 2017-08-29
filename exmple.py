import csv

with open('nodes.csv', 'r', encoding='utf-8') as f:
    hndle = csv.reader(f)
    for r in  hndle:
        print(r)