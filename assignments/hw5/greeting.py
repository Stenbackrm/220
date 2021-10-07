'''
Robert Stenback's greeting card
this program draws a valentines day card in a window
'''

from graphics import GraphWin
from graphics import Circle
from graphics import Polygon
from graphics import Point

def main():
    win_width = 400
    win_height = 400
    win = GraphWin("Valentines Card", win_width, win_height)
    win.setBackground("white")
    #right
    shape = Circle(Point((win_width / 2) + 25, win_height / 2), 30)
    shape.draw(win)
    shape.setFill('red')
    shape.setOutline('red')
    #middle
    shape = Circle(Point((win_width / 2), win_height / 2 +10), 20)
    shape.draw(win)
    shape.setFill('red')
    shape.setOutline('red')
    #left
    shape = Circle(Point((win_width / 2) - 25, win_height / 2), 30)
    shape.draw(win)
    shape.setFill('red')
    shape.setOutline('red')

    triangle = Polygon(Point((win_width / 2) + 50, win_height / 2 + 18) ,
                       Point((win_width / 2) - 50, win_height / 2 + 18),
                       Point(win_width / 2, win_height / 2 + 70))
    triangle.draw(win)
    triangle.setFill('red')
    triangle.setOutline('red')

    win.getMouse()

if __name__ == '__main__':
    main()