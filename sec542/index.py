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
            if index.get(word_lower, None) == None:
                index[word_lower] = [pagenum]
            else :
                #update pagenum / array with duplicate locs where the word appears
                lst = index[word_lower]
                if not pagenum in lst:
                    lst.append(pagenum)
                    index[word_lower] = lst
    return index

def check_index_type(index):
    if type(indexed_keywords) is not dict: raise Exception(
        'Dictionary type expected, but got: ' + str(type(indexed_keywords)
    ))

def sort_index(indexed_keywords):
    check_index_type(indexed_keywords)
    return sorted(indexed_keywords.items(), key=operator.itemgetter(1))

def display(indexed_keywords):
    check_index_type(indexed_keywords)
    for key, value in indexed_keywords:
        print(key, value)

indexed_keywords = get_indexed_keywords(default_sheet)

sorted = sort_index(indexed_keywords)

display(sorted)