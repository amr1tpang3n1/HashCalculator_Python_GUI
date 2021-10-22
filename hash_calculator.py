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

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        self.StringScan = Frame(self.notebook, width=1000, height=700, bg="#70adda")
        self.frame2 = Frame(self.notebook, width=1000, height=700, bg="#70adda")

        self.StringScan.pack(fill=BOTH, expand=1)
        self.frame2.pack(fill=BOTH, expand=1)
        self.notebook.add(self.StringScan,text="                         String Hash Calculation                       ")
        self.notebook.add(self.frame2, text="                         File Hash Calculation                       ")


        ## GUI FOR STRING HASH CALCULATION

        label1 = Label(self.StringScan,text = "Hash Type & String for Generating Hash :", bg = "#abcdef", font = "cambria 14")
        label1.place(x = 30, y = 15)

        self.userInput = StringVar()
        entry_box = Entry(self.StringScan, font = "cambria 12", width = "50", textvariable = self.userInput)
        entry_box.place(x = 30 ,y = 80)

        self.comboBox = ttk.Combobox(self.StringScan,values = ("Sha1","Sha2","Md5"), state = 'readonly')
        self.comboBox.set("Md5")
        self.comboBox.place(x = 30, y = 50)

        self.button = Button(self.StringScan, text = "Generate", font = "cambria 13", bg = "green", fg = "white",
                             command = self.hash_generator_function)
        self.button.place(x = 200 , y = 125)

        self.TextVar = StringVar()
        self.result = Label(self.StringScan, text="Hash Generated: ", bg="#abcdef", font="cambria 14")
        self.result_box = Entry(self.StringScan, font = "cambria 12", width = "50", textvariable = self.TextVar)


        ## GUI FOR FILE HASH CALCULATION

        self.root.mainloop()


    def hash_generator_function(self):
        from tkinter import messagebox

        hash = self.comboBox.get()
        hashType = str()
        if hash == "Md5":
            hashType = "1"
        elif hash == "Sha2":
            hashType = "2"
        elif hash == "Sha1":
            hashType = "3"

        string = str(self.userInput.get())
        if string == "":
            messagebox.showinfo("Error","Nothing to do")

        elif hashType.strip() == "1":
            password = string.encode()
            passwordHash = hashlib.md5(password).hexdigest()
            self.result.place(x=30, y=180)
            self.TextVar.set(passwordHash)
            self.result_box.place(x=30, y=220)

        elif hashType.strip() == "2":
            password = string.encode()
            passwordHash = hashlib.sha256(password).hexdigest()
            self.result.place(x=30, y=180)
            self.TextVar.set(passwordHash)
            self.result_box.place(x=30, y=220)

        elif hashType.strip() == "3":
            password = string.encode()
            passwordHash = hashlib.sha1(password).hexdigest()
            self.result.place(x=30, y=180)
            self.TextVar.set(passwordHash)
            self.result_box.place(x=30, y=220)

        else:
            messagebox.showerror("Error !", "Something Went Wrong !!")

if __name__ == '__main__':
    HashCalculator()