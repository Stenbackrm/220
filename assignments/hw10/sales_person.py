"""
Robert Stenback's sales person class file
"""


class SalesPerson:

    """
    this class ...
    """

    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        sale = int(sale)
        self.sales.append(sale)

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return quota <= self.total_sales()

    def compare_to(self, other):
        if self.total_sales() < other.total_sales():
            return -1
        if self.total_sales() > other.total_sales():
            return 1
        else:
            return 0

    def __str__(self):
        return "{0}-{1} {2}".format(self.get_id(), self.get_name(), self.get_sales())


