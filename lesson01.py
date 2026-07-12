players= ['Neymar', 'Ronaldo', 'Messi', 'Holland', 'Cortoa']
print(players)
print(players[:3])
print(players[2:])
print(players[-1])
print(players[-3])
print(players[0:3])
print(players[0:5])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
for player in players[2:5]:
    print(player.title())
players_2= players[:]
print('My favorite players are:')
print(players)
print("\nMy friend's favorite players are:")
print(players_2)
players= ['Neymar', 'Ronaldo', 'Messi', 'Holland', 'Cortoa']
players_2= players[:]
players.append('James')
print('My favorite players are:')
print(players)
print("\nMy friend's favorite players are:")
print(players_2)
foods = ("pizza", "rice", "stew", "hamburger", "spaghetti")
for food in foods:
    print(food.title())

foods = ("pizza", "rice", "stew", "hamburger", "spaghetti")

foods = ("soup", "pasta", "rice", "hamburger", "spaghetti")
for food in foods:
   print(food.title())
