'''Robert Stenback's annual interst assignment
This program calculates the annual interest rate given the proper information
'''

def main():
    annual_interest = eval(input('what is the annual interest rate? please enter:'))
    annual_interest_decimal = annual_interest /100
    billing_cycle = eval(input('how many days are in a billing cycle?: '))
    p_net_balance = eval(input('what was the previous net balance?: '))
    payment = eval(input('what is the payment amount?: '))
    date_of_payment = eval(input('what was the day of the month that the payment was made?''(enter only a number):'))
    days_left_in_cycle = billing_cycle - date_of_payment
    step_1 = p_net_balance * billing_cycle
    step_2 = payment * days_left_in_cycle
    step_3 = step_1 - step_2
    average_daily_balance = step_3 / billing_cycle
    monthly_interest_rate = annual_interest_decimal / 12
    monthly_interest_charge = round(average_daily_balance * monthly_interest_rate,2)
    print(monthly_interest_charge)
