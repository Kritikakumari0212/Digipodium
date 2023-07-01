from turtle import *
speed('fastest')
for i in range(6):
    pencolor('red')
    pensize(2)
    fd(120)
    for i in range(6):
        pencolor('blue')
        fd(60)
        fillcolor('red')
        begin_fill()
        for i in range(3):
            pencolor('blue')
            fd(30)
            lt(360/3)
        end_fill()
        lt(360/6)
    lt(360/6)
mainloop()        