'''
Robert Stenback's greeting card
this program draws a valentines day card in a window
'''
import time

from graphics import GraphWin
from graphics import Circle
from graphics import Polygon
from graphics import Point
from graphics import Text

def main():
    win_width = 400
    win_height = 400
    win = GraphWin("Valentines Card", win_width, win_height)
    win.setBackground("pink")
    #right
    shape = Circle(Point((win_width / 2) + 25, win_height / 2), 30)
    shape.draw(win)
    shape.setFill('red')
    shape.setOutline('red')
    #middle
    shape1 = Circle(Point((win_width / 2), win_height / 2 +10), 20)
    shape1.draw(win)
    shape1.setFill('red')
    shape1.setOutline('red')
    #left
    shape2 = Circle(Point((win_width / 2) - 25, win_height / 2), 30)
    shape2.draw(win)
    shape2.setFill('red')
    shape2.setOutline('red')

    triangle = Polygon(Point((win_width / 2) + 50, win_height / 2 + 18) ,
                       Point((win_width / 2) - 50, win_height / 2 + 18),
                       Point(win_width / 2, win_height / 2 + 70))
    triangle.draw(win)
    triangle.setFill('red')
    triangle.setOutline('red')

    msg = 'Happy Valentine’s Day!'
    inst = Text(Point(win_width / 2, win_height - 380), msg)
    inst.draw(win)

    p1 = Point(5, 0 )
    p2 = Point(0 , 5)
    p3 = Point(140 , 155)
    p4 = Point(140 , 155)
    line = Polygon(p1,p2,p3,p4)
    line.draw(win)
    line.setFill('yellow')
    line.setOutline('yellow')

    for i in range (12):
        line.move(10,10)
        time.sleep(.03)
    time.sleep(.3)
    msg2 = 'click anywhere to close'
    inst2 = Text(Point(win_width / 2, win_height - 20), msg2)
    inst2.draw(win)
    win.getMouse()

if __name__ == '__main__':
    main()