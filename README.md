# CSV scraper
A CSV scraper made in python specifically made for Canadian Census Data 
## Now With A GUI

## How to install and use

### 1. Clone the reprository
```md
git clone https://github.com/Rafififi/Census-Data-Scraper
```

### 2. install tkinter and pandas

### 3. Run GUI.py

```md
python3 GUI.py
```

### 4. Use The Drop Down Menu To Select Columns

### 5. Use the Text Box To Select Rows

### 6. Press Begin Proccess And Wait

## How to Modify



### To Modify For Other Files Change Scraper.py

```py
Census_Data = Census_Data[Census_Data.CHARACTERISTIC_ID.isin(rows)]
```

Change CHARACTERISTIC_ID to the Column that contains the value in the row that is being looked at
