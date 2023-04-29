#Game for players to take turn . ther e will be A, B, C, D inputs from use
#in put ["A", "B", "C", "D"]
#generate two randon choices from the input and therir corresponding indexes
#cumulative pair lenght is less than total index
#identical pair legnth is the points.add()
# # two player
# a player should have name, score, and


import random
input= ["A", "B", "C", "D"]

pair = []
def player(name, score):
    return {"name": name, "score": score}

cumPair = 0
totalIndex = 0
score = 0
while len(cumPair) < totalIndex:

    def randomChoice(items):
        count= 0
        while count<2:
            from random import choice
            a = choice(items)
            i = items.index(a)
            pair.append((a, i))
            count += 1
        return pair
    
    pair1, pair2 = pair
    if pair1[0] == pair2[0]:
        score += 1
    for i in pair:        
        cum, ind = i
        cumPair += 1
        totalIndex += ind
    print(score)
    print(randomChoice(input))
    
    #============================CORRECTION =============================
    
    def pairAlphaIndex(alphas:list) ->(tuple):
        alpha_index = zip(alphas, range(len(alphas)))
        return list(alpha_index)
        pass
    
    def pairAlpha(pairs:list)-> tuple(str, int):
        
        pass
    
    def cumPair(pair, index):
        cum = str()
        total = int()
        
        while len(cum) <= total:
            pair_alphas, total_index = pairAlpha()
            
            pass
        
    def showScoreBoard(players):
        pass