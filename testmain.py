import tkinter as tk
import test

class Omenu(object):

    def __init__(self):
        self.app = tk.Tk()
        self.app.title('test1')
        self.OpMenu()
        self.btn()

    def OpMenu(self):
        self.op = tk.StringVar()
        self.opt =['1', '2']
        self.men = tk.OptionMenu(self.app, self.op, *self.opt)
        self.men.pack()

    def btn(self):
        self.btn_btn = tk.Button(self.app, text='newGui', command=self.test)
        self.btn_btn.pack()

    def test(self):
        win = guiOpMenu2.Omenu2(self.app)

win = Omenu()
win.app.mainloop()
