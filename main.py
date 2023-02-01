from tkinter import *
from dbinteraction import clientBase
from addForm import bigtittygothgirl
# from test import footjob
import test

def searchdbname(name):
    pass

def searchdbdate(month, year):
    pass

def addClient():
    # bigtittygothgirl()
    footjob()

def dateSearch():
    searchField.delete(0, END)
    searchdbdate(clickedMonth.get(), clickedYear.get())

def nameSearch():
    clickedYear.set(years[0])
    clickedMonth.set(months[0])
    searchdbname(searchField.get())

root = Tk()
root.title('root')
root.geometry("1000x500")

LF = Frame(root, width=179)
LF.configure(background='blue')
dateFrame = Frame(LF)
nameFrame = Frame(LF)

months = [
    "All",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
# datatype of menu text
clickedMonth = StringVar()
# initial menu text
clickedMonth.set(months[0])
# Create Dropdown menu
monthMenu = OptionMenu(dateFrame, clickedMonth, *months )

years = [
    "All",
    "2023",
    "2022",
    "2021",
    "2020"
]
# datatype of menu text
clickedYear = StringVar()
# initial menu text
clickedYear.set(years[0])
# Create Dropdown menu
yearMenu = OptionMenu(dateFrame, clickedYear, *years )
searchButton2 = Button(dateFrame, text='Search', font=('default', 7), command=dateSearch)

searchField = Entry(nameFrame, font=('default', 12))
searchButton1 = Button(nameFrame, text='Search', font=('default', 7), command=addClient)#command=nameSearch

monthMenu.pack(side=LEFT, padx=3, pady=3)
yearMenu.pack(side=LEFT, padx=3, pady=3)
searchButton2.pack(side=RIGHT, pady=3)
dateFrame.grid_propagate(1)
dateFrame.grid(row=0, column=0, columnspan=2, pady=3, sticky='wne')

searchField.grid(row=0, column=0)
searchButton1.grid(row=0, column=1)
nameFrame.grid(row=1, column=0, columnspan=2, pady=3, sticky='wne')

LF.pack(side=LEFT, fill=Y)

root.mainloop()
