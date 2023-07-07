from turtle import *

def square(size, color): #function definition
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(size)
        right(90)
    end_fill()
def hexagon(size,color):
    fillcolor(color)
    begin_fill()
    for i in range(6):
        forward(size)
        right(60)
    end_fill()

hexagon(100,'yellow')
hexagon(80,'purple')
square(80,'red') #calling
square(50,'blue')
square(25,'green')

mainloop()