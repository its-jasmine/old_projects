# module imports
import tkinter as tk    # sets tk as an alias for tkinter
from tkinter import messagebox
from math import *

window = tk.Tk()   # creates window
window.title("Calculator")   # window header title


def number(x):  # defining a function
    r = entry1.cget("font")  # retrieves font style
    if r == 'Times 20 bold':
        entry1.delete(0, "end")  # clears entry text
    entry1.config(font=("Times", 20))  # configures new font style
    y = entry1.get()  # retrieves entry text
    z = y.find("sqrt()")  # locates the presence of this string, indicating that a square root has been added
    if z != -1:
        r = y.find("()")  # locates the location (index) of this string
        entry1.insert(r + 1, x)  # adds string inside bracket
    else:
        entry1.insert(len(y), x)  # adds string to end of entry text


def operation(a):  # defining a function
    b = entry1.get()  # retrieves entry text
    if a == "1/":
        c = b + " " + a  # assigns operation with spaces as a string
        entry1.delete(0, "end")  # clears entry box
        entry1.insert(0, c)  # inserts string value into entry box
    else:
        c = b + " " + a + " "  # assigns operation with spaces as a string
        entry1.delete(0, "end")  # clears entry box
        entry1.insert(0, c)  # inserts string value into entry box


def equal():  # defining a function
    try:
        a = eval(entry1.get())  # retrieves and evaluates expression in entry
        entry1.delete(0, "end")  # clears entry box
        entry1.insert(0, a)  # inserts value into entry box
        entry1.config(font=("Times", 20, "bold"))  # configures new font style
    except:
        mess = tk.messagebox.showerror(title="Something is Wrong", message= "Please enter a valid expression.")  # displays error message
        entry1.delete(0, "end")  # clears entry box


def delete():  # defining a function
    c = entry1.get()  # retrieves entry text
    z = c[:-1]  # creates and assigns slice to variable
    entry1.delete(0, "end")  # clears entry box
    entry1.insert(0, z)  # inserts string value into entry box


def clear():  # defining a function
    entry1.delete(0, "end")  # clears entry box


frame2 = tk.Frame(window).grid(row=6)  # declaring the properties for frame

# declaring the properties for each button
but1 = tk.Button(frame2, text="1", fg="red", command=lambda: number(1), font=("Times",20, "bold"), height=1, width=5)
but2 = tk.Button(frame2, text="2", fg="red", command=lambda: number(2), font=("Times",20, "bold"), height=1, width=5)
but3 = tk.Button(frame2, text="3", fg= "red", command=lambda: number(3), font=("Times",20, "bold"), height=1, width=5)
but4 = tk.Button(frame2, text="4", fg = "red", command=lambda: number(4), font=("Times",20, "bold"), height=1, width=5)
but5 = tk.Button(frame2, text="5", fg= "red", command=lambda: number(5), font=("Times",20, "bold"), height=1, width=5)
but6 = tk.Button(frame2, text="6", fg = "red", command=lambda: number(6), font=("Times",20, "bold"), height=1, width=5)
but7 = tk.Button(frame2, text="7", fg= "red", command=lambda: number(7), font=("Times",20, "bold"), height=1, width=5)
but8 = tk.Button(frame2, text="8", fg = "red", command=lambda: number(8), font=("Times",20, "bold"), height=1, width=5)
but9 = tk.Button(frame2, text="9", fg= "red", command=lambda: number(9), font=("Times",20, "bold"), height=1, width=5)
but0 = tk.Button(frame2, text="0", fg = "red", command=lambda: number(0), font=("Times",20, "bold"), height=1, width=5)
butpar1 = tk.Button(frame2, text="(", fg = "red", command=lambda: number("("), font=("Times",20, "bold"), height=1, width=5)
butpar2 = tk.Button(frame2, text=")", fg = "red", command=lambda: number(")"), font=("Times",20, "bold"), height=1, width=5)
butequals = tk.Button(frame2, text="=", fg = "red", command=lambda: equal(), font=("Times",20, "bold"), height=3, width=5)
butplus = tk.Button(frame2, text="+", fg = "red", command=lambda: operation("+"), font=("Times",20, "bold"), height=1, width=5)
butminus = tk.Button(frame2, text="-", fg = "red", command=lambda: operation("-"), font=("Times",20, "bold"), height=1, width=5)
butmult = tk.Button(frame2, text="*", fg = "red", command=lambda: operation("*"), font=("Times",20, "bold"), height=1, width=5)
butdiv = tk.Button(frame2, text="/", fg = "red", command=lambda: operation("/"), font=("Times",20, "bold"), height=1, width=5)
butsqrt = tk.Button(frame2, text="√", fg = "red", command=lambda: operation("sqrt()"), font=("Times",20, "bold"), height=1, width=5)
butinv = tk.Button(frame2, text="1 / x", fg = "red", command=lambda: operation("1/"), font=("Times",20, "bold"), height=1, width=5)
butexp = tk.Button(frame2, text="**", fg = "red", command=lambda: operation("**"), font=("Times",20, "bold"), height=1, width=5)
butdec = tk.Button(frame2, text=".", fg = "red", command=lambda: number("."), font=("Times",20, "bold"), height=1, width=5 )
butdel = tk.Button(frame2, text="Del", fg = "red", command=lambda: delete(), font=("Times",20, "bold"), height=1, width=5 )
butclear = tk.Button(frame2, text="Clear", fg = "red", command=lambda: clear(), font=("Times",20, "bold"), height=3, width=5 )


# declaring properties for entry
entry1 = tk.Entry(frame2, font=("Times",20), width=32)


# gridding widgets into the window
entry1.grid(row=0, columnspan=6, rowspan=2)

butplus.grid(row=2, column=0)
butminus.grid(row=3, column=0)
butmult.grid(row=4, column=0)
butdiv.grid(row=5, column=0)
butsqrt.grid(row=6, column=0)

but1.grid(row=2, column=1)
but4.grid(row=3, column=1)
but7.grid(row=4, column=1)
butinv.grid(row=5, column=1)
butexp.grid(row=6, column=1)

but2.grid(row=2, column=2)
but5.grid(row=3, column=2)
but8.grid(row=4, column=2)
but0.grid(row=5, column=2)
butpar1.grid(row=6, column=2)

but3.grid(row=2, column=3)
but6.grid(row=3, column=3)
but9.grid(row=4, column=3)
butdec.grid(row=5, column=3)
butpar2.grid(row=6, column=3)

butclear.grid(row=2, rowspan=2, column=5)
butdel.grid(row=4, column=5,)
butequals.grid(row=5, rowspan=2, column=5)

window.mainloop()  # loop for the window to appear (only ends when the x button is pressed)
