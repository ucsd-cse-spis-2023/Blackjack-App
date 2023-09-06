#import libraries
import random

from deap import base
from deap import creator
from deap import tools


# class Game:
#     cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
#     scenarioIDToScenarioNoAce = {
#         0: {'playerTotal': 4, 'dealerCard': 2},
#         1: {'playerTotal': 4, 'dealerCard': 3},
#         2: {'playerTotal': 4, 'dealerCard': 4},
#         3: {'playerTotal': 4, 'dealerCard': 5},
#         4: {'playerTotal': 4, 'dealerCard': 6},
#         5: {'playerTotal': 4, 'dealerCard': 7},
#         6: {'playerTotal': 4, 'dealerCard': 8},
#         7: {'playerTotal': 4, 'dealerCard': 9},
#         8: {'playerTotal': 4, 'dealerCard': 10},
#         9: {'playerTotal': 4, 'dealerCard': 11},
#         10: {'playerTotal': 5, 'dealerCard': 2},
#         11: {'playerTotal': 5, 'dealerCard': 3},
#         12: {'playerTotal': 5, 'dealerCard': 4},
#         13: {'playerTotal': 5, 'dealerCard': 5},
#         14: {'playerTotal': 5, 'dealerCard': 6},
#         15: {'playerTotal': 5, 'dealerCard': 7},
#         16: {'playerTotal': 5, 'dealerCard': 8},
#         17: {'playerTotal': 5, 'dealerCard': 9},
#         18: {'playerTotal': 5, 'dealerCard': 10},
#         19: {'playerTotal': 5, 'dealerCard': 11},
#         20: {'playerTotal': 6, 'dealerCard': 2},
#         21: {'playerTotal': 6, 'dealerCard': 3},
#         22: {'playerTotal': 6, 'dealerCard': 4},
#         23: {'playerTotal': 6, 'dealerCard': 5},
#         24: {'playerTotal': 6, 'dealerCard': 6},
#         25: {'playerTotal': 6, 'dealerCard': 7},
#         26: {'playerTotal': 6, 'dealerCard': 8},
#         27: {'playerTotal': 6, 'dealerCard': 9},
#         28: {'playerTotal': 6, 'dealerCard': 10},
#         29: {'playerTotal': 6, 'dealerCard': 11},
#         30: {'playerTotal': 7, 'dealerCard': 2},
#         31: {'playerTotal': 7, 'dealerCard': 3},
#         32: {'playerTotal': 7, 'dealerCard': 4},
#         33: {'playerTotal': 7, 'dealerCard': 5},
#         34: {'playerTotal': 7, 'dealerCard': 6},
#         35: {'playerTotal': 7, 'dealerCard': 7},
#         36: {'playerTotal': 7, 'dealerCard': 8},
#         37: {'playerTotal': 7, 'dealerCard': 9},
#         38: {'playerTotal': 7, 'dealerCard': 10},
#         39: {'playerTotal': 7, 'dealerCard': 11},
#         40: {'playerTotal': 8, 'dealerCard': 2},
#         41: {'playerTotal': 8, 'dealerCard': 3},
#         42: {'playerTotal': 8, 'dealerCard': 4},
#         43: {'playerTotal': 8, 'dealerCard': 5},
#         44: {'playerTotal': 8, 'dealerCard': 6},
#         45: {'playerTotal': 8, 'dealerCard': 7},
#         46: {'playerTotal': 8, 'dealerCard': 8},
#         47: {'playerTotal': 8, 'dealerCard': 9},
#         48: {'playerTotal': 8, 'dealerCard': 10},
#         49: {'playerTotal': 8, 'dealerCard': 11},
#         50: {'playerTotal': 9, 'dealerCard': 2},
#         51: {'playerTotal': 9, 'dealerCard': 3},
#         52: {'playerTotal': 9, 'dealerCard': 4},
#         53: {'playerTotal': 9, 'dealerCard': 5},
#         54: {'playerTotal': 9, 'dealerCard': 6},
#         55: {'playerTotal': 9, 'dealerCard': 7},
#         56: {'playerTotal': 9, 'dealerCard': 8},
#         57: {'playerTotal': 9, 'dealerCard': 9},
#         58: {'playerTotal': 9, 'dealerCard': 10},
#         59: {'playerTotal': 9, 'dealerCard': 11},
#         60: {'playerTotal': 10, 'dealerCard': 2},
#         61: {'playerTotal': 10, 'dealerCard': 3},
#         62: {'playerTotal': 10, 'dealerCard': 4},
#         63: {'playerTotal': 10, 'dealerCard': 5},
#         64: {'playerTotal': 10, 'dealerCard': 6},
#         65: {'playerTotal': 10, 'dealerCard': 7},
#         66: {'playerTotal': 10, 'dealerCard': 8},
#         67: {'playerTotal': 10, 'dealerCard': 9},
#         68: {'playerTotal': 10, 'dealerCard': 10},
#         69: {'playerTotal': 10, 'dealerCard': 11},
#         70: {'playerTotal': 11, 'dealerCard': 2},
#         71: {'playerTotal': 11, 'dealerCard': 3},
#         72: {'playerTotal': 11, 'dealerCard': 4},
#         73: {'playerTotal': 11, 'dealerCard': 5},
#         74: {'playerTotal': 11, 'dealerCard': 6},
#         75: {'playerTotal': 11, 'dealerCard': 7},
#         76: {'playerTotal': 11, 'dealerCard': 8},
#         77: {'playerTotal': 11, 'dealerCard': 9},
#         78: {'playerTotal': 11, 'dealerCard': 10},
#         79: {'playerTotal': 11, 'dealerCard': 11},
#         80: {'playerTotal': 12, 'dealerCard': 2},
#         81: {'playerTotal': 12, 'dealerCard': 3},
#         82: {'playerTotal': 12, 'dealerCard': 4},
#         83: {'playerTotal': 12, 'dealerCard': 5},
#         84: {'playerTotal': 12, 'dealerCard': 6},
#         85: {'playerTotal': 12, 'dealerCard': 7},
#         86: {'playerTotal': 12, 'dealerCard': 8},
#         87: {'playerTotal': 12, 'dealerCard': 9},
#         88: {'playerTotal': 12, 'dealerCard': 10},
#         89: {'playerTotal': 12, 'dealerCard': 11},
#         90: {'playerTotal': 13, 'dealerCard': 2},
#         91: {'playerTotal': 13, 'dealerCard': 3},
#         92: {'playerTotal': 13, 'dealerCard': 4},
#         93: {'playerTotal': 13, 'dealerCard': 5},
#         94: {'playerTotal': 13, 'dealerCard': 6},
#         95: {'playerTotal': 13, 'dealerCard': 7},
#         96: {'playerTotal': 13, 'dealerCard': 8},
#         97: {'playerTotal': 13, 'dealerCard': 9},
#         98: {'playerTotal': 13, 'dealerCard': 10},
#         99: {'playerTotal': 13, 'dealerCard': 11},
#         100: {'playerTotal': 14, 'dealerCard': 2},
#         101: {'playerTotal': 14, 'dealerCard': 3},
#         102: {'playerTotal': 14, 'dealerCard': 4},
#         103: {'playerTotal': 14, 'dealerCard': 5},
#         104: {'playerTotal': 14, 'dealerCard': 6},
#         105: {'playerTotal': 14, 'dealerCard': 7},
#         106: {'playerTotal': 14, 'dealerCard': 8},
#         107: {'playerTotal': 14, 'dealerCard': 9},
#         108: {'playerTotal': 14, 'dealerCard': 10},
#         109: {'playerTotal': 14, 'dealerCard': 11},
#         110: {'playerTotal': 15, 'dealerCard': 2},
#         111: {'playerTotal': 15, 'dealerCard': 3},
#         112: {'playerTotal': 15, 'dealerCard': 4},
#         113: {'playerTotal': 15, 'dealerCard': 5},
#         114: {'playerTotal': 15, 'dealerCard': 6},
#         115: {'playerTotal': 15, 'dealerCard': 7},
#         116: {'playerTotal': 15, 'dealerCard': 8},
#         117: {'playerTotal': 15, 'dealerCard': 9},
#         118: {'playerTotal': 15, 'dealerCard': 10},
#         119: {'playerTotal': 15, 'dealerCard': 11},
#         120: {'playerTotal': 16, 'dealerCard': 2},
#         121: {'playerTotal': 16, 'dealerCard': 3},
#         122: {'playerTotal': 16, 'dealerCard': 4},
#         123: {'playerTotal': 16, 'dealerCard': 5},
#         124: {'playerTotal': 16, 'dealerCard': 6},
#         125: {'playerTotal': 16, 'dealerCard': 7},
#         126: {'playerTotal': 16, 'dealerCard': 8},
#         127: {'playerTotal': 16, 'dealerCard': 9},
#         128: {'playerTotal': 16, 'dealerCard': 10},
#         129: {'playerTotal': 16, 'dealerCard': 11},
#         130: {'playerTotal': 17, 'dealerCard': 2},
#         131: {'playerTotal': 17, 'dealerCard': 3},
#         132: {'playerTotal': 17, 'dealerCard': 4},
#         133: {'playerTotal': 17, 'dealerCard': 5},
#         134: {'playerTotal': 17, 'dealerCard': 6},
#         135: {'playerTotal': 17, 'dealerCard': 7},
#         136: {'playerTotal': 17, 'dealerCard': 8},
#         137: {'playerTotal': 17, 'dealerCard': 9},
#         138: {'playerTotal': 17, 'dealerCard': 10},
#         139: {'playerTotal': 17, 'dealerCard': 11},
#         140: {'playerTotal': 18, 'dealerCard': 2},
#         141: {'playerTotal': 18, 'dealerCard': 3},
#         142: {'playerTotal': 18, 'dealerCard': 4},
#         143: {'playerTotal': 18, 'dealerCard': 5},
#         144: {'playerTotal': 18, 'dealerCard': 6},
#         145: {'playerTotal': 18, 'dealerCard': 7},
#         146: {'playerTotal': 18, 'dealerCard': 8},
#         147: {'playerTotal': 18, 'dealerCard': 9},
#         148: {'playerTotal': 18, 'dealerCard': 10},
#         149: {'playerTotal': 18, 'dealerCard': 11},
#         150: {'playerTotal': 19, 'dealerCard': 2},
#         151: {'playerTotal': 19, 'dealerCard': 3},
#         152: {'playerTotal': 19, 'dealerCard': 4},
#         153: {'playerTotal': 19, 'dealerCard': 5},
#         154: {'playerTotal': 19, 'dealerCard': 6},
#         155: {'playerTotal': 19, 'dealerCard': 7},
#         156: {'playerTotal': 19, 'dealerCard': 8},
#         157: {'playerTotal': 19, 'dealerCard': 9},
#         158: {'playerTotal': 19, 'dealerCard': 10},
#         159: {'playerTotal': 19, 'dealerCard': 11},
#         160: {'playerTotal': 20, 'dealerCard': 2},
#         161: {'playerTotal': 20, 'dealerCard': 3},
#         162: {'playerTotal': 20, 'dealerCard': 4},
#         163: {'playerTotal': 20, 'dealerCard': 5},
#         164: {'playerTotal': 20, 'dealerCard': 6},
#         165: {'playerTotal': 20, 'dealerCard': 7},
#         166: {'playerTotal': 20, 'dealerCard': 8},
#         167: {'playerTotal': 20, 'dealerCard': 9},
#         168: {'playerTotal': 20, 'dealerCard': 10},
#         169: {'playerTotal': 20, 'dealerCard': 11}
#         }
#     scenarioIDToScenarioWithAce = {
#         170: {"playerTotal": 13, "dealerCard": 2},
#         171: {"playerTotal": 13, "dealerCard": 3},
#         172: {"playerTotal": 13, "dealerCard": 4},
#         173: {"playerTotal": 13, "dealerCard": 5},
#         174: {"playerTotal": 13, "dealerCard": 6},
#         175: {"playerTotal": 13, "dealerCard": 7},
#         176: {"playerTotal": 13, "dealerCard": 8},
#         177: {"playerTotal": 13, "dealerCard": 9},
#         178: {"playerTotal": 13, "dealerCard": 10},
#         179: {"playerTotal": 13, "dealerCard": 11},
#         180: {"playerTotal": 14, "dealerCard": 2},
#         181: {"playerTotal": 14, "dealerCard": 3},
#         182: {"playerTotal": 14, "dealerCard": 4},
#         183: {"playerTotal": 14, "dealerCard": 5},
#         184: {"playerTotal": 14, "dealerCard": 6},
#         185: {"playerTotal": 14, "dealerCard": 7},
#         186: {"playerTotal": 14, "dealerCard": 8},
#         187: {"playerTotal": 14, "dealerCard": 9},
#         188: {"playerTotal": 14, "dealerCard": 10},
#         189: {"playerTotal": 14, "dealerCard": 11},
#         190: {"playerTotal": 15, "dealerCard": 2},
#         191: {"playerTotal": 15, "dealerCard": 3},
#         192: {"playerTotal": 15, "dealerCard": 4},
#         193: {"playerTotal": 15, "dealerCard": 5},
#         194: {"playerTotal": 15, "dealerCard": 6},
#         195: {"playerTotal": 15, "dealerCard": 7},
#         196: {"playerTotal": 15, "dealerCard": 8},
#         197: {"playerTotal": 15, "dealerCard": 9},
#         198: {"playerTotal": 15, "dealerCard": 10},
#         199: {"playerTotal": 15, "dealerCard": 11},
#         200: {"playerTotal": 16, "dealerCard": 2},
#         201: {"playerTotal": 16, "dealerCard": 3},
#         202: {"playerTotal": 16, "dealerCard": 4},
#         203: {"playerTotal": 16, "dealerCard": 5},
#         204: {"playerTotal": 16, "dealerCard": 6},
#         205: {"playerTotal": 16, "dealerCard": 7},
#         206: {"playerTotal": 16, "dealerCard": 8},
#         207: {"playerTotal": 16, "dealerCard": 9},
#         208: {"playerTotal": 16, "dealerCard": 10},
#         209: {"playerTotal": 16, "dealerCard": 11},
#         210: {"playerTotal": 17, "dealerCard": 2},
#         211: {"playerTotal": 17, "dealerCard": 3},
#         212: {"playerTotal": 17,"dealerCard": 4},
#         213: {"playerTotal": 17,"dealerCard": 5},
#         214: {"playerTotal": 17, "dealerCard": 6},
#         215: {"playerTotal": 17, "dealerCard": 7},
#         216: {"playerTotal": 17, "dealerCard": 8},
#         217: {"playerTotal": 17, "dealerCard": 9},
#         218: {"playerTotal": 17, "dealerCard": 10},
#         219: {"playerTotal": 17, "dealerCard": 11},
#         220: {"playerTotal": 18, "dealerCard": 2},
#         221: {"playerTotal": 18, "dealerCard": 3},
#         222: {"playerTotal": 18, "dealerCard": 4},
#         223: {"playerTotal": 18, "dealerCard": 5},
#         224: {"playerTotal": 18, "dealerCard": 6},
#         225: {"playerTotal": 18, "dealerCard": 7},
#         226: {"playerTotal": 18, "dealerCard": 8},
#         227: {"playerTotal": 18, "dealerCard": 9},
#         228: {"playerTotal": 18, "dealerCard": 10},
#         229: {"playerTotal": 18, "dealerCard": 11},
#         230: {"playerTotal": 19, "dealerCard": 2},
#         231: {"playerTotal": 19, "dealerCard": 3},
#         232: {"playerTotal": 19, "dealerCard": 4},
#         233: {"playerTotal": 19, "dealerCard": 5},
#         234: {"playerTotal": 19, "dealerCard": 6},
#         235: {"playerTotal": 19, "dealerCard": 7},
#         236: {"playerTotal": 19, "dealerCard": 8},
#         237: {"playerTotal": 19, "dealerCard": 9},
#         238: {"playerTotal": 19, "dealerCard": 10},
#         239: {"playerTotal": 19, "dealerCard": 11},
#         240: {"playerTotal": 20, "dealerCard": 2},
#         241: {"playerTotal": 20, "dealerCard": 3},
#         242: {"playerTotal": 20, "dealerCard": 4},
#         243: {"playerTotal": 20, "dealerCard": 5},
#         244: {"playerTotal": 20, "dealerCard": 6},
#         245: {"playerTotal": 20, "dealerCard": 7},
#         246: {"playerTotal": 20, "dealerCard": 8},
#         247: {"playerTotal": 20, "dealerCard": 9},
#         248: {"playerTotal": 20,"dealerCard": 10},
#         249: {"playerTotal": 20, "dealerCard": 11}
#     }
#     def __init__(self):
#         self.total = 0
#         self.dealerCard = 0
#         self.aceCount = 0

