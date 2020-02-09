from tkinter import *
from tkinter import messagebox
import math

#Houd het tussen resultaat bij doorheen het gebruik
tussen_res = 0

#Initializeren van tkinter
root = Tk()
root.title('Calculator')

#Input veld maken
veld = Entry(root, width=35)

#Voeg nummer toe aan veld
def addNumber(number):
    getal = veld.get()
    veld.delete(0, 'end')
    getal = str(getal) + str(number)
    veld.insert(0, getal)

#Maak veld leeg en ook het tussen resultaat
def clear():
    global tussen_res
    veld.delete(0, 'end')
    tussen_res = 0

#Tel op
def add():
    global tussen_res
    global bewerking
    bewerking = "ADD"
    if tussen_res == 0:
        try:
            tussen_res = int(veld.get())
        except ValueError:
            messagebox.showerror('Number format error', 'Please only fill in numbers')
    veld.delete(0, 'end')

#Vermenigvuldig
def multiply():
    global tussen_res
    global bewerking
    bewerking = "MULTIPLY"
    if tussen_res == 0:
        try:
            tussen_res = int(veld.get())
        except ValueError:
            messagebox.showerror('Number format error', 'Please only fill in numbers')
    veld.delete(0, 'end')

#Trek af
def subtract():
    global tussen_res
    global bewerking
    bewerking = "SUBTRACT"
    if tussen_res == 0:
        try:
            tussen_res = int(veld.get())
        except ValueError:
            messagebox.showerror('Number format error', 'Please only fill in numbers')
    veld.delete(0, 'end')

#Deel door
def divide():
    global tussen_res
    global bewerking
    bewerking = "DIVIDE"
    if tussen_res == 0:
        try:
            tussen_res = int(veld.get())
        except ValueError:
            messagebox.showerror('Number format error', 'Please only fill in numbers')
    veld.delete(0, 'end')

#Tot de x macht
def power():
    global tussen_res
    global bewerking
    bewerking = "POWER"
    if tussen_res == 0:
        try:
            tussen_res = int(veld.get())
        except ValueError:
            messagebox.showerror('Number format error', 'Please only fill in numbers')
    veld.delete(0, 'end')

#Vierkantswortel
def squareroot():
    global tussen_res
    global bewerking
    bewerking = "SQRT"
    if tussen_res == 0:
        try:
            tussen_res = int(veld.get())
        except ValueError:
            messagebox.showerror('Number format error', 'Please only fill in numbers')
            veld.delete(0, 'end')
            return None
    veld.delete(0, 'end')
    veld.insert(0, f'sqrt({tussen_res})')

#Toont resultaat
def equal():
    global tussen_res
    global bewerking
    tweede_getal = 0
    try:
        tweede_getal = int(veld.get())
    except ValueError:
        messagebox.showerror('Number format error', 'Please only fill in numbers')
        veld.delete(0, 'end')
        return None
    
    if bewerking == "ADD":
        tussen_res = tussen_res + tweede_getal
    
    if bewerking == "DIVIDE":
        tussen_res = tussen_res / tweede_getal
    
    if bewerking == "SUBTRACT":
        tussen_res = tussen_res - tweede_getal

    if bewerking == "MULTIPLY":
        tussen_res = tussen_res * tweede_getal

    if bewerking == "POWER":
        tussen_res = tussen_res ** tweede_getal

    if bewerking == "SQRT":
        tussen_res = math.sqrt(tussen_res)
    
    veld.delete(0, 'end')
    veld.insert(0, tussen_res )

#Initializeren getal buttons
een = Button(root, text='1', width=12, height=2, command=lambda: addNumber(1))
twee = Button(root, text='2', width=12, height=2, command=lambda: addNumber(2))
drie = Button(root, text='3', width=12, height=2, command=lambda: addNumber(3))
vier = Button(root, text='4', width=12, height=2, command=lambda: addNumber(4))
vijf = Button(root, text='5', width=12, height=2, command=lambda: addNumber(5))
zes = Button(root, text='6', width=12, height=2, command=lambda: addNumber(6))
zeven = Button(root, text='7', width=12, height=2, command=lambda: addNumber(7))
acht = Button(root, text='8', width=12, height=2, command=lambda: addNumber(8))
negen = Button(root, text='9', width=12, height=2, command=lambda: addNumber(9))
nul = Button(root, text='0', width=12, height=2, command=lambda: addNumber(0))

#Initializeren clear button
clear = Button(root, text='clear', width=12, height=2, command=clear)

#Initializeren bewerking buttons
plus = Button(root, text='+', width=12, height=2, command=add)
subtract = Button(root, text='-', width=12, height=2, command=subtract)
maal = Button(root, text='*', width=12, height=2, command=multiply)
deel = Button(root, text='/', width=12, height=2, command=divide)
macht = Button(root, text='^', width=12, height=2, command=power)
vierkants = Button(root, text='\u221A\u0305', width=12, height=2, command=squareroot)

#Initializeren gelijk aan button
gelijkaan = Button(root, text='=', width=12, height=2, command=equal)

#Plaatsen van buttons etc in het frame
veld.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

negen.grid(row=1, column=2)
acht.grid(row=1, column=1)
zeven.grid(row=1, column=0)

zes.grid(row=2, column=2)
vijf.grid(row=2, column=1)
vier.grid(row=2, column=0)

drie.grid(row=3, column=2)
twee.grid(row=3, column=1)
een.grid(row=3, column=0)

nul.grid(row=4, column=0)
plus.grid(row=4, column=1)
gelijkaan.grid(row=4, column=2)

maal.grid(row=5, column=0)
subtract.grid(row=5, column=1)
clear.grid(row=5, column=2)

deel.grid(row=6, column=0)
macht.grid(row=6, column=1)
vierkants.grid(row=6, column=2)

#Houd programma runnende
root.mainloop()