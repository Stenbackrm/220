"""
Robert Stenback's three door game
"""
from random import randint
from graphics import Rectangle, Point, GraphWin, Text
from button import Button

def main():
    width = 600
    height = 500
    win_name = 'Three Door Game'
    door_1_txt, door_2_txt, door_3_txt = 'door 1', 'door 2', 'door 3'
    win = GraphWin(win_name, width, height)
    point_1 = Point(width / 2 - 50, 500 - height / 3)
    point_2 = Point(width / 2 + 50, 560 - height / 3)

    text_w = 'I have a secret door'
    text = Text(Point(width / 2, 450 - height / 3), text_w)
    text.draw(win)

    button_1_rec = Rectangle(point_1, point_2)
    button_1 = Button(button_1_rec, door_2_txt)
    button_1.draw(win)

    button_2_rec = button_1_rec.clone()
    button_2_rec.move(150, 0)
    button_2 = Button(button_2_rec, door_3_txt)
    button_2.draw(win)

    button_3_rec = button_1_rec.clone()
    button_3_rec.move(-150, 0)
    button_3 = Button(button_3_rec, door_1_txt)
    button_3.draw(win)

    point = win.getMouse()
    rand_num = randint(1, 3)

    if button_1.is_clicked(point) is True:
        if rand_num == 2:
            button_1.color_button('green')
            text_w = 'you win!!'
            text.setText(text_w)
        else:
            button_1.color_button('red')
            text_x = 'you lose it was door'
            text_w = '{0} {1}'.format(text_x, rand_num)
            text.setText(text_w)

    if button_2.is_clicked(point) is True:
        if rand_num == 3:
            button_2.color_button('green')
            text_w = 'you win!!'
            text.setText(text_w)
        else:
            button_2.color_button('red')
            text_x = 'you lose it was door'
            text_w = '{0} {1}'.format(text_x, rand_num)
            text.setText(text_w)

    if button_3.is_clicked(point) is True:
        if rand_num == 2:
            button_3.color_button('green')
            text_w = 'you win!!'
            text.setText(text_w)
        else:
            button_3.color_button('red')
            text_x = 'you lose it was door'
            text_w = '{0} {1}'.format(text_x, rand_num)
            text.setText(text_w)
    win.getMouse()

if __name__ == '__main__':
    main()
