import tkinter as tk
from tkinter import messagebox
from dbinteraction import clientBase
from datetime import datetime
from tkinter import ttk

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
		
		self.searchFrame = tk.Frame(self.master, width=179)
		self.searchFrame.configure(background='blue')
		self.dateFrame = tk.Frame(self.searchFrame)
		self.nameFrame = tk.Frame(self.searchFrame)
		
		self.clickedMonth = tk.IntVar()
		# set 'default' month text to current month
		self.currentMonth = datetime.now().month
		self.clickedMonth.set(monthsList[(self.currentMonth - 1)])# offset currentMonth to match list indicies
		self.monthMenu = tk.OptionMenu(self.dateFrame, self.clickedMonth, *monthsList )
		
		self.clickedYear = tk.IntVar()
		# self.currentYear = datetime.now().year # ill cross this bridge when i get to it
		self.clickedYear.set(yearsList[0])
		self.yearMenu = tk.OptionMenu(self.dateFrame, self.clickedYear, *yearsList )
		self.searchButton2 = tk.Button(self.dateFrame, text='Search', font=('default', 7), command=self.dateSearch)
		
		self.searchField = tk.Entry(self.nameFrame, font=('default', 12))
		self.searchButton1 = tk.Button(self.nameFrame, text='Search', font=('default', 7), command=self.addClientForm)#command=nameSearch

		self.monthMenu.pack(side=tk.LEFT, padx=3, pady=3)
		self.yearMenu.pack(side=tk.LEFT, padx=3, pady=3)
		self.searchButton2.pack(side=tk.RIGHT, pady=3)
		# self.dateFrame.grid_propagate(1)
		self.dateFrame.pack(side=tk.TOP)
		
		self.searchField.grid(row=0, column=0)
		self.searchButton1.grid(row=0, column=1)
		self.nameFrame.pack(side=tk.TOP)
		
		self.searchFrame.pack(side=tk.LEFT, fill=tk.Y)

	def populateTreeview(self, clients):
		self.clients = clients
		self.tv = ttk.Treeview(self.searchFrame, selectmode="browse")
		self.tv.pack(side=tk.RIGHT)
		verscrlbar = ttk.Scrollbar(self.searchFrame, orient ="vertical", command=self.tv.yview)
		verscrlbar.pack(side ='right', fill ='x')
		self.tv.configure(xscrollcommand = verscrlbar.set)
		self.tv["columns"] = ("1", "2", "3")
		self.tv['show'] = 'headings'
		self.tv.column("1", width = 90, anchor ='c')
		self.tv.column("2", width = 90, anchor ='se')
		self.tv.column("3", width = 90, anchor ='se')
		self.tv.heading("1", text ="fName")
		self.tv.heading("1", text ="lName")
		self.tv.heading("2", text ="month")
		self.tv.heading("3", text ="year")
		self.tv.heading("4", text ="comments")
		self.tv.insert("", 'end', values =("Nidhi", "F", "25"))
		self.tv.insert("", 'end', values =("Nisha", "F", "23"))
		self.tv.insert("", 'end', values =("Preeti", "F", "27"))
		self.tv.insert("", 'end', values =("Rahul", "M", "20"))
		self.tv.insert("", 'end', values =("Sonu", "F", "18"))
		self.tv.insert("", 'end', values =("Rohit", "M", "19"))
		self.tv.insert("", 'end', values =("Geeta", "F", "25"))
		self.tv.insert("", 'end', values =("Ankit", "M", "22"))
		self.tv.insert("", 'end', values =("Mukul", "F", "25"))
		self.tv.insert("", 'end', values =("Mohit", "M", "16"))
		self.tv.insert("", 'end', values =("Vivek", "M", "22"))
		self.tv.insert("", 'end', values =("Suman", "F", "30"))

	def dateSearch(self):
		print("dateSearch")

	def addClientForm(self):
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

			try:
				self.tootsies = clientBase()
				self.tootsies.addDB(self.values)
			except:
				self.errorAddingToDB = messagebox.showerror("Data Insertion Error", "An error occured while attemping\nto add new client into database.")
			else:
				self.master.destroy()# close 'add client form' window
				self.successfullyAddedClient = messagebox.showinfo("", "New Client Successfully Added!")

def main():
	master = tk.Tk()
	app = tootsies(master)
	db = clientBase()
	app.populateTreeview(db.returnAll())
	master.mainloop()

main()