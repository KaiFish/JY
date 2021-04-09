import statistics as st
import csv
from person import Person
from treatment import Treatment
from enums import *
from read import *
from stats import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def plot(title, yLabel, xLabel, labels, data1, label1, data2, label2):
    x = np.arange(len(labels))
    width = 0.3
    fig, ax = plt.subplots()
    rect1 = ax.bar(x-width/2, data1, width, label=label1)
    rect2 = ax.bar(x+width/2, data2, width, label=label2)

    ax.set_ylabel(yLabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_xlabel(xLabel)

    ax.bar_label(rect1, padding=3)
    ax.bar_label(rect2, padding=3)
    ax.legend()
    fig.tight_layout()

def rrCount(d):
    rr = []
    for p in d:
        rr.append(p.getRR())
    a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in rr:
        if x == -10:
            a[0] += 1
        elif x == -9:
            a[1] += 1
        elif x == -8:
            a[2] += 1
        elif x == -7:
            a[3] += 1
        elif x == -6:
            a[4] += 1
        elif x == -5:
            a[5] += 1
        elif x == -4:
            a[6] += 1
        elif x == -3:
            a[7] += 1
        elif x == -2:
            a[8] += 1
        elif x == -1:
            a[9] += 1
        elif x == 0:
            a[10] += 1
        elif x == 1:
            a[11] += 1
        elif x == 2:
            a[12] += 1
        elif x == 3:
            a[13] += 1
        elif x == 4:
            a[14] += 1
        elif x == 5:
            a[15] += 1
        elif x == 6:
            a[16] += 1
        elif x == 7:
            a[17] += 1
        elif x == 8:
            a[18] += 1
        elif x == 9:
            a[19] += 1
        elif x == 10:
            a[20] += 1
    return a

def lfCount(d):
    lf = []
    for p in d:
        lf.append(p.getLF())
    a = [0,0,0,0,0,0,0,0,0,0,0]
    for x in lf:
        if x == -3:
            a[0] += 1
        elif x == -2:
            a[1] += 1
        elif x == -1:
            a[2] += 1
        elif x == 0:
            a[3] += 1
        elif x == 1:
            a[4] += 1
        elif x == 2:
            a[5] += 1
        elif x == 3:
            a[6] += 1
        elif x == 4:
            a[7] += 1
        elif x == 5:
            a[8] += 1
        elif x == 6:
            a[9] += 1
        elif x == 7:
            a[10] += 1
    return a

def prCount(d):
    pr = []
    for p in d:
        pr.append(p.getProtest())
    a = [0,0,0,0,0,0,0,0,0]
    for x in pr:
        if x == -4:
            a[0] += 1
        elif x == -3:
            a[1] += 1
        elif x == -2:
            a[2] += 1
        elif x == -1:
            a[3] += 1
        elif x == 0:
            a[4] += 1
        elif x == 1:
            a[5] += 1
        elif x == 2:
            a[6] += 1
        elif x == 3:
            a[7] += 1
        elif x == 4:
            a[8] += 1
    return a

def pyCount(d):
    pr = []
    for p in d:
        pr.append(p.getPayment())
    a = [0,0,0,0,0,0,0]
    for x in pr:
        if x == -3:
            a[0] += 1
        elif x == -2:
            a[1] += 1
        elif x == -1:
            a[2] += 1
        elif x == 0:
            a[3] += 1
        elif x == 1:
            a[4] += 1
        elif x == 2:
            a[5] += 1
        elif x == 3:
            a[6] += 1
    return a

def pnCount(d):
    pr = []
    for p in d:
        pr.append(p.getPandemic())
    a = [0,0,0,0,0,0,0]
    for x in pr:
        if x == -3:
            a[0] += 1
        elif x == -2:
            a[1] += 1
        elif x == -1:
            a[2] += 1
        elif x == 0:
            a[3] += 1
        elif x == 1:
            a[4] += 1
        elif x == 2:
            a[5] += 1
        elif x == 3:
            a[6] += 1
    return a

def JTViolate(d):
    j = []
    for p in d:
        j.append(p.treatment.getViolate())
    a = [0, 0]
    for x in j:
        if x == "Y":
            a[0] += 1
        elif x == "N":
            a[1] += 1
    return a

def JTSuspend(d):
    j = []
    for p in d:
        j.append(p.treatment.getSuspend())
    a = [0, 0]
    for x in j:
        if x == "Y":
            a[0] += 1
        elif x == "N":
            a[1] += 1
    return a

def JTDraft(d):
    j = []
    for p in d:
        j.append(p.treatment.getDraft())
    a = [0, 0]
    for x in j:
        if x == "Y":
            a[0] += 1
        elif x == "N":
            a[1] += 1
    return a

def JTCompensation(d):
    j = []
    for p in d:
        j.append(p.treatment.getCompensation())
    a = [0, 0]
    for x in j:
        if x == "Y":
            a[0] += 1
        elif x == "N":
            a[1] += 1
    return a

def JTSocial(d):
    j = []
    for p in d:
        j.append(p.treatment.getSocial())
    a = [0, 0]
    for x in j:
        if x == "Y":
            a[0] += 1
        elif x == "N":
            a[1] += 1
    return a

def JTPandemic(d):
    j = []
    for p in d:
        j.append(p.treatment.getPandemic())
    a = [0, 0]
    for x in j:
        if x == "Y":
            a[0] += 1
        elif x == "N":
            a[1] += 1
    return a

def graph(group, type, d):
    if type == "rr":
        title = group +" Racial Resentment"
        rrLabels = ["-10","-9","-8","-7","-6","-5","-4","-3","-2","-1","0","1","2","3","4","5","6","7","8","9","10"]
        rr = rrCount(d)
        plot(title, "Responses", "Score", rrLabels, rr)
    elif type == "lf":
        title = group + " Linked Fate"
        lfLabels = ["-3","-2","-1","0","1","2","3","4","5","6","7"]
        lf = lfCount(d)
        plot(title, "Responses", "Score", lfLabels, lf)
    elif type == "pr":
        title = group+" Protest"
        prLabels = ["-4","-3","-2","-1","0","1","2","3","4"]
        pr = prCount(d)
        plot(title, "Responses", "Score", prLabels, pr)
    elif type == "py":
        title = group+" Payment"
        pyLabels = ["-3","-2","-1","0","1","2","3"]
        py = pyCount(d)
        plot(title, "Responses", "Score", pyLabels, py)
    elif type == "pn":
        title == group+" Pandemic"
        pnLabels = ["-3","-2","-1","0","1","2","3"]
        pn = pnCount(d)
        plot(title, "Responses", "Score", pnLabels, pn)


d = data('response1.csv') #all data
d2 = data('response2.csv')
for p in d2:
    d.append(p)
white, black = race(d)
dem, rep, ind = party(d)
lib, mod, con = ideology(d)
retail, neutral, resentment, linked = treatment(d)
rr, lf = align(d)

# b_rr = lfCount(black)
# w_rr = lfCount(white)
# lfLabels = ["-3","-2","-1","0","1","2","3","4","5","6","7"]
# plot("Frequency of Linked Fate Scores", "Frequency", "Scores", lfLabels, b_rr, "Black", w_rr, "White")



#score guide:
#rr: racial resentment
#lf: linked fate
#pr: protest
#py: payment
#pn: pandemic

w_rr = combine(white, rr)
w_lf = combine(white, lf)

w_rr = combine(w_rr, lib)
w_lf = combine(w_lf, lib)

J_w_rr = JTPandemic(w_rr)
J_w_lf = JTPandemic(w_lf)

labels = ["Yes", "No"]

x = np.arange(len(labels))
width = 0.2
fig, ax = plt.subplots()
rects1 = ax.bar(x - (width/2), J_w_rr, width, label='Racial Resentment')
rects2 = ax.bar(x + (width/2), J_w_lf, width, label='Linked Fate')



ax.set_ylabel('Responses')
ax.set_title("White Liberal Responses to Pandemic Question")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_xlabel('Answers')
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)


fig.tight_layout()

#Edit this line with group, score code, and data to produce graph
#graph("Black", "lf", black)


plt.show()
