from tkinter import *

def dateSearch():
	# clear name fields
	searchField.delete(0, END)

def nameSearch():
	# clear date fields
	pass

def on_focus_in(entry):
    entry.configure(state='normal')
    entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')





root = Tk()
root.title('root')
root.geometry("1000x500")

LF = Frame(root, width=179)
LF.configure(background='blue')
dateFrame = Frame(LF)
nameFrame = Frame(LF)


months = [
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
clicked = StringVar()
# initial menu text
clicked.set( "January" )
# Create Dropdown menu
monthMenu = OptionMenu(dateFrame, clicked, *months )


years = [
    "2023",
    "2022",
    "2021",
    "2020"
]
# datatype of menu text
clicked = StringVar()
# initial menu text
clicked.set("2023")
# Create Dropdown menu
yearMenu = OptionMenu(dateFrame, clicked, *years )
searchButton2 = Button(dateFrame, text='Search', font=('default', 7))

searchField = Entry(nameFrame, font=('default', 12))
searchButton1 = Button(nameFrame, text='Search', font=('default', 7))

searchField.insert(0, "Enter Name")
focus_in = searchField.bind('<Button-1>', lambda x: on_focus_in(searchField))

yearMenu.grid(row=0, column=1)
monthMenu.grid(row=0, column=0)
searchButton2.grid(row=0, column=2, sticky='we')
dateFrame.grid_propagate(1)
dateFrame.grid(row=0, column=0, columnspan=2, pady=3, sticky='wne')


searchField.grid(row=0, column=0)
searchButton1.grid(row=0, column=1)
nameFrame.grid(row=1, column=0, columnspan=2, pady=3, sticky='wne')

LF.pack(side=LEFT, fill=Y)

root.mainloop()