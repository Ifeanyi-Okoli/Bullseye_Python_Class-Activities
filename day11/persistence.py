"""We use files for persistence.
Files helps us to save data for later use.
"""

#create a list of players, the score, name and level
# open file and save into the file#
import os
# players = {
#     "player1": {"name": "John", "score": 100, "level": 2},
#     "player2": {"name": "Mary", "score": 300, "level": 4},
# }


# file = open("score.txt", "w")
# file.write = (players["player1"])
# file.write = (players["player2"])
# content = file.read()
# file.close()
# print(content)


#========correction================

players = [
    {"name": "John", "score": 0, "trials": 0},
    {"name": "Mary", "score": 0, "trials": 0},
]

with open("score.txt", "w") as file:
    # content = file.read()
    for player in players:
        #[["name", "John"], ["score", 0], ["trials", 0]]
        name, score, trial = player.items()
        playerRecord = f"{name[1]}/{score[1]}/{trial[1]}\n"  #file.write(f"{player['name']}, {player['score']}, {player['trials']}\n")
        print(playerRecord)
        
        file.write(playerRecord)
            
