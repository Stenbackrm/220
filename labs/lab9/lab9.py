"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
from graphics import *

def addTen(nums):
    x = 0
    for _ in nums:
        nums[x] = nums[x] + 10
        x = x + 1

def squareEach(nums):
    x = 0
    for _ in nums:
        nums[x] = nums[x] ** 2
        x = x + 1

def sumList(nums):
    x = 0
    for _ in nums:
        nums[x] = nums[x] ** 2
        x = x + 1
    return sum(nums)

def toNumbers(nums):
    x = 0
    for _ in nums:
        nums[x] = int(nums[x])
        x = x + 1

def writeSumOfSquares():
    num_file = input('what is the file name of the file you would like to use? <nums.txt>: ')
    num_file = open(num_file, 'r')
    out_file = open('num_out_file', "w+")
    for line in num_file:
        num_list = line
        num_list = num_list.split(' ')
        toNumbers(num_list)
        squareEach(num_list)
        print(str(sumList(num_list)))
        out_file.write(str(sumList(num_list)) + '\n')

def leapYear(year):
    return year % 100 != 0 and year % 4 == 0 or year % 400 == 0

def circleOverlap():
    win = GraphWin('circles', 500, 500)

    point_1 = win.getMouse()
    point_2 = win.getMouse()
    rad_1 = ((point_1.getX() - point_2.getX()) ** 2 + (point_1.getY() - point_2.getY()) ** 2) ** .5
    cir_1 = Circle(point_1, rad_1)
    cir_1.draw(win)

    point_1 = win.getMouse()
    point_2 = win.getMouse()
    rad_2 = ((point_1.getX() - point_2.getX()) ** 2 + (point_1.getY() - point_2.getY()) ** 2) ** .5
    cir_2 = Circle(point_1, rad_2)
    cir_2.draw(win)

    dis_p_1 = cir_1.getCenter()
    dis_p_2 = cir_2.getCenter()
    dis = ((dis_p_1.getX() - dis_p_2.getX()) ** 2 + (dis_p_1.getY() - dis_p_2.getY()) ** 2) ** .5
    text = ''
    if dis <= rad_1 + rad_2:
        text = 'the circles overlap'
    else:
        text = 'the circles do not overlap'
    text_box = Text(Point(250, 10), text)
    text_box.draw(win)

    win.getMouse()

def main():
    writeSumOfSquares()
    year = eval(input('enter a year: '))
    #year = 2048
    if leapYear(year) == True:
        print(year, 'is a leap year')
    else:
        print(year, 'is not a leap year')
    circleOverlap()



if __name__ == '__main__':
    main()