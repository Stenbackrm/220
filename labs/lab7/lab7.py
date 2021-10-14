"""
Name: Robert Stenback
Partner: <your partner's name goes here – first and last>
lab7.py
"""
import math
def cash_conversion():
    user = eval(input('enter a number here: '))
    print('${:.2f}'.format(user))

def encode():
    s = input('enter your text here: ')
    k = eval(input('enter your key here: '))
    acc = ''
    for c in s:
        i = ord(c)
        x = k + i
        c = (chr(x))
        acc = acc + c
    print(acc)

def sphere_area(radius):
    A = 4 * math.pi * (radius ** 2)
    return(A)

def sphere_volume(radius):
    V = (3/4) * math.pi * (radius ** 2)
    return(V)

def sphere():
    print(sphere_area(3))
    print(sphere_volume(5))

def sum_n(n):
    sum_of_sequence = (n * (n+1)) / 2
    return(sum_of_sequence)

def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        cube_sums = i ** 3
        acc = cube_sums + acc
    return acc

def sums():
    print(sum_n(3))
    print(sum_n_cubes(3))

def encode_better():
    s = input('enter your sentence/word here: ')
    k = input('enter your key here')
    acc = ''
    for i in range(len(s)):
        c = s[i]
        key = k[i % len(k)]
        c = ord(c)
        key = ord(key) - 97
        x = key + c
        x = chr(x)
        acc = acc + x
    print(acc)


def main():
    # cash_conversion()
    # encode()
    # sphere()
    # sums()
    # encode_better()
    pass


main()
