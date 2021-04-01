import statistics as st
import csv
from person import Person
from treatment import Treatment
from enums import *
from read import *

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

def combine(a, b):
    c = []
    for x in a:
        if x in b:
            c.append(x)
    return c

def distribution(d, name):
    m = st.mean(d)
    sd = st.mean(d)
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


d = data('response1.csv')
d2 = data('response2.csv')
for p in d2:
    d.append(p)
white, black = race(d)
dem, rep, ind = party(d)
retail, neutral, resentment, linked = treatment(d)


w_dem = combine(white, dem)
b_dem = combine(black, dem)
w_rep = combine(white, rep)
b_rep = combine(black, rep)
w_ind = combine(white, ind)
b_ind = combine(black, ind)


w_r = combine(white, retail)
b_r = combine(black, retail)
w_n = combine(white, neutral)
b_n = combine(black, neutral)
w_rr = combine(white, resentment)
b_rr = combine(black, resentment)
w_lf = combine(white, linked)
b_lf = combine(black, linked)


w_d_r = combine(w_dem, retail)
b_d_r = combine(b_dem, retail)
w_r_r = combine(w_rep, retail)
b_r_r = combine(b_rep, retail)
w_i_r = combine(w_ind, retail)
b_i_r = combine(b_ind, retail)


w_d_n = combine(w_dem, neutral)
b_d_n = combine(b_dem, neutral)
w_r_n = combine(w_rep, neutral)
b_r_n = combine(b_rep, neutral)
w_i_n = combine(w_ind, neutral)
b_i_n = combine(b_ind, neutral)


w_d_rr = combine(w_dem, resentment)
b_d_rr = combine(b_dem, resentment)
w_r_rr = combine(w_rep, resentment)
b_r_rr = combine(b_rep, resentment)
w_i_rr = combine(w_ind, resentment)
b_i_rr = combine(b_ind, resentment)


w_d_lf = combine(w_dem, linked)
b_d_lf = combine(b_dem, linked)
w_r_lf = combine(w_rep, linked)
b_r_lf = combine(b_rep, linked)
w_i_lf = combine(w_ind, linked)
b_i_lf = combine(b_ind, linked)

print("Total Response: " + s(d))
print("White: " + s(white) + "\t" + "Black: " + s(black))
print("DEM: " + s(dem) + "\t" + "REP: " + s(rep) + "\t" + "IND: " + s(ind))
print("Retail: " + s(retail) + "\t" + "Neutral: " + s(neutral) + "\t" + "Resentment: " + s(resentment) + "\t" + "Linked: " + s(linked))
print()
print("DEM -" + "\t" + "White: " + s(w_dem) + "\t" + "Black: " + s(b_dem))
print("REP -" + "\t" + "White: " + s(w_rep) + "\t" + "Black: " + s(b_rep))
print("IND -" + "\t" + "White: " + s(w_ind) + "\t" + "Black: " + s(b_ind))
print()
print("retail -" + "\t" +  "White: " + s(w_r) + "\t" + "Black: " + s(b_r))
print("neutral -" + "\t" + "White: " + s(w_n) + "\t" + "Black: " + s(b_n))
print("resentment -" + "\t" + "White: " + s(w_rr) + "\t" + "Black: " + s(b_rr))
print("linked -" + "\t" + "White: " + s(w_lf) + "\t" + "Black: " + s(b_lf))
print()
print("retail - \t" + "white dem: " + s(w_d_r)+ "\t black dem: " + s(b_d_r) + "\t white rep: " + s(w_r_r) + "\t black rep: " + s(b_r_r) + "\t white ind: " + s(w_i_r) + "\t black ind: " + s(b_i_r))
print("neutral - \t" + "white dem: " + s(w_d_n)+ "\t black dem: " + s(b_d_n) + "\t white rep: " + s(w_r_n) + "\t black rep: " + s(b_r_n) + "\t white ind: " + s(w_i_n) + "\t black ind: " + s(b_i_n))
print("resentment - \t" + "white dem: " + s(w_d_rr)+ "\t black dem: " + s(b_d_rr) + "\t white rep: " + s(w_r_rr) + "\t black rep: " + s(b_r_rr) + "\t white ind: " + s(w_i_rr) + "\t black ind: " + s(b_i_rr))
print("linked - \t" + "white dem: " + s(w_d_lf)+ "\t black dem: " + s(b_d_lf) + "\t white rep: " + s(w_r_lf) + "\t black rep: " + s(b_r_lf) + "\t white ind: " + s(w_i_lf) + "\t black ind: " + s(b_i_lf))
print()
print()


scores(d, "Total")
print("----------------------------------")
scores(white, "White")
print("----------------------------------")
scores(black, "Black")
print("----------------------------------")
scores(dem, "Democrat")
print("----------------------------------")
scores(rep, "Republican")
print("----------------------------------")
scores(ind, "Independent")
print("----------------------------------")
scores(retail, "Retail")
print("----------------------------------")
scores(neutral, "Neutral")
print("----------------------------------")
scores(resentment, "Racial Resentment")
print("----------------------------------")
scores(linked, "Linked Fate")
