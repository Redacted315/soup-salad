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
		self.master.title("Rollaflex")
		self.master.geometry("1000x500")
		self.searchFrame = tk.Frame(self.master)
		self.searchFrame.configure(background='blue')
		self.searchFrame.pack(side=tk.LEFT, anchor='w', fill=tk.Y, expand=tk.YES, ipadx=2, ipady=2)

	def populateTreeview(self, clients):
		self.clients = clients
		self.tv = ttk.Treeview(self.searchFrame, selectmode="browse")
		self.tv.pack(side=tk.TOP, fill=tk.Y, expand=tk.YES, padx=2, pady=2)
		self.tv["columns"] = ("1", "2", "3", "4")#, "5"
		self.tv['show'] = 'headings'
		self.tv.column("1", width = 90, anchor ='c') # anchor anchors the text within the columns
		self.tv.column("2", width = 90, anchor ='c')
		self.tv.column("3", width = 55, anchor ='c')
		self.tv.column("4", width = 50, anchor ='c')
		self.tv.heading("1", text ="First")
		self.tv.heading("2", text ="Last")
		self.tv.heading("3", text ="month")
		self.tv.heading("4", text ="year")
		for i in self.clients:
			self.tv.insert("", tk.END, values=(i[1:]))# split client_id off of values so it is not shown
		ttk.Style().configure('.', relief='flat', borderwidth=2)

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
		self.addButton = tk.Button(self.form, text="Add", command=self.testFail)
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
			self.values = (self.firstNameEntry.get(), self.lastNameEntry.get(), self.monthDropdown.get(), self.yearDropdown.get())
			self.comments = self.commentEntry.get()
			try:
				self.tootsies = clientBase()
				self.tootsies.addDB(self.values)
			except:
				self.errorAddingToDB = messagebox.showerror("Data Insertion Error", "An error occured while attemping to add new client to database.")
			else:
				self.master.destroy()# close 'add client form' window
				self.successfullyAddedClient = messagebox.showinfo("", "New Client Successfully Added!")

def main():
	master = tk.Tk()
	app = tootsies(master)
	db = clientBase()
	# print(db.returnAll())
	app.populateTreeview(db.returnAll())
	master.mainloop()

if __name__ == '__main__':
	main()
