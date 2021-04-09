import statistics as st
import csv
from person import Person
from treatment import Treatment
from enums import *
from read import *
from dataSet import DataSet

d = data('response1.csv')
d2 = data('response2.csv')
for p in d2:
    d.append(p)

ds = DataSet(d)

with open('data.csv', 'w', newline='') as f:
    write = csv.writer(f, delimiter = ',', quoting=csv.QUOTE_NONE, escapechar= '~')
    for x in ds:
        write.writerow(x)
