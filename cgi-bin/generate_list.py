#! /bin/python

import glob
import billmodel
import yate

data_files = glob.glob("data/*.txt")
bill_lists_month = billmodel.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("账单"))
print(yate.start_form("generate_bill_data.py"))
print(yate.para("查看某个月份的账单："))
for each_month in bill_lists_month:
    print(yate.radio_button("selected_month", bill_lists_month[each_month].month))
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))
