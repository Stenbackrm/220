"""
Robert Stenback's three door game
"""
from random import randint
from graphics import Rectangle, Point, GraphWin, Text
from Button import Button


def lose(button, ran_num, text):
    button.color_button('red')
    text.setText('you lose :( it was door {0}\n\nclick to exit'.format(ran_num))


def game_win(button, text):
    button.color_button('green')
    text.setText('you win!!\n\nclick to exit')

def main():

    door_1_txt, door_2_txt, door_3_txt = 'door 1', 'door 2', 'door 3'
    win = GraphWin('Three Door Game', 600, 500)
    point_1 = Point(250, 500 - 500 / 3)
    point_2 = Point(350, 560 - 500 / 3)

    text = Text(Point(600 / 2, 350 - 500 / 3), 'I have a secret door')
    text.draw(win)

    button_1_rec = Rectangle(point_1, point_2)
    button_1 = Button(button_1_rec, door_2_txt)
    button_1.draw(win)

    button_2_rec = Rectangle(point_1, point_2)
    button_2_rec.move(150, 0)
    button_2 = Button(button_2_rec, door_3_txt)
    button_2.draw(win)

    button_3_rec = Rectangle(point_1, point_2)
    button_3_rec.move(-150, 0)
    button_3 = Button(button_3_rec, door_1_txt)
    button_3.draw(win)

    point = win.getMouse()
    rand_num = randint(1, 3)

    if button_1.is_clicked(point) is True:
        if rand_num == 2:
            game_win(button_1, text)
        else:
            lose(button_1, rand_num, text)

    if button_2.is_clicked(point) is True:
        if rand_num == 3:
            game_win(button_2, text)
        else:
            lose(button_2, rand_num, text)

    if button_3.is_clicked(point) is True:
        if rand_num == 2:
            game_win(button_1, text)
        else:
            lose(button_3, rand_num, text)
    win.getMouse()


if __name__ == '__main__':
    main()
