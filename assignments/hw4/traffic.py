'''
Robert Stenback's traffic averages
this program finds the average traffic on streets given by the user
'''

def main():
    road_num = eval(input('how many roads were surveyed?: '))
    road = 1
    acc_total = 0
    for _ in range(road_num):
        day_num = 1
        acc_cars = 0
        days = eval(input('how many days was road ' + str(road) + ' surveyed?:'))
        road = road + 1
        for _ in range(days):
            cars = eval(input('how many cars were seen on day ' + str(day_num) + '?'))
            acc_cars = acc_cars + cars
            acc_total = acc_total + cars
            day_num = day_num + 1
        average_cars = round(acc_cars / days,2)
        print('road ',road,' average cars per day: ',average_cars)
    average_total = round(acc_total / road_num,2)
    print('total number of vehicles: ', acc_total)
    print('average number of vehicles per road: ', average_total)

if __name__ == '__main__':
    main()
