from tkinter import *

def dateSearch():
	# remove text entry and search button, and replace with two dropdown menus for month and date
	print("dateSearch")
	nameSearchFrame.destroy()
	dateFilter.configure(state=DISABLED)
	nameFilter.configure(state=NORMAL)


def nameSearch():
	# remove dropdown menus, and add entry and search button
	print("nameSearch")
	# dateSearchFrame.destroy()
	nameSearchFrame = Frame(LF)
	searchField = Entry(nameSearchFrame, font=('default', 12), width=10)
	searchButton = Button(nameSearchFrame, text='Search', font=('default', 7), height=1)
	nameSearchFrame.grid(row=1, column=0, columnspan=2)
	searchField.grid(row=0,column=0, padx=3, pady=3)
	searchButton.grid(row=0,column=1, padx=3, pady=3)
	nameFilter.configure(state=DISABLED)
	dateFilter.configure(state=NORMAL)


def gw():
	print(LF.winfo_width())


#################################
root = Tk()
root.title('root')
root.geometry("1000x500")
#################################
LF = Frame(root, width=179)
LF.configure(background='blue')
LF.grid_propagate(0)
nameSearchFrame = Frame(LF)

searchField = Entry(nameSearchFrame, font=('default', 12), width=10)
searchButton = Button(nameSearchFrame, text='Search', font=('default', 7), height=1)

filterVar = IntVar()
dateFilter = Radiobutton(LF, text="Date", selectcolor="grey", command=dateSearch, variable=filterVar, value=1)
nameFilter = Radiobutton(LF, text="Name", selectcolor="grey", command=nameSearch, variable=filterVar, value=2)



#################################
RF = Frame(root)
RF.configure(background="dark green")


info = Label(RF, text='details', font=('default', 24))

quitButton = Button(root, text="QUIT", font=('default', 24), command=quit)
quitButton.configure(background="red", activebackground="maroon")
#################################
quitButton.pack(side=BOTTOM, fill=X, expand=NO, padx=3, pady=3)

LF.pack(side=LEFT, fill=Y, expand=NO)
RF.pack(side=RIGHT, fill=BOTH, expand=YES)
dateFilter.grid(row=0, column=0, sticky='wne')
nameFilter.grid(row=0, column=1, sticky='wne')
# nameSearchFrame.grid(row=1, column=0, columnspan=2)

info.pack()

#################################
root.mainloop()