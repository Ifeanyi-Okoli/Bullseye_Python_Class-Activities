players = [
    {"name": "John", "score": 0, "trials": 0},
    {"name": "Mary", "score": 0, "trials": 0},
]

with open("./score.txt", "r") as file:
    record = file.readlines()
    print(record)
    for index, player in enumerate(record):
        name, score, trials = player.split("/")
        players[index]["name"] = name
        players[index]["score"] = score
        players[index]["trials"] = trials
        # playerRecord = f"{name[1]}/{score[1]}/{trial[1]}\n"  #file.write(f"{player['name']}, {player['score']}, {player['trials']}\n")


print(players)

