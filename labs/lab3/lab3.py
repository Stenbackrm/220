"""
Name: Robert
lab3.py
"""

def average():
    num_grade = eval(input("how many grades will you be averaging?:"))
    acc = 0
    x = 1
    for i in range(num_grade):
        homework_x = eval(input('what was your grade on homework ' + str(x)))
        acc = acc + homework_x
        x = x + 1
    final_average = acc / num_grade
    print('your average grade would be:', round(final_average),'%')

def tip_jar():
    acc = 0
    for x in range(5):
        money = eval(input("how much money did you add to the jar?: "))
        acc = acc + money
    print('there are',acc,'dollars in the jar')



def newton():
    x = eval(input('what is the starting value?'))
    ref = eval(input('how many times would you like to refine?'))
    acc = x/2
    for i in range(ref):
        acc = (acc + (x /acc))/2
    print(acc)

def sequence():
    num_of_terms = eval(input('how many terms would you like?:'))
    for x in range(1,num_of_terms + 1):
        x = 1 + (x // 2 * 2)
        print(x, end=' ')

def pi():
    acc = 1
    n = eval(input('how many terms would you like?:'))
    for x in range(n):
        num = 2 + (x // 2 * 2)
        denom = 1 + ((x +1) // 2 * 2)
        acc = acc * (num / denom)
    print(acc * 2)

