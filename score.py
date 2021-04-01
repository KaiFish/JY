class Score:
    def __init__(self):
        self.rr = 0
        self.lf = 0

    def edit(self, s):
        if s == "Strongly agree":
            return 2
        elif s == "Somewhat agree":
            return 1
        elif s == "Neither agree or disagree":
            return 0
        elif s == "Somewhat disagree":
            return -1
        elif s == "Strongly disagree":
            return -2
        elif s == "Extremely Hardworking":
            return 3
        elif s == "Moderately Hardworking":
            return 2
        elif s == "Marginally Hardworking":
            return 1
        elif s == "Neutral":
            return 0
        elif s == "Marginally Lazy":
            return -1
        elif s == "Moderately Lazy":
            return -2
        elif s == "Extremely Lazy":
            return -3
        elif s == "Extremely Intelligent":
            return 3
        elif s == "Moderately Intelligent":
            return 2
        elif s == "Marginally Intelligent":
            return 1
        elif s == "Neutral":
            return 0
        elif s == "Marginally Unintelligent":
            return -1
        elif s == "Moderately Intelligent":
            return -2
        elif s == "Extremely Unintelligent":
            return -3
        elif s == "Yes":
            return 1
        elif s == "No":
            return -1
        elif s == "Better":
            return -1
        elif s == "Same":
            return 0
        elif s == "Worse":
            return 1
        elif s == "Explain your opinion here":
            return 0
        elif s == "Extremely important":
            return 4
        elif s == "Very important":
            return 3
        elif s == "Moderately important":
            return 2
        elif s == "Slightly important":
            return 1
        elif s == "Not at all important":
            return 0
        else:
            return 0

    def updateRR(self, s):
        self.rr += self.edit(s)

    def updateLF(self, s):
        self.lf += self.edit(s)

    def getRR(self):
        return self.rr

    def getLF(self):
        return self.lf
