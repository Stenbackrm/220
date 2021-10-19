"""
Robert Stenback's vigenere cypher
this program encodes text according to a vigenere cypher
"""
from graphics import *

def code(message, keyword):
    acc = ''
    message = message.replace(' ','')
    message = message.upper()
    keyword = keyword.upper()
    for i in range(len(message)):
        c = message[i]
        key = keyword[i % len(keyword)]
        c = ord(c)
        key = ord(key) - 65
        x = c + key
        if x > 90:
            x = x - 26
            x = chr(x)
        else:
            x = chr(x)
        acc = acc + x
    return acc

def main():
    win_width = 500
    win_height = 500
    win = GraphWin('Vigenere Cypher', win_width, win_height)

    msg = 'Message to code:'
    inst = Text(Point(win_width / 2 - 150, win_height - 480), msg)
    inst.draw(win)

    msg_2 = 'Enter Keyword:'
    inst = Text(Point(win_width / 2 - 150, win_height - 420), msg_2)
    inst.draw(win)

    s_box = Entry(Point(win_width / 2 + 100, win_height - 480), 25)
    s_box.setText(' ')
    s_box.draw(win)

    k_box = Entry(Point(win_width / 2 + 100, win_height - 420), 25)
    k_box.setText(' ')
    k_box.draw(win)
    win.getMouse()

    s = s_box.getText()
    k = k_box.getText()


    msg_3 = 'Result: ' + code(s,k)
    inst = Text(Point(win_width / 2 - 150, win_height - 120), msg_3)
    inst.draw(win)

    win.getMouse()

if __name__ == '__main__':
    main()
