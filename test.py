import tkinter as tk
class Omenu2(object):

    def __init__(self, app):
        self.app = app
        self.master = tk.Toplevel(app)
        self.master.title('test1')
        self.OpMenu2()

    def OpMenu2(self):
        self.op2 = tk.StringVar()
        self.opt2 =['2', '3']
        self.men2 = tk.OptionMenu(self.master, self.op2, *self.opt2, command=self.test)
        self.men2.pack()

    def test(self, num):
       print(self.op2.get())
       print(num)