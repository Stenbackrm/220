"""
Name: Robert Stenback
lab2.py
"""
def sum_of_threes():
    upper_bound = eval(input('enter an upper bound for the operation here:'))
    acc = 0
    for x in range(0,upper_bound + 1,3):
        acc = x + acc
    print(acc)

def muliplication_table():
    for h in range(1,11):
        print()
        for l in range(1,11):
            print(h * l,end=" ")

def triangle_area():
    a_side = eval(input('what is the length of side A?:'))
    b_side = eval(input('what is the length of side B?: '))
    c_side = eval(input('what is the length of side C?: '))
    s = (a_side + b_side + c_side) / 2
    area = (s * (s - a_side) * (s - b_side) * (s - c_side)) ** 0.5
    print('the area of the triangle is:',area)

def sumSquares():
    lower = eval(input('what is the lower bound?: '))
    upper = eval(input('what is the upper bound?: '))
    acc = 0
    for x in range(lower,upper + 1):
        acc = acc + x ** 2
    print(acc)

def power():
    num = eval(input('what number are you starting with?:'))
    expo = eval(input('what power are you raising it to?: '))
    acc = 1
    for x in range(0,expo):
        acc = acc * num
    print(acc)

