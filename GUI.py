from tkinter import Tk, StringVar, OptionMenu, Text, Button, Label
import os
import Scraper
import sys

csv_files = []
path = os.path.dirname(__file__)
print(path)
files = os.listdir(path)

csv_files = [file for file in files if file.endswith('.csv')]

i = 0
for file in csv_files:
    if file == "Census_Data.csv":
        continue
    print(file, " ", i)
    i += 1

Selected_file = int(input("Select a file based on the number: "))
file = csv_files[Selected_file]

options = Scraper.ReadFirstLine(file)

columns = []
rows = []
# Top level frame
frame = Tk()
frame.title("TextBox Input")
frame.geometry('800x400')
# Function for getting Input
# from textbox and printing it
# at label widget


def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    label.config(text="Provided Input: "+inp)
    inp = inp.split(", ")
    global rows
    rows = inp


# TextBox Creation
def ShowDropDown():
    label.config(text=clicked.get())
    columns.append(clicked.get())


clicked = StringVar()
clicked.set(str(options[0]))

drop = OptionMenu(frame, clicked, *options)
drop.pack()

inputtxt = Text(frame, height=5, width=20)

inputtxt.pack()

# Button Creation
printButton = Button(frame,
                     text="Type in ID numbers seperated like so: 0, 1, etc",
                     command=printInput)
printButton.pack()
# Label Creation
label = Label(frame, text="")
label.pack()
button = Button(frame, text="Add to Search", command=ShowDropDown).pack()

leave = Button(frame, text="cancel", command=sys.exit).pack()
start = Button(frame, text="Begin Proccessing", command=frame.destroy).pack()
frame.mainloop()

num = 0
for row in rows:
    rows[num] = int(row)
    num += 1
print(rows)
columns = list(set(columns))
print(columns)

Scraper.ReadAndOutput(file, columns, rows)
