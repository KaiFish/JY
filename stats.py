import statistics as st
import csv
from person import Person
from treatment import Treatment
from enums import *
from read import *
import random as r
import math

r.seed(72)

def s(i):
    return str(len(i))

def race(d):
    w = []
    b = []
    for p in d:
        race = p.getRace()
        if race == Race.WHITE:
            w.append(p)
        elif race == Race.BLACK:
            b.append(p)
    return w, b

def snap(d, n):
    for i in range(n):
        x = r.randrange(0, len(d))
        d.pop(x)
    return d

def party(s):
    d = []
    r = []
    i = []
    for p in s:
        party = p.getParty()
        if party == Party.DEM:
            d.append(p)
        elif party == Party.REP:
            r.append(p)
        elif party == Party.IND:
            i.append(p)
    return d, r, i

def ideology(d):
    l = []
    m = []
    c = []
    for p in d:
        i = p.getIdeology()
        if i == Ideology.LIB:
            l.append(p)
        elif i == Ideology.MOD:
            m.append(p)
        elif i == Ideology.CON:
            c.append(p)
    return l, m, c

def treatment(d):
    r = []
    n = []
    rr = []
    lf = []
    for p in d:
        type = p.getType()
        if type == "Retail Control Group":
            r.append(p)
        elif type == "Race Neutral Control Group":
            n.append(p)
        elif type == "Racial Resentment Treatment Group":
            rr.append(p)
        elif type == "Linked Fate Treatment Group":
            lf.append(p)
    return r, n, rr, lf

def align(d):
    rr = []
    lf = []
    for p in d:
        x = p.LF
        y = p.RR
        if x == "HIGH":
            lf.append(p)
        if y == "HIGH":
            rr.append(p)
    return rr, lf

def combine(a, b):
    c = []
    for x in a:
        if x in b:
            c.append(x)
    return c

def distribution(d, name):
    m = st.mean(d)
    sd = st.stdev(d)
    sd_n2, sd_n1, sd_p1, sd_p2 = 0, 0, 0, 0
    if sd >= 0:
        sd_n2 = m - (2*sd)
        sd_n1 = m - sd
        sd_p1 = m + sd
        sd_p2 = m + (2*sd)
    else:
        sd_n2 = m + (2*sd)
        sd_n1 = m + sd
        sd_p1 = m - sd
        sd_p2 = m - (2*sd)
    out = 0
    mid = 0
    i = 0
    for x in d:
        if x < sd_n2:
            out += 1
        elif x >= sd_n2 and x < sd_n1:
            mid += 1
        elif x >= sd_n1 and x < m:
            i += 1
        elif x >= m and x <= sd_p1:
            i += 1
        elif x > sd_p1 and x <= sd_p2:
            mid += 1
        elif x > sd_p2:
            out += 1
    t = len(d)
    sd1 = int((i/t) * 100)
    sd2 = int(((i+mid)/t) * 100)
    print(name)
    print("mean: " + str(m) + "\t stDEV: " + str(sd))
    print("mean + 1SD " + str(m+sd))
    print("mean - 1SD " + str(m-sd))
    print("1 SD: " + str(sd1) + "% \t 2 SD: " +str(sd2) + "%")

def scores(d, name):
    rr = []
    lf = []
    pr = []
    py = []
    pn = []
    for p in d:
        rr.append(p.getRR())
        lf.append(p.getLF())
        pr.append(p.getProtest())
        py.append(p.getPayment())
        pn.append(p.getPandemic())

    print("Group: " + name)
    distribution(rr, "Racial Resentment")
    distribution(lf, "Linked Fate")
    distribution(pr, "Protest")
    distribution(py, "Payment")
    distribution(pn, "Pandemic")

def v(s1, n1, s2, n2):
    a = (s1/n1)
    b = (s2/n2)
    c = (a+b)*(a+b)
    d = ((a*a)/(n1-1))+((b*b)/n2-1)
    return c/d

def t_test(d1, d2):
    m1 = st.mean(d1)
    s1 = st.variance(d1)
    m2 = st.mean(d2)
    s2 = st.variance(d2)
    n1 = len(d1)
    n2 = len(d2)
    t = (m1-m2)/math.sqrt((s1/n1)+(s2/n2))
    print("v: " + str(v(s1, n1, s2, n2)))
    return t


d = data('response1.csv')
d2 = data('response2.csv')
for p in d2:
    d.append(p)
white, black = race(d)
#white = snap(white, 400)
dem, rep, ind = party(d)
retail, neutral, resentment, linked = treatment(d)

r_rr= []
for p in retail:
    r_rr.append(p.getRR())
n_rr = []
for p in neutral:
    n_rr.append(p.getRR())

#scores(d, "Data")