#     def giveCard(self, cards):
#         card = cards.pop(random.randint(1,len(cards)-1))
#         #print(card)
#         self.total += card
#         if card == 11:
#             self.aceCount += 1
#         return card

# player = Game()
# dealer = Game()
# dealerCard = 0 #only keep track of this for dealer

# def playGame(scenarioList):
#     global dealerCard
# #     global cards, playerAceCount, dealerAceCount, scenarioList, secCard, playerTotal, dealerCard, scenarioIDToScenarioNoAce, scenarioIDToScenarioWithAce, card, player, dealerTotal
# #     player = True
# #     cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
# #     playerTotal = 0
# #     dealerCard = 0
# #     dealerTotal = 0
# #     scenarioIDToScenarioNoAce = {
# #     0: {'playerTotal': 4, 'dealerCard': 2},
# #     1: {'playerTotal': 4, 'dealerCard': 3},
# #     2: {'playerTotal': 4, 'dealerCard': 4},
# #     3: {'playerTotal': 4, 'dealerCard': 5},
# #     4: {'playerTotal': 4, 'dealerCard': 6},
# #     5: {'playerTotal': 4, 'dealerCard': 7},
# #     6: {'playerTotal': 4, 'dealerCard': 8},
# #     7: {'playerTotal': 4, 'dealerCard': 9},
# #     8: {'playerTotal': 4, 'dealerCard': 10},
# #     9: {'playerTotal': 4, 'dealerCard': 11},
# #     10: {'playerTotal': 5, 'dealerCard': 2},
# #     11: {'playerTotal': 5, 'dealerCard': 3},
# #     12: {'playerTotal': 5, 'dealerCard': 4},
# #     13: {'playerTotal': 5, 'dealerCard': 5},
# #     14: {'playerTotal': 5, 'dealerCard': 6},
# #     15: {'playerTotal': 5, 'dealerCard': 7},
# #     16: {'playerTotal': 5, 'dealerCard': 8},
# #     17: {'playerTotal': 5, 'dealerCard': 9},
# #     18: {'playerTotal': 5, 'dealerCard': 10},
# #     19: {'playerTotal': 5, 'dealerCard': 11},
# #     20: {'playerTotal': 6, 'dealerCard': 2},
# #     21: {'playerTotal': 6, 'dealerCard': 3},
# #     22: {'playerTotal': 6, 'dealerCard': 4},
# #     23: {'playerTotal': 6, 'dealerCard': 5},
# #     24: {'playerTotal': 6, 'dealerCard': 6},
# #     25: {'playerTotal': 6, 'dealerCard': 7},
# #     26: {'playerTotal': 6, 'dealerCard': 8},
# #     27: {'playerTotal': 6, 'dealerCard': 9},
# #     28: {'playerTotal': 6, 'dealerCard': 10},
# #     29: {'playerTotal': 6, 'dealerCard': 11},
# #     30: {'playerTotal': 7, 'dealerCard': 2},
# #     31: {'playerTotal': 7, 'dealerCard': 3},
# #     32: {'playerTotal': 7, 'dealerCard': 4},
# #     33: {'playerTotal': 7, 'dealerCard': 5},
# #     34: {'playerTotal': 7, 'dealerCard': 6},
# #     35: {'playerTotal': 7, 'dealerCard': 7},
# #     36: {'playerTotal': 7, 'dealerCard': 8},
# #     37: {'playerTotal': 7, 'dealerCard': 9},
# #     38: {'playerTotal': 7, 'dealerCard': 10},
# #     39: {'playerTotal': 7, 'dealerCard': 11},
# #     40: {'playerTotal': 8, 'dealerCard': 2},
# #     41: {'playerTotal': 8, 'dealerCard': 3},
# #     42: {'playerTotal': 8, 'dealerCard': 4},
# #     43: {'playerTotal': 8, 'dealerCard': 5},
# #     44: {'playerTotal': 8, 'dealerCard': 6},
# #     45: {'playerTotal': 8, 'dealerCard': 7},
# #     46: {'playerTotal': 8, 'dealerCard': 8},
# #     47: {'playerTotal': 8, 'dealerCard': 9},
# #     48: {'playerTotal': 8, 'dealerCard': 10},
# #     49: {'playerTotal': 8, 'dealerCard': 11},
# #     50: {'playerTotal': 9, 'dealerCard': 2},
# #     51: {'playerTotal': 9, 'dealerCard': 3},
# #     52: {'playerTotal': 9, 'dealerCard': 4},
# #     53: {'playerTotal': 9, 'dealerCard': 5},
# #     54: {'playerTotal': 9, 'dealerCard': 6},
# #     55: {'playerTotal': 9, 'dealerCard': 7},
# #     56: {'playerTotal': 9, 'dealerCard': 8},
# #     57: {'playerTotal': 9, 'dealerCard': 9},
# #     58: {'playerTotal': 9, 'dealerCard': 10},
# #     59: {'playerTotal': 9, 'dealerCard': 11},
# #     60: {'playerTotal': 10, 'dealerCard': 2},
# #     61: {'playerTotal': 10, 'dealerCard': 3},
# #     62: {'playerTotal': 10, 'dealerCard': 4},
# #     63: {'playerTotal': 10, 'dealerCard': 5},
# #     64: {'playerTotal': 10, 'dealerCard': 6},
# #     65: {'playerTotal': 10, 'dealerCard': 7},
# #     66: {'playerTotal': 10, 'dealerCard': 8},
# #     67: {'playerTotal': 10, 'dealerCard': 9},
# #     68: {'playerTotal': 10, 'dealerCard': 10},
# #     69: {'playerTotal': 10, 'dealerCard': 11},
# #     70: {'playerTotal': 11, 'dealerCard': 2},
# #     71: {'playerTotal': 11, 'dealerCard': 3},
# #     72: {'playerTotal': 11, 'dealerCard': 4},
# #     73: {'playerTotal': 11, 'dealerCard': 5},
# #     74: {'playerTotal': 11, 'dealerCard': 6},
# #     75: {'playerTotal': 11, 'dealerCard': 7},
# #     76: {'playerTotal': 11, 'dealerCard': 8},
# #     77: {'playerTotal': 11, 'dealerCard': 9},
# #     78: {'playerTotal': 11, 'dealerCard': 10},
# #     79: {'playerTotal': 11, 'dealerCard': 11},
# #     80: {'playerTotal': 12, 'dealerCard': 2},
# #     81: {'playerTotal': 12, 'dealerCard': 3},
# #     82: {'playerTotal': 12, 'dealerCard': 4},
# #     83: {'playerTotal': 12, 'dealerCard': 5},
# #     84: {'playerTotal': 12, 'dealerCard': 6},
# #     85: {'playerTotal': 12, 'dealerCard': 7},
# #     86: {'playerTotal': 12, 'dealerCard': 8},
# #     87: {'playerTotal': 12, 'dealerCard': 9},
# #     88: {'playerTotal': 12, 'dealerCard': 10},
# #     89: {'playerTotal': 12, 'dealerCard': 11},
# #     90: {'playerTotal': 13, 'dealerCard': 2},
# #     91: {'playerTotal': 13, 'dealerCard': 3},
# #     92: {'playerTotal': 13, 'dealerCard': 4},
# #     93: {'playerTotal': 13, 'dealerCard': 5},
# #     94: {'playerTotal': 13, 'dealerCard': 6},
# #     95: {'playerTotal': 13, 'dealerCard': 7},
# #     96: {'playerTotal': 13, 'dealerCard': 8},
# #     97: {'playerTotal': 13, 'dealerCard': 9},
# #     98: {'playerTotal': 13, 'dealerCard': 10},
# #     99: {'playerTotal': 13, 'dealerCard': 11},
# #     100: {'playerTotal': 14, 'dealerCard': 2},
# #     101: {'playerTotal': 14, 'dealerCard': 3},
# #     102: {'playerTotal': 14, 'dealerCard': 4},
# #     103: {'playerTotal': 14, 'dealerCard': 5},
# #     104: {'playerTotal': 14, 'dealerCard': 6},
# #     105: {'playerTotal': 14, 'dealerCard': 7},
# #     106: {'playerTotal': 14, 'dealerCard': 8},
# #     107: {'playerTotal': 14, 'dealerCard': 9},
# #     108: {'playerTotal': 14, 'dealerCard': 10},
# #     109: {'playerTotal': 14, 'dealerCard': 11},
# #     110: {'playerTotal': 15, 'dealerCard': 2},
# #     111: {'playerTotal': 15, 'dealerCard': 3},
# #     112: {'playerTotal': 15, 'dealerCard': 4},
# #     113: {'playerTotal': 15, 'dealerCard': 5},
# #     114: {'playerTotal': 15, 'dealerCard': 6},
# #     115: {'playerTotal': 15, 'dealerCard': 7},
# #     116: {'playerTotal': 15, 'dealerCard': 8},
# #     117: {'playerTotal': 15, 'dealerCard': 9},
# #     118: {'playerTotal': 15, 'dealerCard': 10},
# #     119: {'playerTotal': 15, 'dealerCard': 11},
# #     120: {'playerTotal': 16, 'dealerCard': 2},
# #     121: {'playerTotal': 16, 'dealerCard': 3},
# #     122: {'playerTotal': 16, 'dealerCard': 4},
# #     123: {'playerTotal': 16, 'dealerCard': 5},
# #     124: {'playerTotal': 16, 'dealerCard': 6},
# #     125: {'playerTotal': 16, 'dealerCard': 7},
# #     126: {'playerTotal': 16, 'dealerCard': 8},
# #     127: {'playerTotal': 16, 'dealerCard': 9},
# #     128: {'playerTotal': 16, 'dealerCard': 10},
# #     129: {'playerTotal': 16, 'dealerCard': 11},
# #     130: {'playerTotal': 17, 'dealerCard': 2},
# #     131: {'playerTotal': 17, 'dealerCard': 3},
# #     132: {'playerTotal': 17, 'dealerCard': 4},
# #     133: {'playerTotal': 17, 'dealerCard': 5},
# #     134: {'playerTotal': 17, 'dealerCard': 6},
# #     135: {'playerTotal': 17, 'dealerCard': 7},
# #     136: {'playerTotal': 17, 'dealerCard': 8},
# #     137: {'playerTotal': 17, 'dealerCard': 9},
# #     138: {'playerTotal': 17, 'dealerCard': 10},
# #     139: {'playerTotal': 17, 'dealerCard': 11},
# #     140: {'playerTotal': 18, 'dealerCard': 2},
# #     141: {'playerTotal': 18, 'dealerCard': 3},
# #     142: {'playerTotal': 18, 'dealerCard': 4},
# #     143: {'playerTotal': 18, 'dealerCard': 5},
# #     144: {'playerTotal': 18, 'dealerCard': 6},
# #     145: {'playerTotal': 18, 'dealerCard': 7},
# #     146: {'playerTotal': 18, 'dealerCard': 8},
# #     147: {'playerTotal': 18, 'dealerCard': 9},
# #     148: {'playerTotal': 18, 'dealerCard': 10},
# #     149: {'playerTotal': 18, 'dealerCard': 11},
# #     150: {'playerTotal': 19, 'dealerCard': 2},
# #     151: {'playerTotal': 19, 'dealerCard': 3},
# #     152: {'playerTotal': 19, 'dealerCard': 4},
# #     153: {'playerTotal': 19, 'dealerCard': 5},
# #     154: {'playerTotal': 19, 'dealerCard': 6},
# #     155: {'playerTotal': 19, 'dealerCard': 7},
# #     156: {'playerTotal': 19, 'dealerCard': 8},
# #     157: {'playerTotal': 19, 'dealerCard': 9},
# #     158: {'playerTotal': 19, 'dealerCard': 10},
# #     159: {'playerTotal': 19, 'dealerCard': 11},
# #     160: {'playerTotal': 20, 'dealerCard': 2},
# #     161: {'playerTotal': 20, 'dealerCard': 3},
# #     162: {'playerTotal': 20, 'dealerCard': 4},
# #     163: {'playerTotal': 20, 'dealerCard': 5},
# #     164: {'playerTotal': 20, 'dealerCard': 6},
# #     165: {'playerTotal': 20, 'dealerCard': 7},
# #     166: {'playerTotal': 20, 'dealerCard': 8},
# #     167: {'playerTotal': 20, 'dealerCard': 9},
# #     168: {'playerTotal': 20, 'dealerCard': 10},
# #     169: {'playerTotal': 20, 'dealerCard': 11}
# #     }
# #     scenarioIDToScenarioWithAce = {
# #     170: {"playerTotal": 13, "dealerCard": 2},
# #     171: {"playerTotal": 13, "dealerCard": 3},
# #     172: {"playerTotal": 13, "dealerCard": 4},
# #     173: {"playerTotal": 13, "dealerCard": 5},
# #     174: {"playerTotal": 13, "dealerCard": 6},
# #     175: {"playerTotal": 13, "dealerCard": 7},
# #     176: {"playerTotal": 13, "dealerCard": 8},
# #     177: {"playerTotal": 13, "dealerCard": 9},
# #     178: {"playerTotal": 13, "dealerCard": 10},
# #     179: {"playerTotal": 13, "dealerCard": 11},
# #     180: {"playerTotal": 14, "dealerCard": 2},
# #     181: {"playerTotal": 14, "dealerCard": 3},
# #     182: {"playerTotal": 14, "dealerCard": 4},
# #     183: {"playerTotal": 14, "dealerCard": 5},
# #     184: {"playerTotal": 14, "dealerCard": 6},
# #     185: {"playerTotal": 14, "dealerCard": 7},
# #     186: {"playerTotal": 14, "dealerCard": 8},
# #     187: {"playerTotal": 14, "dealerCard": 9},
# #     188: {"playerTotal": 14, "dealerCard": 10},
# #     189: {"playerTotal": 14, "dealerCard": 11},
# #     190: {"playerTotal": 15, "dealerCard": 2},
# #     191: {"playerTotal": 15, "dealerCard": 3},
# #     192: {"playerTotal": 15, "dealerCard": 4},
# #     193: {"playerTotal": 15, "dealerCard": 5},
# #     194: {"playerTotal": 15, "dealerCard": 6},
# #     195: {"playerTotal": 15, "dealerCard": 7},
# #     196: {"playerTotal": 15, "dealerCard": 8},
# #     197: {"playerTotal": 15, "dealerCard": 9},
# #     198: {"playerTotal": 15, "dealerCard": 10},
# #     199: {"playerTotal": 15, "dealerCard": 11},
# #     200: {"playerTotal": 16, "dealerCard": 2},
# #     201: {"playerTotal": 16, "dealerCard": 3},
# #     202: {"playerTotal": 16, "dealerCard": 4},
# #     203: {"playerTotal": 16, "dealerCard": 5},
# #     204: {"playerTotal": 16, "dealerCard": 6},
# #     205: {"playerTotal": 16, "dealerCard": 7},
# #     206: {"playerTotal": 16, "dealerCard": 8},
# #     207: {"playerTotal": 16, "dealerCard": 9},
# #     208: {"playerTotal": 16, "dealerCard": 10},
# #     209: {"playerTotal": 16, "dealerCard": 11},
# #     210: {"playerTotal": 17, "dealerCard": 2},
# #     211: {"playerTotal": 17, "dealerCard": 3},
# #     212: {"playerTotal": 17,"dealerCard": 4},
# #     213: {"playerTotal": 17,"dealerCard": 5},
# #     214: {"playerTotal": 17, "dealerCard": 6},
# #     215: {"playerTotal": 17, "dealerCard": 7},
# #     216: {"playerTotal": 17, "dealerCard": 8},
# #     217: {"playerTotal": 17, "dealerCard": 9},
# #     218: {"playerTotal": 17, "dealerCard": 10},
# #     219: {"playerTotal": 17, "dealerCard": 11},
# #     220: {"playerTotal": 18, "dealerCard": 2},
# #     221: {"playerTotal": 18, "dealerCard": 3},
# #     222: {"playerTotal": 18, "dealerCard": 4},
# #     223: {"playerTotal": 18, "dealerCard": 5},
# #     224: {"playerTotal": 18, "dealerCard": 6},
# #     225: {"playerTotal": 18, "dealerCard": 7},
# #     226: {"playerTotal": 18, "dealerCard": 8},
# #     227: {"playerTotal": 18, "dealerCard": 9},
# #     228: {"playerTotal": 18, "dealerCard": 10},
# #     229: {"playerTotal": 18, "dealerCard": 11},
# #     230: {"playerTotal": 19, "dealerCard": 2},
# #     231: {"playerTotal": 19, "dealerCard": 3},
# #     232: {"playerTotal": 19, "dealerCard": 4},
# #     233: {"playerTotal": 19, "dealerCard": 5},
# #     234: {"playerTotal": 19, "dealerCard": 6},
# #     235: {"playerTotal": 19, "dealerCard": 7},
# #     236: {"playerTotal": 19, "dealerCard": 8},
# #     237: {"playerTotal": 19, "dealerCard": 9},
# #     238: {"playerTotal": 19, "dealerCard": 10},
# #     239: {"playerTotal": 19, "dealerCard": 11},
# #     240: {"playerTotal": 20, "dealerCard": 2},
# #     241: {"playerTotal": 20, "dealerCard": 3},
# #     242: {"playerTotal": 20, "dealerCard": 4},
# #     243: {"playerTotal": 20, "dealerCard": 5},
# #     244: {"playerTotal": 20, "dealerCard": 6},
# #     245: {"playerTotal": 20, "dealerCard": 7},
# #     246: {"playerTotal": 20, "dealerCard": 8},
# #     247: {"playerTotal": 20, "dealerCard": 9},
# #     248: {"playerTotal": 20,"dealerCard": 10},
# #     249: {"playerTotal": 20, "dealerCard": 11}
# # }
# #     scenarioList = []
# #     playerAceCount = 0
# #     dealerAceCount = 0
# #     card = 0
# #     secCard = 0

