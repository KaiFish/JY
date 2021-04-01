from enums import *
from score import Score
from treatment import Treatment
import re

class Person:
    def setRace(self, arg):
        if "Black or African-American" in arg:
            arg = "Black or African-American"
        r = {
            "White" : Race.WHITE,
            "Black or African-American" : Race.BLACK,
            "Hispanic/Latinx" : Race.HISP_LAT,
            "Asian or Asian American" : Race.ASIAN,
            "Native Hawaiian or Pacific Islander" : Race.PACIFIC,
            "Prefer not to say" : Race.ND,
            "" : Race.X
        }
        self.race = r.get(arg, Race.MIXED)

    def setGender(self, arg):
        g = {
            "Male" : Gender.MALE,
            "Female" : Gender.FEMALE,
            "Other" : Gender.OTHER,
            "Prefer Not to Say" : Gender.ND,
            "" : Gender.X
        }
        self.gender = g.get(arg)

    def setAge(self, arg):
        a = {
            1 : Age.TEENS,
            2 : Age.TWENTIES,
            3 : Age.THIRTIES,
            4 : Age.FORTIES,
            5 : Age.FIFTIES,
            6 : Age.SIXTIES,
            7 : Age.SEVENTIES,
            8 : Age.EIGHTIES,
            9 : Age.NINTIES
        }
        if arg == "":
            self.age = Age.X
        else:
            i = re.sub('\D', '', arg)
            if int(int(i)/10) >= 10:
                self.age = Age.MORE
            else:
                self.age = a.get(int(int(i)/10))

    def setEducation(self, arg):
        e = {
            "Some High School, No Diploma" : Education.SOME_HS,
            "High School Degree or GED" : Education.HS_GED,
            "Associate's Degree" : Education.ASSOC,
            "Some College, No Diploma" : Education.SOME_COLL,
            "Bachelor's Degree" : Education.BACH,
            "Master's Degree (MS, MBA, MED)" : Education.MAST,
            "Professional Degree (PhD, JD, MD)" : Education.PROF,
            "" : Education.X
        }
        self.education = e.get(arg)

    def setParty(self, arg):
        p = {
            "Democrat" : Party.DEM,
            "Republican" : Party.REP,
            "Independent" : Party.IND,
            "" : Party.X
        }
        self.party = p.get(arg)

    def setVote(self, arg):
        v = {
            "Yes" : Vote.YES,
            "No" : Vote.NO,
            "Rather not say" : Vote.ND,
            "" : Vote.X
        }
        self.vote = v.get(arg)

    def setIdeology(self, arg):
        i = {
            "Liberal" : Ideology.LIB,
            "Conservative" : Ideology.CON,
            "Moderate" : Ideology.MOD,
            "" : Ideology.X
        }
        self.ideology = i.get(arg)

    def setIncome(self, arg):
        i = {
            "0k-24k" : Income.A,
            "25k-50k" : Income.B,
            "51k-100k" : Income.C,
            "101k-300k" : Income.D, # ????
            "300k-500k" : Income.E,
            "500k+" : Income.F,
            "" : Income.X
        }
        self.income = i.get(arg)

    def setUnion(self, arg):
        u = {
            "Yes" : Union.YES,
            "No" : Union.NO,
            "" : Union.X
        }
        self.union = u.get(arg)

    def setAthlete(self,arg):
        a = {
            "Yes" : Athlete.YES,
            "No" : Athlete.NO,
            "" : Athlete.X
        }
        self.athlete = a.get(arg)

    def setFriend(self, arg):
        f = {
            "Yes" : Friend.YES,
            "No" : Friend.NO,
            "" : Friend.X
        }
        self.friend = f.get(arg)

    def setRegion(self, arg):
        r = {
            "Foriegn Country" : Region.FORIEGN,
            "Northeast" : Region.NORTHEAST,
            "Mid Atlantic" : Region.MIDATLANTIC,
            "Southeast" : Region.SOUTHEAST,
            "Midwest" : Region.MIDWEST,
            "Southwest" : Region.SOUTHWEST,
            "West Coast" : Region.WESTCOAST,
            "Northwest" : Region.NORTHWEST,
            "" : Region.X
        }
        self.region = r.get(arg)

    def setNCAA_Athlete(self, arg):
        a = {
            "Strongly Support" : NCAA_Athlete.S_SUPPORT,
            "Somewhat Support" : NCAA_Athlete.SUPPORT,
            "Neither Support Nor Oppose" : NCAA_Athlete.NEITHER,
            "Somewhat Oppose" : NCAA_Athlete.OPPOSE,
            "Strongly Oppose" : NCAA_Athlete.S_OPPOSE,
            "" : NCAA_Athlete.X
        }
        self.ncaa_athlete = a.get(arg)

    def setNCAA_Admin(self, arg):
        a = {
            "Strongly Support" : NCAA_Admin.S_SUPPORT,
            "Somewhat Support" : NCAA_Admin.SUPPORT,
            "Neither Support Nor Oppose" : NCAA_Admin.NEITHER,
            "Somewhat Oppose" : NCAA_Admin.OPPOSE,
            "Strongly Oppose" : NCAA_Admin.S_OPPOSE,
            "" : NCAA_Admin.X
        }
        self.ncaa_admin = a.get(arg)

    def __init__(self, stuff, treatment):
        self.setRace(stuff[0])
        self.setGender(stuff[1])
        self.setAge(stuff[2])
        self.setEducation(stuff[3])
        self.setParty(stuff[5])
        self.setVote(stuff[6])
        self.setIdeology(stuff[7])
        self.setIncome(stuff[8])
        self.setUnion(stuff[9])
        self.setAthlete(stuff[10])
        self.setFriend(stuff[12])
        self.setRegion(stuff[13])
        self.setNCAA_Athlete(stuff[14])
        self.setNCAA_Admin(stuff[15])
        self.score = Score()
        self.score.updateRR(stuff[16])
        self.score.updateRR(stuff[17])
        self.score.updateRR(stuff[18])
        self.score.updateRR(stuff[19])
        self.score.updateLF(stuff[20])
        self.score.updateLF(stuff[21])
        self.score.updateLF(stuff[22])
        self.score.updateLF(stuff[24])
        self.treatment = treatment

    def getRace(self):
        return self.race

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

    def getEducation(self):
        return self.education

    def getParty(self):
        return self.party

    def getVote(self):
        return self.vote

    def getIdeology(self):
        return self.ideology

    def getIncome(self):
        return self.income

    def getUnion(self):
        return self.union

    def getAthlete(self):
        return self.athlete

    def getFriend(self):
        return self.friend

    def getRegion(self):
        return self.region

    def getNCAA_Athlete(self):
        return self.ncaa_athlete

    def getNCAA_Admin(self):
        return self.ncaa_admin

    def getScore(self):
        return self.score.getScore()

    def getTreatment(self):
        return self.treatment

    def getType(self):
        return self.treatment.getName()

    def getRR(self):
        return self.score.getRR()

    def getLF(self):
        return self.score.getLF()

    def getPayment(self):
        return self.treatment.getPayment()

    def getProtest(self):
        return self.treatment.getProtest()

    def getPandemic(self):
        return self.treatment.getSafety()

    def __str__(self):
        x = self.income.name
        i = ""
        if x == "A":
            i = "0 - 24k"
        elif x == "B":
            i = "25k - 50k"
        elif x == "C":
            i = "51k - 100k"
        elif x == "D":
            i = "101k - 300k"
        elif x == "E":
            i = "301k - 500k"
        elif x == "F":
            i = "500k+"
        else:
            i = "X"

        s = "--------------------------------------"
        s += "--------------------------------------------------"
        s +=  "Race: " + self.race.name
        s += "\t" + "Gender: " + self.gender.name
        s += "\t" + "Age: " + self.age.name
        s += "\t" + "Education: " + self.education.name
        if len(s) <= 148:
            s += "  "
        s += "\t" + "Region: " + self.region.name
        s += "\n" + "Party: " + self.party.name
        s += "\t" + "Ideology: " + self.ideology.name
        s += "\t" + "Voter: " + self.vote.name
        s += "\t" + "Union: " + self.union.name
        s += "\t\t" + "Income: " + i
        s += "\n" + "Athlete: " + self.athlete.name
        s += "\t" + "Friend: " + self.friend.name
        s += "\t" + "Athlete_O: " + self.ncaa_athlete.name
        s += "\t\t\t" + "Admin_O: " + self.ncaa_admin.name
        s += "\n" + "--------------------------------------"
        s += "--------------------------------------------------"
        s += "\n" + "Racial Resentment: " + str(self.getRR())
        s += "\t" + "Linked Fate: " + str(self.getLF())
        s += "\t" + "Treatment: " + self.treatment.getName()
        s += "\n" + "--------------------------------------"
        s += "--------------------------------------------------"
        s += "\n" + "Payment: " + str(self.getPayment())
        s += "\t" + "Protest: " + str(self.getProtest())
        s += "\t" + "Pandemic: " + str(self.getPandemic())
        s += "\n" + "--------------------------------------"
        s += "--------------------------------------------------"
        s += "\n" + "Violate: " + self.treatment.getViolate()
        s += "\t" + "Suspend: " + self.treatment.getSuspend()
        s += "\t" + "Draft: " + self.treatment.getDraft()
        s += "\t" + "Compensation: " + self.treatment.getCompensation()
        s += "\t" + "Social: " + self.treatment.getSocial()
        s += "\t" + "Pandemic: " + self.treatment.getPandemic()
        s += "\n" + "--------------------------------------"
        s += "--------------------------------------------------"
        return s
