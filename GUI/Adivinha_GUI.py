import tkinter as tk
import random
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Adivinha Número")



numero = random.randrange(0, 10)
numero1 = str(numero)
mainframe = ttk.Frame(root)

ttk.Label(mainframe, text="numero1").grid(column=1, row=2, sticky=E)


root.mainloop()