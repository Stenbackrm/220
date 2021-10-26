'''
Robert Stenback's weighted average program
this program finds the weighted average of multaple grades from a txt file
'''

def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name , 'r')
    out_file = open(out_file_name, 'w+')
    for line in in_file:
        line_num = line.replace('\n','')
        line_num = line_num.split(':')
        name = line_num[0]
        line_num = line_num[1:]
        line_num = str(line_num)[0:-2]
        line_num = line_num.split()
        line_num = line_num[1:]
        for i in range(0, len(line_num)):
            line_num[i] = int(line_num[i])
        weight = line_num[0::2]
        x = 0
        if sum(weight) == 100:
            acc = 0
            for item in range(int(len(line_num) / 2)):
                wei_grd = int(line_num[x]) * int(line_num[x + 1])
                x = x + 2
                acc = acc + wei_grd
            print(name + "'s average: " + str(round(acc / 100, 1)))
            out_file.write(name + "'s average: " + str(round(acc / 100, 1)) + "\n")
        elif sum(weight) > 100:
            print(name + "'s average: Error: The weights are more than 100.")
            out_file.write(name + "'s average: Error: The weights are more than 100." + "\n")
        else:
            print(name + "'s average: Error: The weights are less than 100.")
            out_file.write(name + "'s average: Error: The weights are less than 100." + "\n")
    print(acc)

def main():
    weighted_average('grades.txt', 'avg.txt')

if __name__ == '__main__':
    main()
