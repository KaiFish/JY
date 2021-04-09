from enums import *
from score import Score
from treatment import Treatment
from person import Person
h = ["Race", "Gender", "Age", "Education", "Party", "Vote", "Ideology", "Income", "Union", "Athlete", "Friend of Athlete", "Region", "Support for NCAA Athletes", "Support for NCAA Administrators", "Racial Resentment Score", "Linked Fate Score", "Treatment Group", "Payment Score", "Protest Score", "Pandemic Score", "Violation Response", "Suspension Response", "Draft Response", "Compensation Response", "Social Image Response", "Pandemic Response", "LF", "RR"]


class DataSet:

    def __init__(self, list):
        self.d = [h]
        self.i = 0
        for p in list:
            self.d.append(p.lst())

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.d):
            raise StopIteration
        else:
            self.i += 1
            return self.d[self.i-1]
