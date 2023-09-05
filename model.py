#import libraries
import deap
import math
import random

#create scenarioList


def playGame():
    cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
    playerTotal = 0
    dealerCard = 0
    scenarioIDToScenarioNoAce = {
    0: {'playerTotal': 4, 'dealerCard': 2},
    1: {'playerTotal': 4, 'dealerCard': 3},
    2: {'playerTotal': 4, 'dealerCard': 4},
    3: {'playerTotal': 4, 'dealerCard': 5},
    4: {'playerTotal': 4, 'dealerCard': 6},
    5: {'playerTotal': 4, 'dealerCard': 7},
    6: {'playerTotal': 4, 'dealerCard': 8},
    7: {'playerTotal': 4, 'dealerCard': 9},
    8: {'playerTotal': 4, 'dealerCard': 10},
    9: {'playerTotal': 4, 'dealerCard': 11},
    10: {'playerTotal': 5, 'dealerCard': 2},
    11: {'playerTotal': 5, 'dealerCard': 3},
    12: {'playerTotal': 5, 'dealerCard': 4},
    13: {'playerTotal': 5, 'dealerCard': 5},
    14: {'playerTotal': 5, 'dealerCard': 6},
    15: {'playerTotal': 5, 'dealerCard': 7},
    16: {'playerTotal': 5, 'dealerCard': 8},
    17: {'playerTotal': 5, 'dealerCard': 9},
    18: {'playerTotal': 5, 'dealerCard': 10},
    19: {'playerTotal': 5, 'dealerCard': 11},
    20: {'playerTotal': 6, 'dealerCard': 2},
    21: {'playerTotal': 6, 'dealerCard': 3},
    22: {'playerTotal': 6, 'dealerCard': 4},
    23: {'playerTotal': 6, 'dealerCard': 5},
    24: {'playerTotal': 6, 'dealerCard': 6},
    25: {'playerTotal': 6, 'dealerCard': 7},
    26: {'playerTotal': 6, 'dealerCard': 8},
    27: {'playerTotal': 6, 'dealerCard': 9},
    28: {'playerTotal': 6, 'dealerCard': 10},
    29: {'playerTotal': 6, 'dealerCard': 11},
    30: {'playerTotal': 7, 'dealerCard': 2},
    31: {'playerTotal': 7, 'dealerCard': 3},
    32: {'playerTotal': 7, 'dealerCard': 4},
    33: {'playerTotal': 7, 'dealerCard': 5},
    34: {'playerTotal': 7, 'dealerCard': 6},
    35: {'playerTotal': 7, 'dealerCard': 7},
    36: {'playerTotal': 7, 'dealerCard': 8},
    37: {'playerTotal': 7, 'dealerCard': 9},
    38: {'playerTotal': 7, 'dealerCard': 10},
    39: {'playerTotal': 7, 'dealerCard': 11},
    40: {'playerTotal': 8, 'dealerCard': 2},
    41: {'playerTotal': 8, 'dealerCard': 3},
    42: {'playerTotal': 8, 'dealerCard': 4},
    43: {'playerTotal': 8, 'dealerCard': 5},
    44: {'playerTotal': 8, 'dealerCard': 6},
    45: {'playerTotal': 8, 'dealerCard': 7},
    46: {'playerTotal': 8, 'dealerCard': 8},
    47: {'playerTotal': 8, 'dealerCard': 9},
    48: {'playerTotal': 8, 'dealerCard': 10},
    49: {'playerTotal': 8, 'dealerCard': 11},
    50: {'playerTotal': 9, 'dealerCard': 2},
    51: {'playerTotal': 9, 'dealerCard': 3},
    52: {'playerTotal': 9, 'dealerCard': 4},
    53: {'playerTotal': 9, 'dealerCard': 5},
    54: {'playerTotal': 9, 'dealerCard': 6},
    55: {'playerTotal': 9, 'dealerCard': 7},
    56: {'playerTotal': 9, 'dealerCard': 8},
    57: {'playerTotal': 9, 'dealerCard': 9},
    58: {'playerTotal': 9, 'dealerCard': 10},
    59: {'playerTotal': 9, 'dealerCard': 11},
    60: {'playerTotal': 10, 'dealerCard': 2},
    61: {'playerTotal': 10, 'dealerCard': 3},
    62: {'playerTotal': 10, 'dealerCard': 4},
    63: {'playerTotal': 10, 'dealerCard': 5},
    64: {'playerTotal': 10, 'dealerCard': 6},
    65: {'playerTotal': 10, 'dealerCard': 7},
    66: {'playerTotal': 10, 'dealerCard': 8},
    67: {'playerTotal': 10, 'dealerCard': 9},
    68: {'playerTotal': 10, 'dealerCard': 10},
    69: {'playerTotal': 10, 'dealerCard': 11},
    70: {'playerTotal': 11, 'dealerCard': 2},
    71: {'playerTotal': 11, 'dealerCard': 3},
    72: {'playerTotal': 11, 'dealerCard': 4},
    73: {'playerTotal': 11, 'dealerCard': 5},
    74: {'playerTotal': 11, 'dealerCard': 6},
    75: {'playerTotal': 11, 'dealerCard': 7},
    76: {'playerTotal': 11, 'dealerCard': 8},
    77: {'playerTotal': 11, 'dealerCard': 9},
    78: {'playerTotal': 11, 'dealerCard': 10},
    79: {'playerTotal': 11, 'dealerCard': 11},
    80: {'playerTotal': 12, 'dealerCard': 2},
    81: {'playerTotal': 12, 'dealerCard': 3},
    82: {'playerTotal': 12, 'dealerCard': 4},
    83: {'playerTotal': 12, 'dealerCard': 5},
    84: {'playerTotal': 12, 'dealerCard': 6},
    85: {'playerTotal': 12, 'dealerCard': 7},
    86: {'playerTotal': 12, 'dealerCard': 8},
    87: {'playerTotal': 12, 'dealerCard': 9},
    88: {'playerTotal': 12, 'dealerCard': 10},
    89: {'playerTotal': 12, 'dealerCard': 11},
    90: {'playerTotal': 13, 'dealerCard': 2},
    91: {'playerTotal': 13, 'dealerCard': 3},
    92: {'playerTotal': 13, 'dealerCard': 4},
    93: {'playerTotal': 13, 'dealerCard': 5},
    94: {'playerTotal': 13, 'dealerCard': 6},
    95: {'playerTotal': 13, 'dealerCard': 7},
    96: {'playerTotal': 13, 'dealerCard': 8},
    97: {'playerTotal': 13, 'dealerCard': 9},
    98: {'playerTotal': 13, 'dealerCard': 10},
    99: {'playerTotal': 13, 'dealerCard': 11},
    100: {'playerTotal': 14, 'dealerCard': 2},
    101: {'playerTotal': 14, 'dealerCard': 3},
    102: {'playerTotal': 14, 'dealerCard': 4},
    103: {'playerTotal': 14, 'dealerCard': 5},
    104: {'playerTotal': 14, 'dealerCard': 6},
    105: {'playerTotal': 14, 'dealerCard': 7},
    106: {'playerTotal': 14, 'dealerCard': 8},
    107: {'playerTotal': 14, 'dealerCard': 9},
    108: {'playerTotal': 14, 'dealerCard': 10},
    109: {'playerTotal': 14, 'dealerCard': 11},
    110: {'playerTotal': 15, 'dealerCard': 2},
    111: {'playerTotal': 15, 'dealerCard': 3},
    112: {'playerTotal': 15, 'dealerCard': 4},
    113: {'playerTotal': 15, 'dealerCard': 5},
    114: {'playerTotal': 15, 'dealerCard': 6},
    115: {'playerTotal': 15, 'dealerCard': 7},
    116: {'playerTotal': 15, 'dealerCard': 8},
    117: {'playerTotal': 15, 'dealerCard': 9},
    118: {'playerTotal': 15, 'dealerCard': 10},
    119: {'playerTotal': 15, 'dealerCard': 11},
    120: {'playerTotal': 16, 'dealerCard': 2},
    121: {'playerTotal': 16, 'dealerCard': 3},
    122: {'playerTotal': 16, 'dealerCard': 4},
    123: {'playerTotal': 16, 'dealerCard': 5},
    124: {'playerTotal': 16, 'dealerCard': 6},
    125: {'playerTotal': 16, 'dealerCard': 7},
    126: {'playerTotal': 16, 'dealerCard': 8},
    127: {'playerTotal': 16, 'dealerCard': 9},
    128: {'playerTotal': 16, 'dealerCard': 10},
    129: {'playerTotal': 16, 'dealerCard': 11},
    130: {'playerTotal': 17, 'dealerCard': 2},
    131: {'playerTotal': 17, 'dealerCard': 3},
    132: {'playerTotal': 17, 'dealerCard': 4},
    133: {'playerTotal': 17, 'dealerCard': 5},
    134: {'playerTotal': 17, 'dealerCard': 6},
    135: {'playerTotal': 17, 'dealerCard': 7},
    136: {'playerTotal': 17, 'dealerCard': 8},
    137: {'playerTotal': 17, 'dealerCard': 9},
    138: {'playerTotal': 17, 'dealerCard': 10},
    139: {'playerTotal': 17, 'dealerCard': 11},
    140: {'playerTotal': 18, 'dealerCard': 2},
    141: {'playerTotal': 18, 'dealerCard': 3},
    142: {'playerTotal': 18, 'dealerCard': 4},
    143: {'playerTotal': 18, 'dealerCard': 5},
    144: {'playerTotal': 18, 'dealerCard': 6},
    145: {'playerTotal': 18, 'dealerCard': 7},
    146: {'playerTotal': 18, 'dealerCard': 8},
    147: {'playerTotal': 18, 'dealerCard': 9},
    148: {'playerTotal': 18, 'dealerCard': 10},
    149: {'playerTotal': 18, 'dealerCard': 11},
    150: {'playerTotal': 19, 'dealerCard': 2},
    151: {'playerTotal': 19, 'dealerCard': 3},
    152: {'playerTotal': 19, 'dealerCard': 4},
    153: {'playerTotal': 19, 'dealerCard': 5},
    154: {'playerTotal': 19, 'dealerCard': 6},
    155: {'playerTotal': 19, 'dealerCard': 7},
    156: {'playerTotal': 19, 'dealerCard': 8},
    157: {'playerTotal': 19, 'dealerCard': 9},
    158: {'playerTotal': 19, 'dealerCard': 10},
    159: {'playerTotal': 19, 'dealerCard': 11},
    160: {'playerTotal': 20, 'dealerCard': 2},
    161: {'playerTotal': 20, 'dealerCard': 3},
    162: {'playerTotal': 20, 'dealerCard': 4},
    163: {'playerTotal': 20, 'dealerCard': 5},
    164: {'playerTotal': 20, 'dealerCard': 6},
    165: {'playerTotal': 20, 'dealerCard': 7},
    166: {'playerTotal': 20, 'dealerCard': 8},
    167: {'playerTotal': 20, 'dealerCard': 9},
    168: {'playerTotal': 20, 'dealerCard': 10},
    169: {'playerTotal': 20, 'dealerCard': 11}
    }
    scenarioIDToScenarioWithAce = {
    170: {"playerTotal": 13, "dealerCard": 2},
    171: {"playerTotal": 13, "dealerCard": 3},
    172: {"playerTotal": 13, "dealerCard": 4},
    173: {"playerTotal": 13, "dealerCard": 5},
    174: {"playerTotal": 13, "dealerCard": 6},
    175: {"playerTotal": 13, "dealerCard": 7},
    176: {"playerTotal": 13, "dealerCard": 8},
    177: {"playerTotal": 13, "dealerCard": 9},
    178: {"playerTotal": 13, "dealerCard": 10},
    179: {"playerTotal": 13, "dealerCard": 11},
    180: {"playerTotal": 14, "dealerCard": 2},
    181: {"playerTotal": 14, "dealerCard": 3},
    182: {"playerTotal": 14, "dealerCard": 4},
    183: {"playerTotal": 14, "dealerCard": 5},
    184: {"playerTotal": 14, "dealerCard": 6},
    185: {"playerTotal": 14, "dealerCard": 7},
    186: {"playerTotal": 14, "dealerCard": 8},
    187: {"playerTotal": 14, "dealerCard": 9},
    188: {"playerTotal": 14, "dealerCard": 10},
    189: {"playerTotal": 14, "dealerCard": 11},
    190: {"playerTotal": 15, "dealerCard": 2},
    191: {"playerTotal": 15, "dealerCard": 3},
    192: {"playerTotal": 15, "dealerCard": 4},
    193: {"playerTotal": 15, "dealerCard": 5},
    194: {"playerTotal": 15, "dealerCard": 6},
    195: {"playerTotal": 15, "dealerCard": 7},
    196: {"playerTotal": 15, "dealerCard": 8},
    197: {"playerTotal": 15, "dealerCard": 9},
    198: {"playerTotal": 15, "dealerCard": 10},
    199: {"playerTotal": 15, "dealerCard": 11},
    200: {"playerTotal": 16, "dealerCard": 2},
    201: {"playerTotal": 16, "dealerCard": 3},
    202: {"playerTotal": 16, "dealerCard": 4},
    203: {"playerTotal": 16, "dealerCard": 5},
    204: {"playerTotal": 16, "dealerCard": 6},
    205: {"playerTotal": 16, "dealerCard": 7},
    206: {"playerTotal": 16, "dealerCard": 8},
    207: {"playerTotal": 16, "dealerCard": 9},
    208: {"playerTotal": 16, "dealerCard": 10},
    209: {"playerTotal": 16, "dealerCard": 11},
    210: {"playerTotal": 17, "dealerCard": 2},
    211: {"playerTotal": 17, "dealerCard": 3},
    212: {"playerTotal": 17,"dealerCard": 4},
    213: {"playerTotal": 17,"dealerCard": 5},
    214: {"playerTotal": 17, "dealerCard": 6},
    215: {"playerTotal": 17, "dealerCard": 7},
    216: {"playerTotal": 17, "dealerCard": 8},
    217: {"playerTotal": 17, "dealerCard": 9},
    218: {"playerTotal": 17, "dealerCard": 10},
    219: {"playerTotal": 17, "dealerCard": 11},
    220: {"playerTotal": 18, "dealerCard": 2},
    221: {"playerTotal": 18, "dealerCard": 3},
    222: {"playerTotal": 18, "dealerCard": 4},
    223: {"playerTotal": 18, "dealerCard": 5},
    224: {"playerTotal": 18, "dealerCard": 6},
    225: {"playerTotal": 18, "dealerCard": 7},
    226: {"playerTotal": 18, "dealerCard": 8},
    227: {"playerTotal": 18, "dealerCard": 9},
    228: {"playerTotal": 18, "dealerCard": 10},
    229: {"playerTotal": 18, "dealerCard": 11},
    230: {"playerTotal": 19, "dealerCard": 2},
    231: {"playerTotal": 19, "dealerCard": 3},
    232: {"playerTotal": 19, "dealerCard": 4},
    233: {"playerTotal": 19, "dealerCard": 5},
    234: {"playerTotal": 19, "dealerCard": 6},
    235: {"playerTotal": 19, "dealerCard": 7},
    236: {"playerTotal": 19, "dealerCard": 8},
    237: {"playerTotal": 19, "dealerCard": 9},
    238: {"playerTotal": 19, "dealerCard": 10},
    239: {"playerTotal": 19, "dealerCard": 11},
    240: {"playerTotal": 20, "dealerCard": 2},
    241: {"playerTotal": 20, "dealerCard": 3},
    242: {"playerTotal": 20, "dealerCard": 4},
    243: {"playerTotal": 20, "dealerCard": 5},
    244: {"playerTotal": 20, "dealerCard": 6},
    245: {"playerTotal": 20, "dealerCard": 7},
    246: {"playerTotal": 20, "dealerCard": 8},
    247: {"playerTotal": 20, "dealerCard": 9},
    248: {"playerTotal": 20,"dealerCard": 10},
    249: {"playerTotal": 20, "dealerCard": 11}
}
    scenarioList = []
    for i in range (249):
        scenarioList.append(random.randint(0,1))
    card = 0
    secCard = 0
    playerAceCount = 0
    dealerAceCount = 0
    for i in range(2): 
        currentCard = giveCard(cards)
        if currentCard == 11:
            playerAceCount += 1
        playerTotal += currentCard
    for i in range(2):
        currentCard = giveCard(cards)
        if currentCard == 11:
            dealerAceCount += 1
        if i == 1:
            dealerCard += giveCard(cards)
        else:
            secCard = giveCard(cards)
    if playerAceCount == 0:
        return getIndex(scenarioIDToScenarioNoAce, playerTotal, dealerCard)
    else:
        return getIndex(scenarioIDToScenarioWithAce, playerTotal, dealerCard)
    



def giveCard(list):
    card = list.pop(random.randint(1,len(list)-1))
    return card

def getIndex(dict, playerTotal, dealerCard):
    index = 0
    for i in range(len(dict)):
      if playerTotal == dict[i]["playerTotal"]:
        if dealerCard == dict[i]["dealerCard"]:
          return index


def fitnessFunction(individual):
    choice = individual[153]
    


print(playGame())





#make black jack environment with deck and rules and everything
#with initialized game, have to go through each key and value in dictionary to find index
# use index to find 1 or 0, and then simulate said action with if statement!!!!!