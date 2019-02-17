import tkinter
from tkinter import messagebox

def koszt():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        d = float(d_entry.get())
        wynik = a * b *d/100
        c_label.configure(text=f"Wynik {wynik}")
    except ValueError:
        messagebox.showerror("Błędne dane", "Powinny być liczbami")




root = tkinter.Tk()
root.columnconfigure(1,weight=1)
a_label = tkinter.Label(master = root, text= "Podaj dystans w km")
a_label.grid(row=0, column=0)
a_entry = tkinter.Entry(master = root)
a_entry.grid(row=0, column=1)

b_label = tkinter.Label(master = root, text= "Spalanie")
b_label.grid(row=1, column=0)
b_entry = tkinter.Entry(master = root)
b_entry.grid(row=1, column=1)

d_label = tkinter.Label(master = root, text= "Cena paliwa")
d_label.grid(row=2, column=0)
d_entry = tkinter.Entry(master = root)
d_entry.grid(row=2, column=1)


button = tkinter.Button(master = root, text="Policz koszt przejazdu", command=koszt)
button.grid(row=3, column=0)

c_label = tkinter.Label(master = root, text= "-")
c_label.grid(row=4, column=0)


root.mainloop()