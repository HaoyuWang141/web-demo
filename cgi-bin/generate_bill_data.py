#! /bin/python3

import cgi

import cgitb
cgitb.enable()

import billmodel
import yate

bill_lists_month = billmodel.get_from_store()

form_data = cgi.FieldStorage()
selected_month = form_data['selected_month'].value

print(yate.start_response())
print(yate.include_header(selected_month + " 账单："))    
#print(yate.header("账单："))
#print(yate.para(bill_lists_month[month].month))
for bill_list_day in bill_lists_month[selected_month]:
    print(yate.para(bill_list_day.date))
    print(yate.u_list(bill.person + '&nbsp&nbsp&nbsp&nbsp' + bill.money for bill in bill_list_day))
    print(yate.para('&nbsp&nbsp&nbsp&nbsp'))
print(yate.include_footer({"Home": "/index.html",
                           "Select another bill": "generate_list.py"}))

