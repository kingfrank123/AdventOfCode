# just a smaller sample txt for edge cases
# path2 = r"C:\Users\frank\OneDrive\Desktop\stuff\AdventofCode\sample.txt"
# arr2 = []

# with open(path2, 'r') as file:
#     for line in file:
#         arr2.append(line.strip())
# file.close()

# replace path with your local path
path = r"C:\Users\frank\OneDrive\Desktop\stuff\AdventofCode\input2.txt"
arr = []

with open(path, 'r') as file:
    for line in file:
        arr.append(line.strip())
file.close()

red, green, blue = 12,13,14

# takes in 1 game returns either game id or 0
def validate_game(game):
    # add game[0] if its correct
    round = game[1].split(";")
    for i in round:
        check = i.split(",")
        r,g,b = 0, 0, 0
        for j in check:
            if 'green' in j:
                g = int(j.split()[0])
            elif 'red' in j:
                r = int(j.split()[0])
            elif 'blue' in j:
                b = int(j.split()[0])
        if g > green or b > blue or r > red:
            return 0
    return int(game[0])

# takes in the # of red, green, blue cubes that are possible and list of games
def possible_games(games):
    possible_ids = []
    for game in games:
        game = game[5:]
        game = game.split(":")
        # game[0] -> Game Id, game[1] -> Subsets of hands shown
        possible_ids.append(validate_game(game))

    return sum(possible_ids)

print(possible_games(arr))