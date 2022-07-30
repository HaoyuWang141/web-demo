class Bill():
    def __init__(self, date, person, money):
        self.date = date
        self.person = person
        self.money = money
        
class BillList(list):
    def __init__(self):
        list.__init__([])
        self.sum = 0
    def get_sum(self):
        sum = 0
        for bill in self:
            sum += bill.money
        return sum
    def print(self):
        for bill in self:
            print(bill.person, bill.money)
        
class BillListDay(BillList):
    def __init__(self, date=None):
        BillList.__init__(self)
        self.date = date
    def print(self):
        print(self.date)
        super().print()
        
class BillListMonth(BillList):
    def __init__(self, month=None):
        BillList.__init__(self)
        self.month = month
    def get_sum(self):
        sum = 0
        for day in self:
            sum += day.get_sum()
        return sum
    def print(self):
        print('month:\t' + self.month + '\n')
        for a_day in self:
            print('date:\t' + a_day.date)
            for a_bill in a_day:
                print(a_bill.person + '\t' + a_bill.money)
            print()
