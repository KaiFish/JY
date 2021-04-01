import csv
with open ('response.csv', newline = '') as f1, open('response2.csv', newline = '') as f2:
    r1 = csv.reader(f1)
    r2 = csv.reader(f2)
    i = 0
    j = 0
    a = next(r1)
    b = next(r2)
    for (x,y) in zip(a,b):
        if i == 20 or i == 45 or i == 51 or i == 65 or i == 85:
            j = 0
        print(str(i) + " : " + str(j))
        print(x + " : " + y)
        print("")
        i += 1
        j += 1
    input()
