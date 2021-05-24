import random
playerLi = []
print("Press Enter to submit list...")
i = 1
while 1:
    playerName = input(f"Enter Player {i} Name:\n")
    if playerName == "":
        break
    playerLi.append(playerName)
    i+=1

nPlayer = len(playerLi)
print(f"No. of Player in this Match : {nPlayer}")
n = 1
while not (len(playerLi) == 0):
    randPlayer = random.choice(playerLi)
    print(f"{n}. - {randPlayer}")
    playerLi.remove(randPlayer)
    n+=1