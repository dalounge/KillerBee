import csv
with open('WW Price List-InTouch.csv', 'r', encoding="ANSI") as pricing:
    wwlist = csv.reader(pricing)

    price_list = []
    partNum_idx = None
    listPrice_idx = None
    newListPrice_idx = None
    start_tracking = False

    for row in wwlist:
        if row[0] == 'offering':
           partNum_idx = row.index('partnumber')
           listPrice_idx = row.index('listprice')
           newListPrice_idx = listPrice_idx + 1
           start_tracking = True
        
        if start_tracking == True:
            price_list.append([row[partNum_idx], row[listPrice_idx], row[newListPrice_idx]])

    print(price_list)
