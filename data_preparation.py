import pandas as pd

def prepare_data(file):
 xls=pd.ExcelFile(file)
 df=pd.read_excel(file,sheet_name='Query1')
 return df
