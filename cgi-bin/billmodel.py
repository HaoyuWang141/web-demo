#from asyncio.windows_events import NULL
import pickle
import bill

def get_bill(filename):
    try:
        bill_list_month = bill.BillListMonth()
        bill_list_day = bill.BillListDay()
        with open(filename, 'r') as f:
            bill_list_month.month = f.readline().strip()
            line = f.readline()
            day = ''
            while line:
                if line.find(' ') == -1:
                    if not len(bill_list_day) == 0:
                        bill_list_month.append(bill_list_day)
                    day = line.strip()
                    bill_list_day = bill.BillListDay(day)
                else:
                    line = line.strip().split()
                    bill_list_day.append(bill.Bill(day, line[0], line[1]))
                line = f.readline()
                
            if not len(bill_list_day) == 0:
                bill_list_month.append(bill_list_day)
    except IOError as ioerr:
        print('IOError(get_bill)' + str(ioerr))
    except:
        print('other error in bill_list')
    return bill_list_month
                
def put_to_store(files_list):
    all_bill_lists_month = {}
    for each_file in files_list:
        bill_list_month = get_bill(each_file)
        all_bill_lists_month[bill_list_month.month] = bill_list_month
    try:
        with open('bill.pickle', 'wb') as bf:
            pickle.dump(all_bill_lists_month, bf)
    except IOError as ioerr:
        print('File error(put_and_store):' + str(ioerr))
    return(all_bill_lists_month)
    
def get_from_store():
    all_bill_lists_month  = {}
    try:
        with open('bill.pickle', 'rb') as bf:
            all_bill_lists_month = pickle.load(bf)
    except IOError as ioerr:
        print('File error(get_from_store):' + str(ioerr))
    return(all_bill_lists_month)