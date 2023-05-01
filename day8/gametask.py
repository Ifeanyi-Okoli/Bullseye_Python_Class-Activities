import random
import time
def pairAlphaIndex(alphas:list):
    alpha_index = zip(alphas, range(len(alphas))) 
    return list(alpha_index)

def pairAlpha(pairs:list):
    choice_1, choice_2 = random.choices(pairs, k=2)
    pair_alphas = choice_1[0] + choice_2[0]
    total_index = choice_1[1] + choice_2[1]
    return pair_alphas, total_index

def cumPair (alphas, players, turn):
    cum = str()
    cum_total = int()
    identicals = []
    print(players)
    
def start_game(alphas, players, turn):
    cumPair(alphas, players, 0)
    
def showScoreBoard(players):
    board = f"""
    FINAL SCORE:
    \n
    ================================================
    \n
    \t Player 1: name: {players[0]["name"]}, score: {players[0] ["score"]}
    \n 
    \t Player 1: name: {players[0]["name"]}, score: {players[0] ["score"]}
    \n
    """
    print(board)
    
def updateScore(player, score):
    player["score"] += score
    
players = [
    {"name": "player 1", "score": 0},
    {"name": "player 2", "score": 0}
]

alphas = ["A", "B", "C", "D"]

start_game(alphas, players, 0)