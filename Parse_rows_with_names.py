import pandas as pd

#In this line select the file
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
#Open the cesnus data file and only look at the sections that are needed
Census_Data = pd.read_csv(CSV_FILE, usecols=columns, encoding='latin-1')


#Look for specific charateristic_IDs
#only look at data with the characteristic_IDs of 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#This is because the data that is needed is only in these charateristic_IDs
Census_Data = Census_Data[Census_Data.CHARACTERISTIC_ID.isin(rows)] #instead of CHARACTERISTIC_ID, use the column that contains the rows that are needed

#Get the data that are associated with the ID

#Write the data into a new file
Census_Data.to_csv('Census_Data.csv', index=False)