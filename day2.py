import re

import pandas as pd

with open('day2_input.txt', 'r') as f:
    content = f.read()


def collect_draws(draws):
    cubes = {}

    colors = re.split(',|;', draws)
    for color2 in colors:
        color = re.findall('(\d+) (green|red|blue)', color2)

        if color[0][1] in cubes.keys():
            cubes[color[0][1]] = max(cubes.get(color[0][1]), int(color[0][0]))
        else:
            cubes[color[0][1]] = int(color[0][0])
    return cubes


sample = """Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

lines = content.splitlines()
games = []

for line in lines:
    test = {}
    game = line.replace('Game ', '').split(':')
    test['game'] = int(game[0])
    test.update(collect_draws(game[1]))
    test['power'] = test.get('red') * test.get('green') * test.get('blue')
    print(test)
    games.append(test)

df = pd.DataFrame(games)
print(df.head())

red_limit = 12
green_limit = 13
blue_limit = 14

df_possible_games = df[(df['red'] <= red_limit) & (df['green']
                                                   <= green_limit) & (df['blue'] <= blue_limit)]

print(sum(df_possible_games['game']))
print(sum(df['power']))
