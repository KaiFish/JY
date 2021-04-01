from enum import Enum
class Race(Enum):
    WHITE = 1
    BLACK = 2
    HISP_LAT = 3
    ASIAN = 4
    PACIFIC = 5
    OTHER = 6
    MIXED = 7
    ND = 8
    X = 9

class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    ND = 4
    X = 5

class Age(Enum):
    TEENS = 1
    TWENTIES = 2
    THIRTIES = 3
    FORTIES = 4
    FIFTIES = 5
    SIXTIES = 6
    SEVENTIES = 7
    EIGHTIES = 8
    NINTIES = 9
    MORE = 10
    X = 11

class Education(Enum):
    SOME_HS = 1
    HS_GED = 2
    ASSOC = 3
    SOME_COLL = 4
    BACH = 5
    MAST = 6
    PROF = 7
    X = 8

class Party(Enum):
    DEM = 1
    REP = 2
    IND = 3
    X = 4

class Vote(Enum):
    YES = 1
    NO = 2
    ND = 3
    X = 4

class Ideology(Enum):
    LIB = 1
    CON = 2
    MOD = 3
    X = 4

class Income(Enum):
    A = 24
    B = 50
    C = 100
    D = 300
    E = 500
    F = 501
    X = 1

class Union(Enum):
    YES = 1
    NO = 2
    X = 3

class Athlete(Enum):
    YES = 1
    NO = 2
    X = 3

class Friend(Enum):
    YES = 1
    NO = 2
    X = 3

class Region(Enum):
    FORIEGN = 1
    NORTHEAST = 2
    MIDATLANTIC = 3
    SOUTHEAST = 4
    MIDWEST = 5
    SOUTHWEST = 6
    WESTCOAST = 7
    NORTHWEST = 8
    X = 9

class NCAA_Athlete(Enum):
    S_SUPPORT = 1
    SUPPORT = 2
    NEITHER = 3
    OPPOSE = 4
    S_OPPOSE = 5
    X = 6

class NCAA_Admin(Enum):
    S_SUPPORT = 1
    SUPPORT = 2
    NEITHER = 3
    OPPOSE = 4
    S_OPPOSE = 5
    X = 6
