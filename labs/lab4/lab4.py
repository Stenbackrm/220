"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50) , Point(70 , 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX()-10, p.getY()-10), Point(p.getX()+10, p.getY()+10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
    instructions.undraw()
    instructions.setText('Click again to close')
    instructions.draw(win)


    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width_win = 400
    height_win = 400
    win = GraphWin('Rectangle' , width_win, height_win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = Rectangle(p1, p2)
    r.setOutline("red")
    r.setFill("red")
    r.draw(win)
    length = abs(p2.getX() - p1.getX())
    width =  abs(p2.getY() - p1.getY())
    area = length * width
    area_txt = Text(Point((width_win / 2),30), "the area is:" + str(area))
    perimeter = 2 * (length + width)
    per_txt = Text(Point((width_win / 2),10), "the perimeter is:" + str(perimeter))
    per_txt.draw(win)
    area_txt.draw(win)
    inst_pt = Point(width_win / 2, height_win - 10)
    instructions = Text(inst_pt, "Click to exit program")
    instructions.draw(win)
    win.getMouse()
    win.close()


def circle():
    width_win = 400
    height_win = 400
    win = GraphWin('circle', width_win, height_win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    rad = (((p2.getX() - p1.getX()) ** 2) + ((p2.getY() - p1.getY()) ** 2)) ** .5
    cir = Circle(p1 , rad)
    cir.setOutline("red")
    cir.setFill("red")
    cir.draw(win)
    inst_pt = Point(width_win / 2, height_win - 10)
    instructions = Text(inst_pt, "Click to exit program")
    instructions.draw(win)
    per_txt = Text(Point((width_win / 2), 10), "the radius is:" + str(rad))
    print(p1,p2)
    per_txt.draw(win)
    win.getMouse()
    win.close()


import math
def pi2():
    acc = 0
    n = eval(input('how many passes would you like?'))
    for i in range(n):
        num = 4 * ((-1) ** i)
        denom = 1 + (2 * i)
        acc = acc + (num / denom)
    print(acc)
    print(math.pi - acc)




def main():
    # squares()
    # rectangle()
    # circle()
    # pi2()


main()