#     # for i in range (250):
#     #     scenarioList.append(random.randint(0,1))    
    
   
#     #give player cards
#     for i in range(2):
#         Game.giveCard(player, Game.cards)
#     # print("Player Total: ", player.total)    
#     #give dealer cards

#     dealerCard = Game.giveCard(dealer, Game.cards)
#     Game.giveCard(dealer, Game.cards)
#     # print('Dealer Card:', dealerCard)
#     # print("Dealer Total: ", dealer.total)    

#     if player.aceCount == 0:
#         print('hit')
#         return getIndex(Game.scenarioIDToScenarioNoAce)
#     else:
#         print('hit2')
#         return getIndex(Game.scenarioIDToScenarioWithAce)
    





# def getIndex(dict):
#     print(player.total)
#     print(dealerCard)
#     for element in dict: 
#         if (player.total == dict[element]["playerTotal"]):
#             if (dealerCard == dict[element]["dealerCard"]):
#             #if dealerCard == dict[i]["dealerCard"]:
#                 print(scenarioList[element])
#                 return scenarioList[element]
#                 # if scenarioList[i] == 1:
#                 #     playerTotal += giveCard(cards, player, playerTotal, dealerTotal)
#                 #     if playerAceCount == 0:
#                 #         return getIndex(dict, playerTotal, dealerCard, scenarioList, playerAceCount, cards)
#                 #     else:
#                 #         return getIndex(dict, playerTotal, dealerCard, scenarioList, playerAceCount, cards)
#                 # elif scenarioList[i] == 0 or playerTotal > 21:
#                 #     return playerTotal

