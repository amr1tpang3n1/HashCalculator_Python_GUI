from tkinter import *
from tkinter import ttk
import hashlib

class HashCalculator:
    """
    This is a GUI based Hash Calculator build on Python.
    Developed by : Amrit Pangeni
    Available at : https://github.com/amr1tpang3n1/HashCalculator_Python_GUI.git
    """
    
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title("Hash Calculator")
        self.root.iconbitmap("icon.ico")
        self.root.resizable(0,0)
        self.root.config(background="#abcdef")

        label = Label(self.root,text = "Hash Generator: SHA1, SHA2, MD5", bg = "#ffffff", font = "cambria 18")
        label.pack(fill = X)
        label1 = Label(self.root,text = "String to generate hash of : ", bg = "#abcdef", font = "cambria 14")
        label1.place(x = 30, y = 50)

        self.userInput = StringVar()
        entry_box = Entry(self.root, font = "cambria 12", width = "50", textvariable = self.userInput)
        entry_box.place(x = 30 ,y = 90)

        self.comboBox = ttk.Combobox(self.root,values = ("Sha1","Sha2","Md5"), state = 'readonly')
        self.comboBox.set("Md5")
        self.comboBox.place(x = 270, y = 55)

        self.button = Button(self.root, text = "Generate", font = "cambria 13", bg = "green", fg = "white",
                             command = self.hash_generator_function)
        self.button.place(x = 200 , y = 130)

        self.TextVar = StringVar()
        self.result = Label(self.root, text="Hash Generated: ", bg="#abcdef", font="cambria 14")
        self.result_box = Entry(self.root, font = "cambria 12", width = "50", textvariable = self.TextVar)
        self.root.mainloop()