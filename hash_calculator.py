import hashlib
from tkinter import *
from tkinter import ttk

class HashGenerator:
    def __init__(self):
        """
        This is a GUI based Hash Calculator build on Python.
        Developed by : Amrit Pangeni
        Available at : https://github.com/amr1tpang3n1/HashCalculator_Python_GUI.git
        """

        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title("Hash Calculator")
        self.root.iconbitmap("icon.ico")
        self.root.resizable(0, 0)
        self.root.config(background="#abcdef")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        self.StringScan = Frame(self.notebook, width=1000, height=700, bg="#70adda")
        self.FileScan = Frame(self.notebook, width=1000, height=700, bg="#70adda")

        self.StringScan.pack(fill=BOTH, expand=1)
        self.FileScan.pack(fill=BOTH, expand=1)
        self.notebook.add(self.StringScan,
                          text="                         String Hash Calculation                       ")
        self.notebook.add(self.FileScan, text="                         File Hash Calculation                       ")

        # GUI FOR STRING HASH CALCULATION

        label1 = Label(self.StringScan, text="Hash Type & String for Generating Hash :", bg="#abcdef",
                       font="cambria 14")
        label1.place(x=30, y=15)

        self.userInput = StringVar()
        entry_box = Entry(self.StringScan, font="cambria 12", width="50", textvariable=self.userInput)
        entry_box.place(x=30, y=80)

        self.comboBox = ttk.Combobox(self.StringScan, values=("Sha1", "Sha2", "Md5"), state='readonly')
        self.comboBox.set("Md5")
        self.comboBox.place(x=30, y=50)

        self.button = Button(self.StringScan, text="Generate", font="cambria 13", bg="green", fg="white",
                             command=self.hash_generator_string)
        self.button.place(x=200, y=125)

        self.TextVar = StringVar()
        self.result = Label(self.StringScan, text="Hash Generated: ", bg="#abcdef", font="cambria 14")
        self.result_box = Entry(self.StringScan, font="cambria 12", width="50", textvariable=self.TextVar)

        # GUI FOR FILE HASH CALCULATION

        label2 = Label(self.FileScan, text="Hash Type & File for Generating Hash :", bg="#abcdef",
                       font="cambria 14")
        label2.place(x=30, y=15)

        self.path = StringVar()
        file_path = Entry(self.FileScan, font="cambria 12", width="50", textvariable=self.path, state="readonly")
        file_path.place(x=30, y=80)

        self.button1 = Button(self.FileScan, text="Browse", font="cambria 11", bg="#aaaaaa",
                              command=self.File_Open_Dialog)
        self.button1.place(x=420, y=45)

        self.comboBox1 = ttk.Combobox(self.FileScan, values=("Sha1", "Sha2", "Md5"), state='readonly')
        self.comboBox1.set("Md5")
        self.comboBox1.place(x=30, y=50)

        self.button2 = Button(self.FileScan, text="Generate", font="cambria 13", bg="green", fg="white",
                              command=self.hash_generator_file)
        self.button2.place(x=200, y=125)

        self.resultVar = StringVar()
        self.result1 = Label(self.FileScan, text="Hash Generated: ", bg="#abcdef", font="cambria 14")
        self.result_box1 = Entry(self.FileScan, font="cambria 12", width="50", textvariable=self.resultVar)

        self.root.mainloop()

    def File_Open_Dialog(self):
        from tkinter import filedialog
        file = filedialog.askopenfilename()
        self.path.set(file)

    def hash_generator_string(self):
        from tkinter import messagebox
        hashType = self.comboBox.get()
        string = str(self.userInput.get())

        if string == "":
            messagebox.showinfo("Error", "Nothing to do")

        elif hashType.strip() == "Md5":
            password = string.encode()
            passwordHash = hashlib.md5(password).hexdigest()
            self.result.place(x=30, y=180)
            self.TextVar.set(passwordHash)
            self.result_box.place(x=30, y=220)

        elif hashType.strip() == "Sha2":
            password = string.encode()
            passwordHash = hashlib.sha256(password).hexdigest()
            self.result.place(x=30, y=180)
            self.TextVar.set(passwordHash)
            self.result_box.place(x=30, y=220)

        elif hashType.strip() == "Sha1":
            password = string.encode()
            passwordHash = hashlib.sha1(password).hexdigest()
            self.result.place(x=30, y=180)
            self.TextVar.set(passwordHash)
            self.result_box.place(x=30, y=220)

    def hash_generator_file(self):
        from tkinter import messagebox
        path = self.path.get()
        hashType = self.comboBox1.get()

        with open(path,'rb') as file:
            file_contents = file.read()

        if hashType.strip() == "":
            messagebox.showinfo("Error", "Nothing to do")

        elif hashType.strip() == "Md5":
            passwordHash = hashlib.md5(file_contents).hexdigest()
            self.result1.place(x=30, y=180)
            self.resultVar .set(passwordHash)
            self.result_box1.place(x=30, y=220)

        elif hashType.strip() == "Sha2":
            passwordHash = hashlib.sha256(file_contents).hexdigest()
            self.result1.place(x=30, y=180)
            self.resultVar.set(passwordHash)
            self.result_box1.place(x=30, y=220)

        elif hashType.strip() == "Sha1":
            passwordHash = hashlib.sha1(file_contents).hexdigest()
            self.result1.place(x=30, y=180)
            self.resultVar.set(passwordHash)
            self.result_box1.place(x=30, y=220)

if __name__ == '__main__':
    HashGenerator()
