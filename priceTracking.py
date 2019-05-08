import csv


with open('WW Price List-InTouch.csv', 'r', encoding="ANSI") as pricing:
    wwlist = csv.reader(pricing)

    priceList_list = []
    priceList_dict = {}

    ## This is not required, just showing
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
           continue
        
        if start_tracking == True:
            priceList_list.append([
                row[partNum_idx], # Part No
                row[listPrice_idx], # Original Price
                row[newListPrice_idx] # New Price
                ])

            ## Dictionary form
            priceList_dict[row[partNum_idx]] = row[partNum_idx] # Part No
            priceList_dict[row[partNum_idx]] = {} # Nest Dictionary for new keys
            priceList_dict[row[partNum_idx]]['ListPrice'] = row[listPrice_idx] # Original Price
            priceList_dict[row[partNum_idx]]['NewPrice'] = row[newListPrice_idx] # New Price

    print(priceList_list)
    print(priceList_dict)
    