def get_shuffled_deck():
    cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
    random.shuffle(cards)
    return cards

def get_player_choice(individual, player_hand, dealer_showing_card):
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
    if 11 in player_hand:
        for scenarioId in scenarioIDToScenarioWithAce:
            if sum(player_hand) == scenarioIDToScenarioWithAce[scenarioId]["playerTotal"]:
                if dealer_showing_card == scenarioIDToScenarioWithAce[scenarioId]["dealerCard"]:
                    return individual[scenarioId]
    else:
        for scenarioId in scenarioIDToScenarioNoAce:
            if sum(player_hand) == scenarioIDToScenarioNoAce[scenarioId]["playerTotal"]:
                if dealer_showing_card == scenarioIDToScenarioNoAce[scenarioId]["dealerCard"]:
                    return individual[scenarioId]

    
def fitnessFunction(individual):
    fitness_score = 0
    # Simulate 1000 rounds of blackjack
    for i in range(1000):
        deck = get_shuffled_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        
        # Player turn
        # When player_hand has A-A
        if sum(player_hand) > 21 and (11 in player_hand):
            i = player_hand.index(11)
            player_hand[i] = 1
        
        while sum(player_hand) < 21:
            choice = get_player_choice(individual, player_hand, dealer_hand[0])
            if choice == 1:
                player_hand.append(deck.pop())
                if sum(player_hand) > 21 and (11 in player_hand):
                    i = player_hand.index(11)
                    player_hand[i] = 1
            else:
                break
        
        # Check for bust
        if sum(player_hand) > 21:
            fitness_score -= 1
            continue

        # Dealer hand
        if sum(dealer_hand) > 21 and (11 in dealer_hand):
            i = dealer_hand.index(11)
            dealer_hand[i] = 1

        while sum(dealer_hand) <= 16:
            dealer_hand.append(deck.pop())
            if sum(dealer_hand) > 21 and (11 in dealer_hand):
                i = dealer_hand.index(11)
                dealer_hand[i] = 1
                    
        if sum(dealer_hand) > 21:
            fitness_score += 1
            continue

        if sum(player_hand) > sum(dealer_hand):
            fitness_score += 1
        elif sum(player_hand) < sum(dealer_hand):
            fitness_score -= 1
    return [fitness_score]

