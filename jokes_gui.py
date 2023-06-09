from tkinter import *
import requests


def show():
    def save():
        a = text.size()
        file = open("jokes.txt", "w")
        for i in range(a):
            file.write(text.get(i) + "\n")
        file.close()

    def delete():
        selected = text.curselection()
        for i in selected[::-1]:
            text.delete(i)

    try:
        file = open("jokes.txt", "r")
    except:
        l1.config(text="File does not exist to create a file,copy a single joke")
    else:
        mynew = Toplevel(root)
        mynew.geometry("900x600")
        mynew.resizable(0.0, 0.0)
        text = Listbox(
            mynew, height=20, selectmode=MULTIPLE, width=200, font=("", "15")
        )
        text.pack(fill=BOTH)
        f = file.read()
        f = f.split("\n")
        for i in f:
            text.insert(END, i)
        file.close()
        fram = Frame(mynew, width=800, height=100)
        fram.pack(side=BOTTOM)
        b1 = Button(
            fram,
            text="Delete",
            width=20,
            font=("Arial", "20"),
            command=delete,
            relief=("raised"),
        )
        b1.place(x=70, y=20)
        b1 = Button(
            fram,
            text="Save",
            width=20,
            font=("Arial", "20"),
            command=save,
        )
        b1.place(x=400, y=20)


def jokes():
    d = requests.get("https://v2.jokeapi.dev/joke/Any")
    dicitionary_jokes = d.json()
    l1.config(text="")
    if dicitionary_jokes["type"] == "single":

        def copy():
            try:
                file = open("jokes.txt", "a")
            except:
                file = open("jokes.txt", "w")
                file.close()
            l1.config(text="Saved at: Desktop\gui\jokes.txt")
            file = open("jokes.txt", "a")
            file.write(dicitionary_jokes["joke"] + "\n\n")
            file.close()

        single.config(
            text=dicitionary_jokes["joke"][0:],
            font=("Arial", "20", "bold"),
            wraplength=1000,
        )
        double.config(
            text="",
            font=("Arial", "20", "bold"),
            wraplength=1000,
        )

    else:

        def copy():
            try:
                file = open("jokes.txt", "a")
            except:
                file = open("jokes.txt", "w")
                file.close()
            l1.config(text="Saved at: Desktop\gui\jokes.txt")
            file = open("jokes.txt", "a")

            file.write(dicitionary_jokes["setup"] + "\n")
            file.write(dicitionary_jokes["delivery"] + "\n\n")
            file.close()

        single.config(
            text=dicitionary_jokes["setup"],
            font=("Arial", "20", "bold"),
            wraplength=1000,
        )
        double.config(
            text=dicitionary_jokes["delivery"],
            font=("Arial", "20", "bold"),
            wraplength=1000,
        )

    btn1.config(command=copy)


root = Tk()
root.geometry("1200x500")
root.resizable(0.0, 0.0)
root.config(bg="#fdf0d5", borderwidth=15, relief="groove")
heading = Label(
    text="JOKES MAKER", font=(" Helvetica", "60", "bold"), bg="#fdf0d5", fg="#4a4e69"
)
heading.pack(pady=30)

single = Label(text="", fg="#e63946", bg="#fdf0d5")
single.pack()
single.place(x=50, y=200)
double = Label(text="", fg="#e63946", bg="#fdf0d5")
double.pack()
double.place(x=50, y=300)
btn = Button(
    text="New jokes",
    command=jokes,
    padx=10,
    pady=5,
    font=("Arial", "15", "bold"),
    fg="#a8dadc",
    bg="#1d3557",
)
btn.pack()
btn.place(x=1030, y=410)
btn1 = Button(
    text="Save to the file",
    padx=10,
    pady=5,
    font=("Arial", "15", "bold"),
    fg="#a8dadc",
    bg="#1d3557",
)
btn1.pack()
btn1.place(x=830, y=410)
btn2 = Button(
    text="Show Jokes",
    padx=10,
    pady=5,
    font=("Arial", "15", "bold"),
    fg="#a8dadc",
    bg="#1d3557",
    command=show,
)
btn2.place(x=651, y=410)
l1 = Label(text="sadfsd", fg="red", bg="#fdf0d5", font=("Arial", "15"))
l1.place(x=600, y=350)
# fp = open("jokes.txt", "r+")
# fp.truncate(0)
# fp.close()
jokes()
root.mainloop(
