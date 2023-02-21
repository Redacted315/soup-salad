import tkinter as tk
from tkinter import messagebox
from dbinteraction import clientBase
from tkinter import ttk

global monthsList, yearsList, monthsWordList
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
monthsWordList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

isMonth = True

class myApp:
	
	def __init__(self, master):
		self.db = clientBase()
		self.master = master
		self.master.title("Rollaflex")
		self.master.geometry("1000x500")
		self.master.resizable("false", "false")
		self.treeviewFrame = tk.Frame(self.master)
		self.treeviewFrame.configure(background='pink')
		self.buttonFrame = tk.Frame(self.master)
		self.buttonFrame.configure(bg='yellow')
		self.allMonths = tk.Button(self.buttonFrame, text='All', command=self.all, width=3)
		self.jan = tk.Button(self.buttonFrame, text='Jan', command=self.Jan, width=3)
		self.feb = tk.Button(self.buttonFrame, text='Feb', command=self.Feb, width=3)
		self.mar = tk.Button(self.buttonFrame, text='Mar', command=self.Mar, width=3)
		self.apr = tk.Button(self.buttonFrame, text='Apr', command=self.Apr, width=3)
		self.may = tk.Button(self.buttonFrame, text='May', command=self.May, width=3)
		self.jun = tk.Button(self.buttonFrame, text='Jun', command=self.Jun, width=3)
		self.jul = tk.Button(self.buttonFrame, text='Jul', command=self.Jul, width=3)
		self.aug = tk.Button(self.buttonFrame, text='Aug', command=self.Aug, width=3)
		self.sep = tk.Button(self.buttonFrame, text='Sep', command=self.Sep, width=3)
		self.oct = tk.Button(self.buttonFrame, text='Oct', command=self.Oct, width=3)
		self.nov = tk.Button(self.buttonFrame, text='Nov', command=self.Nov, width=3)
		self.dec = tk.Button(self.buttonFrame, text='Dec', command=self.Dec, width=3)
		self.btnList = [self.allMonths,self.jan,self.feb,self.mar,self.apr,self.may,self.jun,self.jul,self.aug,self.sep,self.oct,self.nov,self.dec]
		for i in self.btnList:
			i.pack(side=tk.TOP, anchor='w')
			i.configure(bg='grey')
		self.tv = ttk.Treeview(self.treeviewFrame, selectmode="browse")
		self.tv.pack(side=tk.TOP, fill=tk.Y, expand=tk.YES)
		self.tv["columns"] = ("1", "2", "3", "4")#, "5"
		self.tv['show'] = 'headings'
		self.tv.column("1", width = 90, anchor ='c') # anchor anchors the text within the columns
		self.tv.column("2", width = 90, anchor ='c')
		self.tv.column("3", width = 55, anchor ='c')
		self.tv.column("4", width = 50, anchor ='c')
		self.tv.heading("1", text ="First", command=self.filter_firstName)
		self.tv.heading("2", text ="Last",  command=self.filter_lastName)
		self.tv.heading("3", text ="month", command=self.filter_month)
		self.tv.heading("4", text ="year",  command=self.filter_year)
		ttk.Style().configure('.', relief='flat', borderwidth=2)
		self.buttonFrame.pack(side=tk.LEFT, anchor='nw', padx=2, pady=2)
		self.treeviewFrame.pack(side=tk.LEFT, anchor='w', fill=tk.Y, expand=tk.YES)

	def filter_firstName(self):
		self.clearTreeView()
		self.populateTreeview(self.db.filterFirstName())

	def filter_lastName(self):
		self.clearTreeView()
		self.populateTreeview(self.db.filterLastName())

	def filter_month(self):
		self.clearTreeView()
		self.populateTreeview(self.db.filterMonth())

	def filter_year(self):
		self.clearTreeView()
		self.populateTreeview(self.db.filterYear())

	def populateTreeview(self, clients):
		self.clients = clients
		for i in self.clients:
			self.tv.insert("", tk.END, values=(i[1:]))# split client_id off of values so it is not shown

	def addClientForm(self):
		self.newClientForm = tk.Toplevel(self.master)
		self.app = addForm(self.newClientForm)

	def clearTreeView(self):
		for item in self.tv.get_children():
			self.tv.delete(item)
	
	def resetbtn(self):
		for i in self.btnList:
			i.configure(relief='raised', bg='grey', activebackground='grey')
	def all(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.returnAll())
		self.allMonths.configure(relief='sunken', bg='teal', activebackground='teal')
	def Jan(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(1))
		self.jan.configure(relief='sunken', bg='teal', activebackground='teal')
	def Feb(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(2))
		self.feb.configure(relief='sunken', bg='teal', activebackground='teal')
	def Mar(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(3))
		self.mar.configure(relief='sunken', bg='teal', activebackground='teal')
	def Apr(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(4))
		self.apr.configure(relief='sunken', bg='teal', activebackground='teal')
	def May(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(5))
		self.may.configure(relief='sunken', bg='teal', activebackground='teal')
	def Jun(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(6))
		self.jun.configure(relief='sunken', bg='teal', activebackground='teal')
	def Jul(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(7))
		self.jul.configure(relief='sunken', bg='teal', activebackground='teal')
	def Aug(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(8))
		self.aug.configure(relief='sunken', bg='teal', activebackground='teal')
	def Sep(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(9))
		self.sep.configure(relief='sunken', bg='teal', activebackground='teal')
	def Oct(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(10))
		self.oct.configure(relief='sunken', bg='teal', activebackground='teal')
	def Nov(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(11))
		self.nov.configure(relief='sunken', bg='teal', activebackground='teal')
	def Dec(self):
		self.resetbtn()
		self.clearTreeView()
		self.populateTreeview(self.db.searchMonth(12))
		self.dec.configure(relief='sunken', bg='teal', activebackground='teal')

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
			self.values = (self.firstNameEntry.get(), self.lastNameEntry.get(), self.monthDropdown.get(), self.yearDropdown.get())
			self.comments = self.commentEntry.get()
			try:
				
				self.db.addDB(self.values)
			except:
				self.errorAddingToDB = messagebox.showerror("Data Insertion Error", "An error occured while attemping to add new client to database.")
			else:
				self.master.destroy()# close 'add client form' window
				self.successfullyAddedClient = messagebox.showinfo("", "New Client Successfully Added!")

def main():
	master = tk.Tk()
	app = myApp(master)
	db = clientBase()
	app.populateTreeview(db.returnAll())
	master.mainloop()

if __name__ == '__main__':
	main()
