#!/usr/bin/python3
# to install xlrd, use:  sudo python3 -m pip install xlrd
import operator
import xlrd

book = xlrd.open_workbook("SEC542.xlsx")
default_sheet = book.sheet_by_index(0)


def get_indexed_keywords(sheet):
    index = {}
    print("Processing {0} rows.".format(sheet.nrows))
    for i in range(sheet.nrows):
        # split the tags string
        word_list = sheet.cell_value(rowx=i, colx=1).split(",")
        # get the page number
        pagenum = sheet.cell_value(rowx=i, colx=0)
        # for each word, assign a page(s)
        for word in word_list:
            word_lower = word.lower().strip()
            if index.get(word_lower, None) == None :
                index[word_lower] = [pagenum]
            else :
                #update pagenum / array with duplicate locs where the word appears
                lst = index[word_lower]
                if not pagenum in lst :
                    lst.append(pagenum)
                index[word_lower] = lst
    return index
indexed_keywords = sorted(get_indexed_keywords(default_sheet).items(), key=operator.itemgetter(1))
print(indexed_keywords)