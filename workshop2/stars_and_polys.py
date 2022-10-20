from turtle import *

speed(0)

def star(n, l):
    for i in range(n):
        outer = ((n-2)*180) / n
        inner = 180 - 2*(180 - outer)

        fd(l)
        lt(180 - outer)
        fd(l)
        rt(180 - inner)

def poly(n, l):
    for i in range(n):
        fd(l)
        rt(360/n)

pencolor("red")

for i in range(5, 10):
    star(i, 100)

mainloop()