from turtle import *
speed('fastest')
for i in range(9):
    pencolor('red')
    fd(100)
    for i in range(9):
        pencolor('blue')
        fd(50)
        lt(360/9)
        for i in range(9):
            pencolor('green')
            fd(25)
            lt(360/9)
    lt(360/9)
mainloop()        