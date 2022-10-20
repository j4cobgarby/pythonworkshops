from turtle import *

def step(s):
    new_s = []
    for i in s:
        if i == 'F':
            new_s += list("F-G+F+G-F")
        elif i == 'G':
            new_s += list("GG")
        else:
            new_s.append(i)
    return new_s

def main():
    s = list("F-G-G")
    penup()
    goto((200,300))
    speed(0)
    setheading(-90)

    pendown()

    for i in range(7):
        s = step(s)

    for instruction in s:
        if instruction == 'F' or instruction == 'G':
            fd(7)
        elif instruction == '+':
            lt(120)
        elif instruction == '-':
            rt(120)

    mainloop()

main()