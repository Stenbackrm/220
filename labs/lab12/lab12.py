"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from random import randint

def find_and_remove_first(in_list, value, new_value):
    in_list[in_list.index(value)] = new_value

def read_data(filename):
    file = open(filename, "r")
    full_list = []
    for line in file:
        line_list = line.split(' ')
        full_list = full_list + line_list
    return full_list[0:-1]

def is_in_linear(search_val, values):
    i = 0
    temp = 0
    while i < len(values) and temp != search_val:
        temp = int(values[i])
        i = i + 1
    return temp == search_val

def  good_input():
    user_in = eval(input('enter a number between 1 and 10: '))
    while user_in < 1 or user_in > 10:
        print('that value was not in the range of 1 to 10')
        user_in = eval(input('enter a number between 1 and 10'))
    return user_in

def num_digits():
    user_in = 1
    while user_in >= 1:
        user_in = eval(input('enter a number: '))
        i = user_in
        count = 0
        while i > 1:
            i = i / 10
            count = count + 1
        print(count, 'digits')

def hi_lo_game():
    secret_num = randint(1,100)
    i = 1
    while i < 9:
        guess_num = eval(input('enter a number 1 to 100: '))
        if secret_num == guess_num:
            print('congrats you guessed the number! the number was', guess_num)
            i = 10
        if secret_num < guess_num:
            print('thats not it, your number is too high')
        if secret_num > guess_num:
            print('thats not it your number is too low')

def main():
    prob_list = [2, 34, 234 , 54, 7 ,'hi there', 'my name', 'this is a string', 2, 7, 34,
                   98, 3, 687, 4, 1986, 'this is not a string']
    find_and_remove_first(prob_list, 2, 'ahh')
    print(prob_list)
    print(len(read_data('nums')))
    print(is_in_linear(1065, read_data('nums')))
    good_input()
    print(num_digits())
    hi_lo_game()

main()
