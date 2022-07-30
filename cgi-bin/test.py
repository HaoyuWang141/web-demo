from billmodel import *

# a = get_bill('data.txt')
# print(len(a))
# for day in a:
#     print(day.date)
#     for a_bill in day:
#         print(a_bill.person,a_bill.money)
#     print()

put_to_store(['data.txt'])
a = get_from_store()
a['July'].print()