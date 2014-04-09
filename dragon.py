import turtle
import random

def dragon_build(turtle_string, n):
    """ Recursively builds a draw string. """
    """ defining f, +, -, as additional rules that don't do anything """

    rules = {'x':'x+yf', 'y':'fx-y','f':'f', '-':'-', '+':'+'}
    turtle_string = ''.join([rules[x] for x in turtle_string])
    if n > 1: return dragon_build(turtle_string, n-1)
    else: return turtle_string

def dragon_draw(size):
    """ Draws a Dragon Curve of length 'size'. """
    turtle_string = dragon_build('fx', size)
    for x in turtle_string:
        turtle.color(random_Color(turtle.color()))
        if x == 'f': turtle.forward(5)
        elif x == '+': turtle.right(90)
        elif x == '-': turtle.left(90)

def random_Color(color):
    color = ""
    for x in range(6): color+= str(hex(random.randint(0,15)))[2:]
    return "#"+color

def main():
    n = int(input("Size of Dragon Curve (int): "))
    turtle.pensize(2)
    turtle.speed(0)
    turtle.penup()
    turtle.backward(100)
    turtle.left(90)
    # turtle.forward(100)
    # turtle.right()
    turtle.pendown()

    dragon_draw(n)
    input()



if __name__ == '__main__': main()