"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target
    w , h , z = win_height , win_height, win_height
    r = z / 10
    cir_w = Circle(Point(w / 2 , h / 2) , 5 * r)
    cir_w.setFill('white')
    cir_bk = Circle(Point(w / 2 , h / 2) , 4 * r)
    cir_bk.setFill('black')
    cir_b = Circle(Point(w / 2 , h / 2) , 3 * r)
    cir_b.setFill("blue")
    cir_r = Circle(Point(w / 2 , h / 2) , 2 * r)
    cir_r.setFill('red')
    cir_y = Circle(Point(w / 2 , h / 2) , r)
    cir_y.setFill('yellow')
    cir_w.draw(win)
    cir_bk.draw(win)
    cir_b.draw(win)
    cir_r.draw(win)
    cir_y.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)
    p1_p2 = (((p1.getX() - p2.getX()) ** 2) + ((p1.getY() - p2.getY()) ** 2)) ** (1/2)
    p2_p3 = (((p2.getX() - p3.getX()) ** 2) + ((p2.getY() - p3.getY()) ** 2)) ** (1/2)
    p3_p1 = (((p3.getX() - p1.getX()) ** 2) + ((p3.getY() - p1.getY()) ** 2)) ** (1/2)
    # and display its area in the graphics window.
    s = (p1_p2 + p2_p3 + p3_p1) / 2
    area = (s * (s - p1_p2) * (s - p2_p3) * (s - p3_p1)) ** (1/2)
    area_text = Text(Point(win_width / 2 , 100), 'the area is '+ str(area))
    area_text.draw(win)
    perimeter = p1_p2 + p2_p3 + p3_p1
    per_text = Text(Point(win_width / 2 , 120), 'the perimeter is '+ str(perimeter))
    per_text.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")


    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")


    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point(win_width / 2, win_width / 2 + 40), 5)
    blue_box = Entry(Point(win_width / 2, win_width / 2 + 100), 5)
    green_box = Entry(Point(win_width / 2, win_width / 2 + 70), 5)
    red_box.draw(win)
    blue_box.draw(win)
    green_box.draw(win)

    for _ in range(5):
        win.getMouse()
        red = int(red_box.getText())
        blue = int(blue_box.getText())
        green = int(green_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)
    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    s = input('write your string here: ')
    print(s[0])
    print(s[-1])
    print(s[1:5])
    print(s[0] + s[-1])
    print(s[0:3] * 10)
    for i in range(len(s)):
        c = s[i]
        print(c)
    print(len(s))

def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4] + [values[0]]
    print(x)
    x = [values[0]] + [values[2]] + [float(values[-1])]
    print(x)
    x = sum(x)
    print(x)
    x = len(values)
    print(x)

def another_series():
    user_in = eval(input('how many loops would you like?: '))
    acc = 0
    for i in range(user_in):
        y = 2 + 2 * (i % 3)
        print(y, end=' ')
        acc = acc + y
        print(acc)


def main():
    # target()
    # triangle()
    # color_shape()
    # process_string()
    # process_list()
    # another_series()
    pass


main()
