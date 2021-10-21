"""
Name: Robert Stenback
lab8.py
"""

from encryption import encode
from encryption import encode_better

def number_words(in_file_name , out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w+')
    x = 1
    for line in in_file:
        words = line.split()
        for word in words:
            out_file.write(str(x) + ' ' + word + '\n')
            x = x + 1
    out_file.close()

def wage(in_file, out_file):
    in_file = open(in_file, "r")
    out_file = open(out_file, "w+")
    for line in in_file:
        parts = line.split()
        wage = float(parts[2]) + 1.65
        total = wage * int(parts[3])
        out_file.write(parts[0] + ' ' + parts[1] + ' ' + str(total) + '\n')

def calculator(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc = acc + (pos * int(isbn[i]))
    return acc

def send_message(file, friend):
    in_file = open(file , 'r')
    out_file = open(friend , 'w+')
    for line in in_file:
        out_file.write(line)
    out_file.close()

def send_safe_message(file, friend, key):
    in_file = open(file, 'r')
    out_file = open(friend, 'w+')
    for line in in_file:
        out_file.write(encode(line, key))
    out_file.close()

def send_uncrackable_message(file, friend, pad):
    in_file = open(file, 'r')
    out_file = open(friend, 'w+')
    pad_file = open(pad, 'r')
    key = pad_file.read()
    for line in in_file:
        out_file.write(encode_better(line, key))
    out_file.close()

def main():
    number_words('Walrus.txt' , 'word_num.txt')
    print(calculator('0072946520'))
    wage('hourly_wages.txt', 'new_wages.txt')
    send_message('Walrus.txt', 'friend.txt')
    send_safe_message('Walrus.txt', 'secret_message.txt', 3)
    send_uncrackable_message('Walrus.txt', 'safest_message.txt', 'pad.txt')
    pass


main()
