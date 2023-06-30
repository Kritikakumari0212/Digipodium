from turtle import *
speed('fastest')
pencolor('green')
pensize(1)
for i in range(100):
    fd(100-i)
    rt(30)
    circle(120 ,270)
mainloop()