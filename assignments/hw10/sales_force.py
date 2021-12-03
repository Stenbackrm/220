"""
Robert Stenback's sales force class
"""
from sort_alg import selection_sort
from sales_person import SalesPerson

class SalesForce:

    """
    this class...
    """

    def __init__(self):
        self.sales_people = []
    def add_data(self,file_name):
        in_file = open(file_name, 'r')
        acc = 0
        for line in in_file:
            temp = line.split(',')
            sales = temp[2].split()
            self.sales_people.append(SalesPerson(temp[0], temp[1][1:]))
            for i in sales:
                self.sales_people[acc].enter_sale(i)
            acc += 1

    def quota_report(self, quota):
        quota_list = []
        for i in self.sales_people:
            temp = []
            temp.append(i.get_id())
            temp.append(i.get_name())
            temp.append(i.total_sales())
            total = i.total_sales()
            if total >= quota:
                temp.append(True)
            else:
                temp.append(False)
            quota_list.append(temp)
        return quota_list

    def top_seller(self):
        sales_dict = {}
        sales_totals = []
        for i in self.sales_people:
            total, person = i.total_sales, i
            sales_dict[total] = person
        for i in sales_dict:
            sales_totals.append(i)
        print(sales_totals)




def main():
    walmart = SalesForce()
    walmart.add_data("salesData.txt")
    print(walmart.quota_report(100))
    walmart.top_seller()
if __name__ == '__main__':
    main()

