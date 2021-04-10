import turtle as t
from random import randint, random
t.speed(1000)
def draw_star(size, points, x, y, colr):
    # parameter for the star
    angle = 180 - (180/points)

    t.color(colr)
    # points = 5
    # angle = 144
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

def draw_planet(size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

#draw size 100 star, 5 points
#draw_star(100, 5, 0, 0, 'red')
#draw size 300 star, 9 points
#draw_star(300, 9, 200, 200, 'yellow')
t.Screen().bgcolor('dark blue')

while True:
    ranSize = randint(10, 100)
    ranPts = randint(2, 5) *2 + 1
    ranX = randint(-500, 500)
    ranY = randint(-400, 400)
    ranColor = (random(), random(), random())
    if (randint(1, 2) == 1):
        draw_star(ranSize, ranPts, ranX, ranY, ranColor)
    else:
        draw_planet(ranSize/2, ranColor, ranX, ranY)
