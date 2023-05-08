import pickle
players = [
    {"name": "John", "score": 0, "trials": 0},
    {"name": "Mary", "score": 0, "trials": 0},
]

with open("score", "ab") as file:
    # content = file.read()
    for player in players:
        name, score, trial = player.items() #unboxing the player from the dictionary produces a tuple of (name, score, trial). each tuple having key and value pairs.
        print(name)
        print(score, trial)
        playerRecord = f"{name[1]}/{score[1]}/{trial[1]}\n"  #file.write(f"{player['name']}, {player['score']}, {player['trials']}\n")
        print(playerRecord)
        
pickle.dump(score, file)


#===========correction==============

