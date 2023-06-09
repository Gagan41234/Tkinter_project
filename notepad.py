from tkinter import *
from tkinter.filedialog import *


class notepad:
    def new(self):
        self.l1.config(text="")
        try:
            self.text.delete(1.0, END)
            self.l1.config(text="")
        except:
            pass

    def open(self):
        try:
            self.l1.config(text="")

            self.file = askopenfile(
                filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
            ).name
            self.text.delete(1.0, END)
            with open(self.file, "r") as f:
                str = f.read()
                self.text.insert("1.0", str)
            self.l1.config(text="Opened from:\n" + self.file)
        except:
            pass

    def save(self):
        # try:
        try:
            with open(self.file, "w") as f:
                f.write(self.text.get("1.0", END))
            self.l1.config(text="Saved at: \n" + self.file)
        except:
            self.file = open("write.txt", "w")
            self.file.write(self.text.get(1.0, END))
            self.file.close()
            self.l1.config(text="Saved at: \nDesktop\gui\write.txt ")

    # except:

    def saveas(self):
        files = [
            ("All Files", "*.*"),
            ("Python Files", "*.py"),
            ("Text Document", "*.txt"),
        ]
        try:
            self.file = asksaveasfile(filetypes=files, defaultextension=files).name
            with open(self.file, "w") as f:
                f.write(self.text.get("1.0", END))
            self.l1.config(text="Saved at:\n" + self.file)
        except:
            pass

    def __init__(self):
        self.window = Tk()
        self.window.config(bg="#2b2d42")
        self.window.geometry("1000x600")
        self.window.title("Notepad")
        self.create_frame1()
        self.create_text()

    def create_text(self):
        self.text = Text(
            self.window, width=400, height=24, font=("Times New Roman", 15)
        )
        self.text.pack(side=BOTTOM, padx=20, pady=5)
        self.l1 = Label(
            self.window, text="", fg="white", font=("Arial", "15"), bg="#2b2d42"
        )
        self.l1.place(x=400, y=10)

    def create_frame1(self):
        self.frame = Frame(self.window, width=205, height=1000, bg="#6096ba")
        self.frame.pack(side=LEFT, padx=10, pady=10)
        btn1 = Button(
            self.frame,
            text="Save",
            padx=50,
            pady=10,
            font=("Bahma", "20"),
            fg="#f1faee",
            bg="#e63946",
            command=lambda: self.save(),
        )
        btn1.place(x=10, y=100)
        btn1 = Button(
            self.frame,
            text="Open",
            padx=47,
            pady=10,
            font=("Bahma", "20"),
            fg="#caf0f8",
            bg="#03045e",
            command=lambda: self.open(),
        )
        btn1.place(x=10, y=200)
        btn1 = Button(
            self.frame,
            text="New",
            padx=54,
            pady=10,
            font=("Bahma", "20"),
            fg="#e0aaff",
            bg="#3c096c",
            command=lambda: self.new(),
        )
        btn1.place(x=10, y=300)
        btn1 = Button(
            self.frame,
            text="Save As",
            padx=30,
            pady=10,
            font=("Bahma", "20"),
            fg="#ffffff",
            bg="#ff9f1c",
            command=lambda: self.saveas(),
        )
        btn1.place(x=10, y=400)


root = notepad()
root.window.mainloop()
