#!/usr/bin/python3
# to install xlrd, use:  sudo python3 -m pip install xlrd
import xlrd

book = xlrd.open_workbook("SEC542.xlsx")
default_sheet = book.sheet_by_index(0)
index = {}

def get_indexed_keywords(sheet):
    print("Processing {0} rows.".format(sheet.nrows))
    for i in range(sheet.nrows):
        # split the tags string
        wordArray = sheet.cell_value(rowx=i, colx=1).split(",")
        # get the page number
        pagenum = sheet.cell_value(rowx=i, colx=0)
        # for each word, assign a page
        for word in wordArray:
            lowerWord = word.lower().strip()
            print(lowerWord, pagenum, word in wordArray)
            if word in wordArray:
                a = index.get(lowerWord, 'nope')
            #index[lowerWord] = [pagenum]
    sortedIndex = sorted(index)
    print(sortedIndex)

get_indexed_keywords(default_sheet)