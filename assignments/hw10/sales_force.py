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
        ranking = []
        for i in self.sales_people:
            total, person = i.total_sales(), i
            sales_dict[total] = person
        for i in self.sales_people:
            sales_totals.append(i.total_sales())
        selection_sort(sales_totals)
        for i in range(len(sales_totals)):
            ranking.append(sales_dict[sales_totals[i]])
        rank_index = []
        if sales_totals[-1] == sales_totals[-2]:
            for i in range(len(sales_totals) - 1):
                if sales_totals[-1] == sales_totals[i]:
                    rank_index.append(i)
            selection_sort(rank_index)
            return [ranking[rank_index[0]:]]
        return [ranking[-1]]

    def individual_sales(self, employee_id):
        id_dict = {}
        for i in self.sales_people:
            list_id, person = i.get_id(), i
            id_dict[list_id] = person
        try:
            return id_dict[employee_id]
        except KeyError:
            return None


def main():
    walmart = SalesForce()
    walmart.add_data("salesData.txt")
    print(walmart.quota_report(100))
    print(walmart.top_seller())
    print(walmart.individual_sales(345))
if __name__ == '__main__':
    main()
