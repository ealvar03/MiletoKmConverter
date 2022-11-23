from tkinter import *


def button_clicked():
    km_conversion = int(entry.get()) * 1.60934
    result.config(text=km_conversion)

# Creating a new windows
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=50, height=50)
window.config(padx=20, pady=20)

# Labels
miles = Label(text="Miles")
miles.grid(column=2, row=0)
km = Label(text="Km")
km.grid(column=2, row=1)
equal = Label(text="is equal to")
equal.grid(column=0, row=1)
result = Label(text="0")
result.grid(column=1, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

window.mainloop()
