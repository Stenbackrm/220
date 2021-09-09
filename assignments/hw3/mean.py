"""Robert Stenback's Mean calculator
This program calculates the mean with the supplied values
"""
def main():
    values = eval(input('enter each of the values seterated by a comma: '))
    n_of_values = len(values)
    inverses = [1 / x for x in values]
    sum_of_inverse = sum(inverses)
    harmonic_mean = round(n_of_values / sum_of_inverse,3)
    list_square = [y ** 2 for y in values]
    sum_of_square = sum(list_square)
    rms_average = round(((1 / n_of_values) * sum_of_square) ** 0.5, 3)
    list_of_products = 1
    for var_z in values:
       list_of_products = list_of_products * var_z
    geometric_mean = round(list_of_products ** (1 / n_of_values),3)
    print('rms average' ,rms_average,'harmonic mean' ,harmonic_mean,'geometric mean',geometric_mean)
