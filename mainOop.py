# main.py > oop

import tkinter as tk
from tkinter import messagebox
from dbinteraction import clientBase

global monthsList, yearsList
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

class tootsies:
	
	def __init__(self, master):
		self.master = master
		self.master.title("Tootsies")
		self.master.geometry("1000x500")
	def searchdbname(name):
    	pass

	def searchdbdate(month, year):
	    pass
	
	def addClient():
	    bigtittygothgirl()
	
	def dateSearch():
	    searchField.delete(0, END)
	    searchdbdate(clickedMonth.get(), clickedYear.get())
	
	def nameSearch():
	    clickedYear.set(years[0])
	    clickedMonth.set(months[0])
	    searchdbname(searchField.get())
	
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



		self.newButton = tk.Button(self.gayFrame, text="add client", command=self.newWindow)
		self.newButton.pack()
		

	def newWindow(self):
		self.newWindow = tk.Toplevel(self.master)
		self.app = addForm(self.newWindow)

class addForm:

	def __init__(self, master):
		self.master = master
		self.master.title("Add New Client")
		self.form = tk.Frame(self.master)
		self.clickedMonth = tk.IntVar()
		self.clickedYear = tk.IntVar()
		self.clickedMonth.set(monthsList[0])
		self.clickedYear.set(yearsList[0])
		self.nameLabel = tk.Label(self.form, text="Name:")
		self.firstNameEntry = tk.Entry(self.form, font=('default', 12), width=20)
		self.lastNameEntry = tk.Entry(self.form, font=('default', 12), width=20)
		self.monthLabel = tk.Label(self.form, text="Month:")
		self.monthDropdown = tk.OptionMenu(self.form, self.clickedMonth, *monthsList)
		self.yearLabel = tk.Label(self.form, text="Year:")
		self.yearDropdown = tk.OptionMenu(self.form, self.clickedYear, *yearsList)
		self.commentLabel = tk.Label(self.form, text="Comments:")
		self.commentEntry = tk.Text(self.form, height=5)	
		self.addButton = tk.Button(self.form, text="Add", command=self.addClient)

		self.nameLabel.grid(row=0, column=0)
		self.firstNameEntry.grid(row=0, column=1)
		self.lastNameEntry.grid(row=0, column=2)
		self.monthLabel.grid(row=1, column=0)
		self.monthDropdown.grid(row=1, column=1)
		self.yearLabel.grid(row=2, column=0)
		self.yearDropdown.grid(row=2, column=1)
		self.commentLabel.grid(row=3, column=0)
		self.commentEntry.grid(row=3, column=1)
		self.addButton.grid(row=4, column=0)
		self.form.pack()

	def addClient(self):
		if len(self.firstNameEntry.get()) <= 1:
			self.firstNameError = messagebox.showerror("Name Error", "Invalid First Name")
		elif len(self.lastNameEntry.get()) <= 1:
			self.lastNameError = messagebox.showerror("Name Error", "Invalid Last Name")
		else:
			self.values = ( self.firstNameEntry.get(),
							self.lastNameEntry.get(),
							self.monthDropdown.get(),
							self.yearDropdown.get(),
							self.commentEntry.get()
						  )

			self.tootsies = clientBase()
			self.tootsies.addDB(self.values)
			self.master.destroy()# close 'add client form' window


def main():
	master = tk.Tk()
	app = tootsies(master)
	master.mainloop()

main()