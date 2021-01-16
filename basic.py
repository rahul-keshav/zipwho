import pandas as pd
sheet =  pd.read_excel('NJ_ZipCode_List_lookup.xlsx')

def sheet_length():
    return len(sheet.index)
def city(i):
    return sheet.iloc[i,0]
def zip_code(i):
    k = sheet.iloc[i,1]
    return str(k)
def county(i):
    return sheet.iloc[i,2]
# clmn=["City","Zip Code","County","Median Income","Cost Of Living Index","Median Mortgage To Income Ratio","Owner Occupied Homes","Median Rooms In Home","College Degree","Professional","Population","Average Household Size","Median Age","Male To Female Ratio","Married","Divorced","White","Black","Asian","Hispanic Ethnicity"]

dict1 = {
        "City":[],
        "Zip Code":[],
        "County":[],
        "Median Income":[],
        "Cost Of Living Index ($)":[],
        "Median Mortgage To Income Ratio (%)":[],
        "Owner Occupied Homes (%)":[],
        "Median Rooms In Home":[],
        "College Degree (%)":[],
        "Professional (%)":[],
        "Population":[],
        "Average Household Size":[],
        "Median Age":[],
        "Male To Female Ratio (%)":[],
        "Married (%)":[],
        "Divorced (%)":[],
        "White (%)":[],
        "Black (%)":[],
        "Asian (%)":[],
        "Hispanic Ethnicity (%)":[],
        }

clmn = list(dict1.keys())

def save_cred(output_data):
    try:
        df2 = pd.read_csv('zipcode.csv')
    except:
        df2 = pd.DataFrame(dict1)
    
    df0 = pd.DataFrame([output_data], columns=clmn)
    df = df2.append(df0,ignore_index=True)    
    df.to_csv('zipcode.csv',index=False)
    print('data saved')