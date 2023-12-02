path = r"C:\Users\frank\OneDrive\Desktop\stuff\AdventofCode\input2.txt"
arr = []

with open(path, 'r') as file:
    for line in file:
        arr.append(line.strip())
file.close()

def max_of_each_game(game):
    round = game[1].split(";")
    # now r g and b represent the max red green and blues seen so far
    r,g,b = 0, 0, 0
    for i in round:
        check = i.split(",")
        # i.e check = [' 20 green', ' 3 red', ' 2 blue']
        for j in check:
            if 'green' in j:
                if int(j.split()[0]) > g:
                    g = int(j.split()[0])
            elif 'red' in j:
                if int(j.split()[0]) > r:
                    r = int(j.split()[0])
            elif 'blue' in j:
                if int(j.split()[0]) > b:
                    b = int(j.split()[0])
        
    return r*g*b

powers = []
for game in arr:
    game = game[5:]
    game = game.split(":")
    powers.append(max_of_each_game(game))

print(sum(powers))



