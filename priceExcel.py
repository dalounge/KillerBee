import csv
from openpyxl import Workbook, load_workbook

path = 'c:\\PriceListReader\\Copy of v2017 Wonderware Price List Update for CS 1_2018.xlsx'

wb = load_workbook(path)

wbHist = wb['Historian 2017']

get_values = False
get_indexes = False
prices = {}
listPrice_idx = None
partNo_idx = None
partNo_name = None

for row_cells in wbHist.iter_rows():
    if get_indexes:
        get_indexes = False
        get_values = True
    
    for cells in row_cells:
        if cells.value == 'Part Description':
            get_indexes = True
            continue
        
        if get_indexes:
            if cells.value == 'Part Number':
                partNo_idx = cells.column
                continue
                
            elif cells.value == 'List Price':
                listPrice_idx = cells.column
                continue
        
        if get_values:
            if cells.column == partNo_idx:
                prices[cells.value] = {}
                partNo_name = cells.value
                continue
                
            elif cells.column == listPrice_idx:
                prices[partNo_name]['ListPrice'] = cells.value
                prices[partNo_name]['Location'] = [cells.column, cells.row]
                continue
                
            elif cells.value == '':
                get_values = False
                get_indexes = False
                listPrice_idx = None
                partNo_idx = None
                partNo_name = None
                break
                
print(prices)
