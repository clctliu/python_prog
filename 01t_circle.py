import turtle as t
from itertools import cycle

colors = cycle(['red','orange','yellow','blue','green'])

def draw_circle(color, size, angle, shift):
    # t.pencolor(color)
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(color, size+1, angle+1, shift+1)

t.bgcolor('pink')
t.pensize(4)
t.speed(1000)

draw_circle('red', 30, 0, 1)
