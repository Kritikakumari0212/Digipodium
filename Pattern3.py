from turtle import *
speed('fastest')
colors=['red','blue']
for i in range(6):
    pencolor('black')
    pensize(2)
    fd(120)
    for i in range(6):
        pencolor('black')
        fd(60)
        fillcolor(colors[i%2])
        begin_fill()
        for i in range(4):
            pencolor('black')
            fd(30)
            lt(360/4)
        end_fill()
        lt(360/6)
    lt(360/6)
mainloop()        