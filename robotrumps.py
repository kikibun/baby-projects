from random import choice
from turtle import *

screen = Screen()
screen.bgcolor('white')
penup()
hideturtle() 

robots = {}

file = open('cards.txt', 'r')
for line in file.read().splitlines():
    #print line
    name, battery, intelligence, sass, image = line.split(', ')
    robots[name] = [battery, intelligence, sass, image]
    screen.register_shape(image)
file.close()
#print(robots)

#names = list(robots.keys())

print("Fighters: ", end='')
length = len(robots.keys())
#print(length)
for name in list(robots.keys())[:-1]:
    print(name, end=', ')
print(list(robots.keys())[-1])
#print(names)
robota = input('Choose your fighter: ')
robotb = input('Choose your fighter: ')
print('Fight stats: battery, intelligence, sass')
fight_stat = input('Choose your battle stat: ')

style = ('Veranda', 14, 'bold')
if robota in robots:
    print(robots[robota])
    stats = robots[robota]
    #style = ('Veranda', 14, 'bold')
    #clear()
    goto(-150, 100)
    shape(stats[3])
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Name: ' + robota, font=style, align='center')
    forward(25)
    write('Battery: ' + stats[0], font=style, align='center')
    forward(25)
    write('Intelligence: '+ stats[1], font=style, align='center')
    forward(25)
    write('Sass: ' + stats[2], font=style, align='center')
else:
    print('There is no fighter by that name!')

def winner(stat_a, stat_b):
    if fight_stat == 'battery':
        stat_a = robots[robota][0]
        stat_b = robots[robotb][0]
    elif fight_stat == 'intelligence':
        stat_a = robots[robota][1]
        stat_b = robots[robotb][1]
    elif fight_stat == 'sass':
        stat_a = robots[robota][2]
        stat_b = robots[robotb][2]

    if int(stat_a) > int(stat_b):
        write('The winner is ' + robota + '!', font=style, align='center')
    else:
        write('The winner is ' + robotb + '!', font=style, align='center')

    

if robotb in robots:
    print(robots[robotb])
    stats = robots[robotb]
    #clear()
    goto(150, 100)
    shape(stats[3])
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Name: ' + robotb, font=style, align='center')
    forward(25)
    write('Battery: ' + stats[0], font=style, align='center')
    forward(25)
    write('Intelligence: '+ stats[1], font=style, align='center')
    forward(25)
    write('Sass: ' + stats[2], font=style, align='center')
    goto(0,0)
    setheading(-90)
    forward(60)
    write('Fight stat is ' + fight_stat, font=style, align='center')
    forward(25)
    winner(robota, robotb)
else:
    print('There is no fighter by that name!')

print(winner(robota, robotb))
 
while True:
     pass