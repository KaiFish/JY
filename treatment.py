class Treatment:
    def getName(self):
        return self.name

    def getPayment(self):
        return self.payment

    def getProtest(self):
        return self.protest

    def getSafety(self):
        return self.safety

    def edit_I(self, s):
        if s == "Agree" or s == "Agree,Explain your opinion.":
            return -1
        elif s == "Disagree" or s == "Disagree,Explain your opinion.":
            return 1
        elif s == "Completely Agree":
            return -2
        elif s == "Moderately Agree":
            return -1
        elif s == "Neither Agree Nor Disagree":
            return 0
        elif s == "Moderately Disagree":
            return 1
        elif s == "Completely Disagree":
            return 2
        else:
            return 0

    def edit_N(self, s):
        if s == "Agree" or s == "Agree,Explain your opinion.":
            return 1
        elif s == "Disagree" or s == "Disagree,Explain your opinion.":
            return -1
        elif s == "Completely Agree":
            return 2
        elif s == "Moderately Agree":
            return 1
        elif s == "Neither Agree Nor Disagree":
            return 0
        elif s == "Moderately Disagree":
            return -1
        elif s == "Completely Disagree":
            return -2
        else:
            return 0

    def updatePayment(self, i):
        self.payment += i

    def updateProtest(self, i):
        self.protest += i

    def updateSafety(self, i):
        self.safety += i

    def setViolate(self, s):
        if s == "Yes" or s == "Yes,Explain your opinion":
            self.violate = 1
        elif s == "No" or s == "No,Explain your opinion":
            self.violate = -1

    def setSuspend(self, s):
        if s == "Yes" or s == "Yes,Explain your opinion":
            self.suspend = 1
        elif s == "No" or s == "No,Explain your opinion":
            self.suspend = -1

    def setDraft(self, s):
        if s == "Yes" or s == "Yes,Explain your opinion":
            self.draft = 1
        elif s == "No" or s == "No,Explain your opinion":
            self.draft = -1

    def setCompensation(self, s):
        if s == "Yes" or s == "Yes,Explain your opinion":
            self.compensation = 1
        elif s == "No" or s == "No,Explain your opinion":
            self.compensation = -1

    def setSocial(self, s):
        if s == "Yes" or s == "Yes,Explain your opinion":
            self.social = 1
        elif s == "No" or s == "No,Explain your opinion":
            self.social = -1

    def setPandemic(self, s):
        if s == "Yes" or s == "Yes,Explain your opinion":
            self.pandemic = 1
        elif s == "No" or s == "No,Explain your opinion":
            self.pandemic = -1

    def useItems(self, items):
        if self.name == "Retail Control Group":
            self.updatePayment(self.edit_N(items[0]))
            self.updatePayment(self.edit_N(items[1]))
            self.updateSafety(self.edit_I(items[2]))
            self.updateProtest(self.edit_N(items[3]))
            self.updateProtest(self.edit_I(items[4]))
            self.updateSafety(self.edit_N(items[5]))
        elif self.name == "Race Neutral Control Group":
            self.setViolate(items[0])
            self.setSuspend(items[2])
            self.setDraft(items[4])
            self.updatePayment(self.edit_N(items[8]))
            self.updatePayment(self.edit_N(items[9]))
            self.updateSafety(self.edit_I(items[10]))
            self.updateProtest(self.edit_N(items[11]))
            self.updateProtest(self.edit_I(items[12]))
            self.updateSafety(self.edit_N(items[13]))
        elif self.name == "Racial Resentment Treatment Group":
            self.setViolate(items[0])
            self.setSuspend(items[2])
            self.setDraft(items[5])
            self.setCompensation(items[7])
            self.setSocial(items[9])
            self.setPandemic(items[11])
            self.updatePayment(self.edit_N(items[14]))
            self.updatePayment(self.edit_N(items[15]))
            self.updateSafety(self.edit_I(items[16]))
            self.updateProtest(self.edit_N(items[17]))
            self.updateProtest(self.edit_I(items[18]))
            self.updateSafety(self.edit_N(items[19]))
        elif self.name == "Linked Fate Treatment Group":
            self.setViolate(items[0])
            self.setSuspend(items[1])
            self.setDraft(items[3])
            self.setCompensation(items[4])
            self.setSocial(items[5])
            self.setPandemic(items[6])
            self.updatePayment(self.edit_N(items[8]))
            self.updatePayment(self.edit_N(items[9]))
            self.updateSafety(self.edit_I(items[10]))
            self.updateProtest(self.edit_N(items[12]))
            self.updateProtest(self.edit_I(items[13]))
            self.updateSafety(self.edit_N(items[14]))

    def __init__(self, name, items):
        self.name = name
        self.payment = 0
        self.protest = 0
        self.safety = 0
        self.violate = 0
        self.suspend = 0
        self.draft = 0
        self.compensation = 0
        self.social = 0
        self.pandemic = 0
        self.useItems(items)

    def getViolate(self):
        if self.violate == 1:
            return "Y"
        elif self.violate == -1:
            return "N"
        else:
            return "X"

    def getSuspend(self):
        if self.suspend == 1:
            return "Y"
        elif self.suspend == -1:
            return "N"
        else:
            return "X"

    def getDraft(self):
        if self.draft == 1:
            return "Y"
        elif self.draft == -1:
            return "N"
        else:
            return "X"

    def getCompensation(self):
        if self.compensation == 1:
            return "Y"
        elif self.compensation == -1:
            return "N"
        else:
            return "X"

    def getSocial(self):
        if self.social == 1:
            return "Y"
        elif self.social == -1:
            return "N"
        else:
            return "X"

    def getPandemic(self):
        if self.pandemic == 1:
            return "Y"
        elif self.pandemic == -1:
            return "N"
        else:
            return "X"
