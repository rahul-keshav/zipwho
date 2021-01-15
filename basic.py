import pandas as pd
sheet =  pd.read_excel('NJ_ZipCode_List_lookup.xlsx')

def sheet_length():
    return len(sheet.index)
def city(i):
    return sheet.iloc[i,0]
def zip_code(i):
    return sheet.iloc[i,1]
def county(i):
    return sheet.iloc[i,2]