#make black jack environment with deck and rules and everything
#with initialized game, have to go through each key and value in dictionary to find index
# use index to find 1 or 0, and then simulate said action with if statement!!!!!

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
# Attribute generator 
toolbox.register("attr_bool", random.randint, 0, 1)
# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, 
    toolbox.attr_bool, 250)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", fitnessFunction)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

pop = toolbox.population(n=300)
# Evaluate the entire population
fitnesses = list(map(toolbox.evaluate, pop))
for ind, fit in zip(pop, fitnesses):
    ind.fitness.values = fit

# CXPB  is the probability with which two individuals
#       are crossed
#
# MUTPB is the probability for mutating an individual
CXPB, MUTPB = 0.5, 0.2

# Extracting all the fitnesses of 
fits = [ind.fitness.values[0] for ind in pop]

# Variable keeping track of the number of generations
g = 0

# Begin the evolution
while max(fits) < 100 and g < 5:
    # A new generation
    g = g + 1
    print("-- Generation %i --" % g)

        # Select the next generation individuals
    offspring = toolbox.select(pop, len(pop))
    # Clone the selected individuals
    offspring = list(map(toolbox.clone, offspring))

    # Apply crossover and mutation on the offspring
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < CXPB:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

    for mutant in offspring:
        if random.random() < MUTPB:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    pop[:] = offspring
        
    # Gather all the fitnesses in one list and print the stats
    fits = [ind.fitness.values[0] for ind in pop]

    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x*x for x in fits)
    std = abs(sum2 / length - mean**2)**0.5

    print("  Min %s" % min(fits))
    print("  Max %s" % max(fits))
    print("  Avg %s" % mean)
    print("  Std %s" % std)

best_ind = tools.selBest(pop, 1)[0]
print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))