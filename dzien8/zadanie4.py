import tkinter
from tkinter import messagebox

def suma():
    print("Naciśnięto przycisk")
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
        wynik = a + b
        c_label.configure(text=f"Wynik {wynik}")
    except ValueError:
        messagebox.showerror("Błędne dane", "Powinny być liczbami")




root = tkinter.Tk()

a_label = tkinter.Label(master = root, text= "argument a")
a_label.pack()
a_entry = tkinter.Entry(master = root)
a_entry.pack()

b_label = tkinter.Label(master = root, text= "argument b")
b_label.pack()
b_entry = tkinter.Entry(master = root)
b_entry.pack()


button = tkinter.Button(master = root, text="Sumuj", command=suma)
button.pack()

c_label = tkinter.Label(master = root, text= "-")
c_label.pack()


root.mainloop()

