"""
Name: Robert Stenback
<ProgramName>.py
"""

from graphics import Rectangle
from graphics import Point


def binary_search(value, in_list):
    left = 0
    right = len(in_list) - 1
    while left <= right:
        middle = (left + right) // 2
        middle_vale = int(in_list[middle])
        if value == middle_vale:
            return True
        if value < middle_vale:
            right = middle - 1
        if value > middle_vale:
            left = middle + 1
    return False


def selection_sort(values):
    for i in range(len(values)):
        low = values[i]
        pos = i
        for j in range(i, len(values)):
            if values[j] < low:
                low = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]
    return values


def rect_sort(rectangles):
    d = {}
    areas = []
    for rect in rectangles:
        d[rect.getArea()] = rect
        areas.append(rect.getArea())
    selection_sort(areas)
    for i in range(len(areas)):
        values[i] = d[areas[i]]
    print(areas)

def file_to_list(file):
    in_file = open(file, 'r')
    data = in_file.read().split()
    for i in range(len(data)):
        data[i] = int(data[i])
    return data

def trade_alert(filename):
    data = file_to_list(filename)
    for i in range(len(data)):
        if data[i] > 830:
            print('Warning!! 830 exceeded at', i, 'seconds!')
        elif data[i] > 500:
            print('alert! 500 exceeded at', i, 'seconds!')


def main():
    val = [4,34,1,23,45,6,7,8,3,32]
    print(selection_sort(file_to_list('trades.txt')))
    trade_alert('trades.txt')


if __name__ == '__main__':
    main()
