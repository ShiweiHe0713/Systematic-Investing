import pandas as pd
import matplotlib
import seaborn as sbn
import openpyxl

# Acess sheet 1, set 2nd as the header for dataframe
file = '../0_data/COUNTER_TREND_DATA.xlsx'
df = pd.read_excel(file, sheet_name=0, header=1)

print(df.head())