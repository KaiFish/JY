import csv
from person import Person
from treatment import Treatment
from enums import *

def data(filename):
    with open (filename, newline = '') as f:
        reader = csv.reader(f)
        stuff = []
        items = []
        name = ""
        data = []
        next(reader)
        next(reader)
        i = 3
        for row in reader:
            if row[17] == "Yes, I give my consent to be the subject of the research.":
                if row[6] == "True" or row[6] == "TRUE":
                    stuff = row[20:45]
                    name = row[100]
                    if name == "Retail Control Group":
                        items = row[45:51]
                    elif name == "Race Neutral Control Group":
                        items = row[51:65]
                    elif name == "Racial Resentment Treatment Group" or name == "Racial Resentment Treatment":
                        name = "Racial Resentment Treatment Group"
                        items = row[65:85]
                    elif name == "Linked Fate Treatment Group" or name == "Linked Fate Treatment":
                        name = "Linked Fate Treatment Group"
                        items = row[85:100]
                    #else:
                        #print(str(i) + " ERROR " + name + "\t" + row[6] + "\t" + row[17])
                    t = Treatment(name, items)
                    p = Person(stuff, t)
                    data.append(p)
            i += 1
    return data
