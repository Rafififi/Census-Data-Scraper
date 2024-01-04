import pandas as pd

CSV_FILE = input("Enter the name of the file: ")

column = input("Enter the column that is needed or press enter to leave: ")
columns = []
while column != "":
    columns.append(column)
    column = (input("Enter the column that is needed or press enter to leave: "))


row = input("Enter the row that is needed or press enter to leave: ")
rows = []
while row != "":
    rows.append(row)
    row = (input("Enter the row that is needed or press enter to leave: "))
print(rows)

Census_Data = pd.read_csv(CSV_FILE, usecols=columns, encoding='latin-1')



Census_Data = Census_Data[Census_Data.CHARACTERISTIC_ID.isin(rows)] #instead of CHARACTERISTIC_ID, use the column that contains the rows that are needed


Census_Data.to_csv('Census_Data.csv', index=False)