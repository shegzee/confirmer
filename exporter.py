import pandas as pd

# fetch original sheets and append true/false values to them

print("reading output excel files...")
basic_raw_1 = pd.read_excel('confirmer_data\\output\\output_1.xlsx')
basic_raw_2 = pd.read_excel('confirmer_data\\output\\output_2.xlsx')

print("reading original excel files...")
excel_file_1 = 'confirmer_data\\raw_data_1.xlsx'
excel_file_2 = 'confirmer_data\\raw_data_2.xlsx'
confirmed_file = 'confirmer_data\\confirmed.xlsx'

# read data into dataframes
raw_data_1 = pd.read_excel(excel_file_1)
raw_data_2 = pd.read_excel(excel_file_2)
# confirmed_data = pd.read_excel(confirmed_file, sheet_name=1)
# print("read", confirmed_file)

print("appending confirmation status...")
raw_data_1 = raw_data_1.join(basic_raw_1['confirmed'])
raw_data_2 = raw_data_2.join(basic_raw_2['confirmed'])


print("exporting data for original excel files...")
raw_data_1.to_excel('confirmer_data\\output\\raw_data_1.xlsx', index=False)
raw_data_2.to_excel('confirmer_data\\output\\raw_data_2.xlsx', index=False)