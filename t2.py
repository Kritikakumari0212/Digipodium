from turtle import *
speed('fastest')
pencolor('blue')
pensize(1)
for i in range(100):
    fd(100-i)
    rt(60)
    circle(100 ,270)
    dot(10,'red')
mainloop()