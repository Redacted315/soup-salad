from tkinter import *
from dbinteraction import clientBase


def checkFieldsValid():
	if nameEntry.get().len() > 1 and monthDropdown.get() > 0 and yearDropdown.get() > 0:
		print("All Fields Are Valid")
		return True
	else:
		return False

def add():
	if not checkFieldsValid():
		print("one or more fields are not valid")
	else:
		# bigtittygothgirl = clientBase()
		# bigtittygothgirl.addClient(nameEntry.get(), monthDropdown.get(), yearDropdown.get(), commentEntry.get(0, END))
		print("bigtittygothgirl")
	
def bigtittygothgirl():
	monthsList = [
	1,
	2,
	3,
	4,
	5,
	6,
	7,
	8,
	9,
	10,
	11,
	12
	]
	
	yearsList = [
	2023,
	2022,
	2021,
	2020,
	2019,
	2018,
	2017,
	2016,
	2015,
	2014,
	2013,
	2012
	]
	
	window = Tk()
	window.title("window")
	# window.geometry("300x300")
	
	clickedMonth = IntVar()
	clickedYear = IntVar()
	clickedMonth.set(monthsList[0])
	clickedYear.set(yearsList[0])
	
	nameLabel = Label(window, text="Name:")
	nameEntry = Entry(window, font=('default', 12), width=20)
	
	monthLabel = Label(window, text="Month:")
	monthDropdown = OptionMenu(window, clickedMonth, *monthsList)
	
	yearLabel = Label(window, text="Year:")
	yearDropdown = OptionMenu(window, clickedYear, *yearsList)
	
	commentLabel = Label(window, text="Comments:")
	commentEntry = Text(window, height=5)
	
	addButton = Button(window, text="Add", command=add)
	
	# nameLabel.pack(side=TOP, anchor=W, padx=5)
	# nameEntry.pack(side=TOP, anchor=W)
	# monthLabel.pack(side=TOP, anchor=W, padx=5)
	# monthDropdown.pack(side=TOP, anchor=W)
	# yearLabel.pack(side=TOP, anchor=W, padx=5)
	# yearDropdown.pack(side=TOP, anchor=W)
	# commentLabel.pack(side=TOP, anchor=W, padx=5)
	# commentEntry.pack(side=TOP, anchor=W, padx=5)
	# addButton.pack(side=BOTTOM, padx=5)
	
	nameLabel.grid(row=0, column=0)
	nameEntry.grid(row=0, column=1)
	monthLabel.grid(row=1, column=0)
	monthDropdown.grid(row=1, column=1)
	yearLabel.grid(row=2, column=0)
	yearDropdown.grid(row=2, column=1)
	commentLabel.grid(row=3, column=0)
	commentEntry.grid(row=3, column=1)
	addButton.grid(row=4, column=0)


	window.mainloop()
