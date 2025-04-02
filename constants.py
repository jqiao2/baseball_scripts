from enum import Enum

DATE_FORMAT_STRING = '%Y-%m-%d'

LAA = 'Los Angeles Angels'
AZ = 'Arizona Diamondbacks'
BAL = 'Baltimore Orioles'
BOS = 'Boston Red Sox'
CHC = 'Chicago Cubs'
CIN = 'Cincinnati Reds'
CLE = 'Cleveland Guardians'
COL = 'Colorado Rockies'
DET = 'Detroit Tigers'
HOU = 'Houston Astros'
KC = 'Kansas City Royals'
LAD = 'Los Angeles Dodgers'
WSH = 'Washington Nationals'
NYM = 'New York Mets'
OAK = 'Oakland Athletics'
PIT = 'Pittsburgh Pirates'
SD = 'San Diego Padres'
SEA = 'Seattle Mariners'
SF = 'San Francisco Giants'
STL = 'St. Louis Cardinals'
TB = 'Tampa Bay Rays'
TEX = 'Texas Rangers'
TOR = 'Toronto Blue Jays'
MIN = 'Minnesota Twins'
PHI = 'Philadelphia Phillies'
ATL = 'Atlanta Braves'
CWS = 'Chicago White Sox'
MIA = 'Miami Marlins'
NYY = 'New York Yankees'
MIL = 'Milwaukee Brewers'

AL = "American League"
AL_WEST = "American League West"
AL_CENTRAL = "American League Central"
AL_EAST = "American League East"
NL = "National League"
NL_WEST = "National League West"
NL_CENTRAL = "National League Central"
NL_EAST = "National League East"


class TEAMS(Enum):
    Arizona_Diamondbacks = 109
    Atlanta_Braves = 144
    Baltimore_Orioles = 110
    Boston_Red_Sox = 111
    Chicago_White_Sox = 145
    Chicago_Cubs = 112
    Cincinnati_Reds = 113
    Cleveland_Guardians = 114
    Colorado_Rockies = 115
    Detroit_Tigers = 116
    Houston_Astros = 117
    Kansas_City_Royals = 118
    Los_Angeles_Angels = 108
    Los_Angeles_Dodgers = 119
    Miami_Marlins = 146
    Milwaukee_Brewers = 158
    Minnesota_Twins = 142
    New_York_Yankees = 147
    New_York_Mets = 121
    Oakland_Athletics = 133
    Philadelphia_Phillies = 143
    Pittsburgh_Pirates = 134
    San_Diego_Padres = 135
    Seattle_Mariners = 136
    San_Francisco_Giants = 137
    St_Louis_Cardinals = 138
    Tampa_Bay_Rays = 139
    Texas_Rangers = 140
    Toronto_Blue_Jays = 141
    Washington_Nationals = 120


teams = {
    108: LAA,
    109: AZ,
    110: BAL,
    111: BOS,
    112: CHC,
    113: CIN,
    114: CLE,
    115: COL,
    116: DET,
    117: HOU,
    118: KC,
    119: LAD,
    120: WSH,
    121: NYM,
    133: OAK,
    134: PIT,
    135: SD,
    136: SEA,
    137: SF,
    138: STL,
    139: TB,
    140: TEX,
    141: TOR,
    142: MIN,
    143: PHI,
    144: ATL,
    145: CWS,
    146: MIA,
    147: NYY,
    158: MIL
}

divisions = {
    "All Teams": {HOU, SEA, TEX, LAA, OAK, CLE, MIN, KC, DET, CWS, BAL, NYY, BOS, TB, TOR, LAD, SD, AZ, SF, COL, MIL, STL, PIT, CIN, CHC, PHI, ATL, NYM, WSH, MIA},
    AL: {HOU, SEA, TEX, LAA, OAK, CLE, MIN, KC, DET, CWS, BAL, NYY, BOS, TB, TOR},
    AL_WEST: {HOU, SEA, TEX, LAA, OAK},
    AL_CENTRAL: {CLE, MIN, KC, DET, CWS},
    AL_EAST: {BAL, NYY, BOS, TB, TOR},
    NL: {LAD, SD, AZ, SF, COL, MIL, STL, PIT, CIN, CHC, PHI, ATL, NYM, WSH, MIA},
    NL_WEST: {LAD, SD, AZ, SF, COL},
    NL_CENTRAL: {MIL, STL, PIT, CIN, CHC},
    NL_EAST: {PHI, ATL, NYM, WSH, MIA},

}
