"""
Name: Robert Stenback
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_area():
    length = eval(input('enter the length: '))
    width = eval(input('enter the with: '))
    area = length * width
    print("Area =", area)

def calc_volume():
    height = eval(input('enter the height here: '))
    length = eval(input('enter the length here: '))
    depth = eval(input('enter the depth here: '))
    volume = height * length * depth
    print("Volume = ", volume)

def shooting_percentage():
    total_shots = eval(input('enter the total shots of the player here: '))
    shots_made = eval(input('enter the total shots made here: '))
    shot_percent = shots_made / total_shots
    print('Shooting percentage of the player is: ', shot_percent * 100,'%')

def coffee():
    coffee_pounds = eval(input('How many pounds would you like to order?: '))
    coffee_cost = 10.5 * coffee_pounds
    coffee_ship = 0.86 * coffee_pounds
    coffee_total = coffee_cost + coffee_ship + 1.50
    print('Total price of order: ','$',coffee_total)

def  kilometers_to_miles():
    num_kilo = eval(input('how many kilometers did you drive?: '))
    num_miles = num_kilo / 1.61
    print('you will drive',num_miles,"miles on this trip")

def kilo_or_mi():
    miles_or_kilo = input('do you want to calculate miles or kilometers? k/m')
    if miles_or_kilo == "k":
        print("You chose to calculate kilometers")
        num_miles = eval(input('how many miles will you drive?: '))
        fin_kilo = num_miles * 1.61
        print('you will drive',fin_kilo,'kilometers on this trip')
    elif miles_or_kilo == "m":
        print("You chose to calculate miles")
        num_kilo = eval(input('how many kilometers will you drive?: '))
        fin_miles = num_kilo / 1.61
        print('you will drive',fin_miles,'on this trip')
    else:
        print("ERROR You must choose between k or m please try again")
        kilo_or_mi()


