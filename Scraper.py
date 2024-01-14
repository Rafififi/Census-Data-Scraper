import pandas as pd


# reads the first row with data so that we can get the number of columns
def ReadFirstLine(file):
    df = pd.read_csv(file, nrows=1, encoding='latin-1')
    columns = df.columns.tolist()
    return columns


# read through the select columns and put the looked for values in a new CSV
def ReadAndOutput(file, columns, rows):
    Census_Data = pd.read_csv(file, usecols=columns, encoding='latin-1')
    Census_Data = Census_Data[Census_Data.CHARACTERISTIC_ID.isin(rows)]
    Census_Data.to_csv('Census_Data.csv', index=False)
