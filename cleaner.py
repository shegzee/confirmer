import pandas as pd
import numbers

print("clean data")

print("reading excel files...")
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

# select needed fields
basic_raw_1 = raw_data_1[['hhldcode', 'firstname_person', 'lastname_person']].copy()
basic_raw_2 = raw_data_2[['hhldcode', 'firstname_person', 'lastname_person']].copy()

# print("removing numeric values...")
# indexNumericNames = basic_raw_1[basic_raw_1['firstname_person'].isnumeric()]
# basic_raw_1.drop(indexNumericNames, inplace=True)
# we don't want to drop any rows

print("cleaning useless, annoying titles...")
titles = ['mr', 'mrs', 'dr', 'engr', 'miss', r'\.']
pattern = '|'.join(titles)
basic_raw_1['lastname_person'] = basic_raw_1['lastname_person'].str.replace(pattern, '', case=False)
basic_raw_1['firstname_person'] = basic_raw_1['firstname_person'].str.replace(pattern, '', case=False)
basic_raw_2['lastname_person'] = basic_raw_2['lastname_person'].str.replace(pattern, '', case=False)
basic_raw_2['firstname_person'] = basic_raw_2['firstname_person'].str.replace(pattern, '', case=False)

# convert all to lowercase
print("stripping and converting to lowercase...")
basic_raw_1['firstname_person'] = basic_raw_1['firstname_person'].apply(lambda x: x.strip().lower() if isinstance(x, str) else x)
basic_raw_1['lastname_person'] = basic_raw_1['lastname_person'].apply(lambda x: x.strip().lower() if isinstance(x, str) else x)

basic_raw_2['firstname_person'] = basic_raw_2['firstname_person'].apply(lambda x: x.strip().lower() if isinstance(x, str) else x)
basic_raw_2['lastname_person'] = basic_raw_2['lastname_person'].apply(lambda x: x.strip().lower() if isinstance(x, str) else x)

print("getting names of confirmed...")
# get names of confirmed people
confirmed_names = confirmed_data['Case Name'].copy()
# lowercase confirmed names for comparison
confirmed_names = confirmed_names.apply(lambda x: x.strip().lower() if isinstance(x, str) else x)

print("creating output files")
basic_raw_1.to_excel("confirmer_data\\input\\cleaned_raw_1.xlsx")
basic_raw_2.to_excel("confirmer_data\\input\\cleaned_raw_2.xlsx")
confirmed_names.to_excel("confirmer_data\\input\\cleaned_confirmed.xlsx")
