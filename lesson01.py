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
colors = ['red', 'green', 'blue']
for color in colors:
   print(f' My favorite color is', {color.title()})
print('These are my favorite colors') 

pizza = ['peperoni', 'italian', 'vegetable', 'cheese']
for pizza_1 in pizza:
   print(pizza_1.title())

animals = ['cat', 'tiger', 'leopard']
for animal in animals:
    print(animal.title())   
for animal in animals:
    print(f' A {animal} is cute')
print(" Any of these animals belong to cat family ")
 for number in range(1, 21):
    print(number)
for number in range(1, 21):
    print(number, end= ',')
#for number in range(1, 1000001):
 #  print(number, end= ',')
print() #go to next line
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
numbers= list(range(1,20, 2))
print(numbers)
numbers = list(range(3,31,3))
for number in numbers:
    print(number)
    print()
cubes = []
for number in range(1,11):
     cubes.append(number**3)
for cube in cubes:
    print(cube)
    print()

cubes = []
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)