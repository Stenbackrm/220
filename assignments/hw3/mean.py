"""Robert Stenback's Mean calculator
This program calculates the mean with the supplied values
"""

def main():
    n_of_values = eval(input('how many values are you averaging?:'))
    acc = 0
    acc_in = 0
    acc_s = 0
    acc_p = 1
    for i in range(n_of_values):
        values = eval(input('what is value '))
        inverses = 1 / values
        acc_in = acc_in + inverses
        squares = values ** 2
        acc_s = acc_s + squares
        acc_p = acc_p * values
        acc = acc + values
    harmonic_mean = round(n_of_values / acc_in, 3)
    rms_average = round(((1 / n_of_values) * acc_s) ** 0.5, 3)
    geometric_mean = round(acc_p ** (1 / n_of_values), 3)
    print(rms_average)
    print(harmonic_mean)
    print(geometric_mean)
if __name__ == '__main__':
    main()