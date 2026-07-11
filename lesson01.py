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
