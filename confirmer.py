import pandas as pd
import numbers

def is_confirmed(firstname, lastname, confirmed):
    if isinstance(firstname, numbers.Number) or isinstance(lastname, numbers.Number):
       return 'false'
    
    # firstname first
    namea = firstname + " " + lastname
    if namea in confirmed.values:
        print(namea)
        return 'true'
    # lastname first
    nameb = lastname + " " + firstname
    if nameb in confirmed.values:
        print(nameb)
        return 'true'
    return 'false'

print("reading input data...")
excel_file_1 = "confirmer_data\\input\\cleaned_raw_1.xlsx"
excel_file_2 = "confirmer_data\\input\\cleaned_raw_2.xlsx"
excel_file_confirmed = "confirmer_data\\input\\cleaned_confirmed.xlsx"

basic_raw_1 = pd.read_excel(excel_file_1)
print("read", excel_file_1)
basic_raw_2 = pd.read_excel(excel_file_2)
print("read", excel_file_2)
confirmed_data = pd.read_excel(excel_file_confirmed)
print("read", excel_file_confirmed)


print("searching raw 1...")
basic_raw_1['confirmed'] = basic_raw_1.apply(lambda x: is_confirmed(x['firstname_person'], x['lastname_person'], confirmed_data), axis=1)
print("searching raw 2...")
basic_raw_2['confirmed'] = basic_raw_2.apply(lambda x: is_confirmed(x['firstname_person'], x['lastname_person'], confirmed_data), axis=1)

# ------------
# fetch original sheets and append true/false values to them

print("reading original excel files...")
# Excel file names
excel_file_1 = 'confirmer_data\\raw_data_1.xlsx'
excel_file_2 = 'confirmer_data\\raw_data_2.xlsx'
confirmed_file = 'confirmer_data\\confirmed.xlsx'

# read data into dataframes
raw_data_1 = pd.read_excel(excel_file_1)
print("read", excel_file_1)
raw_data_2 = pd.read_excel(excel_file_2)
print("read", excel_file_2)
confirmed_data = pd.read_excel(confirmed_file, sheet_name=1)
print("read", confirmed_file)

print("appending confirmation status...")
raw_data_1.join(basic_raw_1['confirmed'])
raw_data_2.join(basic_raw_2['confirmed'])

# ------------

print("exporting to excel...")
basic_raw_1.to_excel('confirmer_data\\output\\output_1.xlsx')
basic_raw_2.to_excel('confirmer_data\\output\\output_2.xlsx')

confirmed_raw = basic_raw_1[basic_raw_1['confirmed'] == 'true'].append(basic_raw_2[basic_raw_2['confirmed'] == 'true'])
confirmed_raw.to_excel('confirmer_data\\output\\confirmed_raw.xlsx')

print("exporting data for original excel files...")
raw_data_1 = raw_data_1.to_excel('confirmer_data\\output\\raw_data_1.xlsx', index=False)
raw_data_2 = raw_data_2.to_excel('confirmer_data\\output\\raw_data_2.xlsx', index=False)

print("processing completed")

'''
for item in basic_raw_1.iloc:
    basic_raw_1

# try different orders for [dirty] raw data:
# first name first
tested_names_1a = raw_data_1['firstname_person'] + " " + raw_data_1['lastname_person']
tested_names_2a = raw_data_2['firstname_person'] + " " + raw_data_2['lastname_person']

tested_names_1b = raw_data_1['lastname_person'] + " " + raw_data_1['firstname_person']
tested_names_2b = raw_data_2['lastname_person'] + " " + raw_data_2['firstname_person']



raw_data_1.head()
'''