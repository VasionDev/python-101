from tkinter import *
import random
import time
import datetime
from tkinter import messagebox

root = Tk()
root.geometry('1350x750+0+0')
root.title('GUI application')
root.configure(background='black')

top = Frame(root, width=1350, height=100, bd=16, relief=RAISED)
top.pack(side=TOP)

labelTop = Label(top, text='Cafe Management System', font=('arial', 40, 'bold'), width=1350)
labelTop.pack()

frame1 = Frame(root, width=900, height=650, bd=14, relief=RAISED)
frame1.pack(side=LEFT)

frame2 = Frame(root, width=450, height=650, bd=14, relief=RAISED)
frame2.pack(side=RIGHT)

frame1Top = Frame(frame1, width=900, height=350, bd=14, relief=RAISED)
frame1Top.pack(side=TOP)

frame1Bottom = Frame(frame1, width=900, height=300, bd=14, relief=RAISED)
frame1Bottom.pack(side=BOTTOM)

frame2Top = Frame(frame2, width=450, height=450, bd=14, relief=RAISED)
frame2Top.pack(side=TOP)

frame2Bottom = Frame(frame2, width=450, height=200, bd=14, relief=RAISED)
frame2Bottom.pack(side=BOTTOM)

frame1TopLeft = Frame(frame1Top, width=450, height=350, bd=14, relief=RAISED)
frame1TopLeft.pack(side=LEFT)

frame1TopRight = Frame(frame1Top, width=450, height=350, bd=14, relief=RAISED)
frame1TopRight.pack(side=RIGHT)

frame1BottomLeft = Frame(frame1Bottom, width=500, height=300, bd=14, relief=RAISED)
frame1BottomLeft.pack(side=LEFT)

frame1BottomRight = Frame(frame1Bottom, width=400, height=300, bd=14, relief=RAISED)
frame1BottomRight.pack(side=RIGHT)

frame2TopLabel = Label(frame2Top, text='Receipt', font=('arial', 10, 'bold'))
frame2TopLabel.grid(row=0, sticky=W)

frame2TopDisplay = Text(frame2Top, font=('arial', 10, 'bold'), width=47, height=30)
frame2TopDisplay.grid(row=1, column=0)

# **** Functions ****


def exit_project():
    project_exit = messagebox.askyesno('Project Exit', 'Are you want to exit?')
    if project_exit is True:
        root.destroy()


def reset_project():
    check1.set(0)
    check2.set(0)
    check3.set(0)
    check4.set(0)
    check5.set(0)
    check6.set(0)
    check7.set(0)
    check8.set(0)
    check9.set(0)
    check10.set(0)
    check11.set(0)
    check12.set(0)
    check13.set(0)
    check14.set(0)
    check15.set(0)
    check16.set(0)

    entry1.set(0)
    entry2.set(0)
    entry3.set(0)
    entry4.set(0)
    entry5.set(0)
    entry6.set(0)
    entry7.set(0)
    entry8.set(0)
    entry9.set(0)
    entry10.set(0)
    entry11.set(0)
    entry12.set(0)
    entry13.set(0)
    entry14.set(0)
    entry15.set(0)
    entry16.set(0)

    entryField1.configure(state=DISABLED)
    entryField2.configure(state=DISABLED)
    entryField3.configure(state=DISABLED)
    entryField4.configure(state=DISABLED)
    entryField5.configure(state=DISABLED)
    entryField6.configure(state=DISABLED)
    entryField7.configure(state=DISABLED)
    entryField8.configure(state=DISABLED)
    entryField9.configure(state=DISABLED)
    entryField10.configure(state=DISABLED)
    entryField11.configure(state=DISABLED)
    entryField12.configure(state=DISABLED)
    entryField13.configure(state=DISABLED)
    entryField14.configure(state=DISABLED)
    entryField15.configure(state=DISABLED)
    entryField16.configure(state=DISABLED)


def check_button():
    if check1.get() == 1:
        entryField1.configure(state=NORMAL)
    else:
        entryField1.configure(state=DISABLED)
    if check2.get() == 1:
        entryField2.configure(state=NORMAL)
    else:
        entryField2.configure(state=DISABLED)
    if check3.get() == 1:
        entryField3.configure(state=NORMAL)
    else:
        entryField3.configure(state=DISABLED)
    if check4.get() == 1:
        entryField4.configure(state=NORMAL)
    else:
        entryField4.configure(state=DISABLED)
    if check5.get() == 1:
        entryField5.configure(state=NORMAL)
    else:
        entryField5.configure(state=DISABLED)
    if check6.get() == 1:
        entryField6.configure(state=NORMAL)
    else:
        entryField6.configure(state=DISABLED)
    if check7.get() == 1:
        entryField7.configure(state=NORMAL)
    else:
        entryField7.configure(state=DISABLED)
    if check8.get() == 1:
        entryField8.configure(state=NORMAL)
    else:
        entryField8.configure(state=DISABLED)
    if check9.get() == 1:
        entryField9.configure(state=NORMAL)
    else:
        entryField9.configure(state=DISABLED)
    if check10.get() == 1:
        entryField10.configure(state=NORMAL)
    else:
        entryField10.configure(state=DISABLED)
    if check11.get() == 1:
        entryField11.configure(state=NORMAL)
    else:
        entryField11.configure(state=DISABLED)
    if check12.get() == 1:
        entryField12.configure(state=NORMAL)
    else:
        entryField12.configure(state=DISABLED)
    if check13.get() == 1:
        entryField13.configure(state=NORMAL)
    else:
        entryField13.configure(state=DISABLED)
    if check14.get() == 1:
        entryField14.configure(state=NORMAL)
    else:
        entryField14.configure(state=DISABLED)
    if check15.get() == 1:
        entryField15.configure(state=NORMAL)
    else:
        entryField15.configure(state=DISABLED)
    if check16.get() == 1:
        entryField16.configure(state=NORMAL)
    else:
        entryField16.configure(state=DISABLED)


# **** Variables ****

check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
check4 = IntVar()
check5 = IntVar()
check6 = IntVar()
check7 = IntVar()
check8 = IntVar()
check9 = IntVar()
check10 = IntVar()
check11 = IntVar()
check12 = IntVar()
check13 = IntVar()
check14 = IntVar()
check15 = IntVar()
check16 = IntVar()

check1.set(0)
check2.set(0)
check3.set(0)
check4.set(0)
check5.set(0)
check6.set(0)
check7.set(0)
check8.set(0)
check9.set(0)
check10.set(0)
check11.set(0)
check12.set(0)
check13.set(0)
check14.set(0)
check15.set(0)
check16.set(0)

entry1 = IntVar()
entry2 = IntVar()
entry3 = IntVar()
entry4 = IntVar()
entry5 = IntVar()
entry6 = IntVar()
entry7 = IntVar()
entry8 = IntVar()
entry9 = IntVar()
entry10 = IntVar()
entry11 = IntVar()
entry12 = IntVar()
entry13 = IntVar()
entry14 = IntVar()
entry15 = IntVar()
entry16 = IntVar()

entry1.set(0)
entry2.set(0)
entry3.set(0)
entry4.set(0)
entry5.set(0)
entry6.set(0)
entry7.set(0)
entry8.set(0)
entry9.set(0)
entry10.set(0)
entry11.set(0)
entry12.set(0)
entry13.set(0)
entry14.set(0)
entry15.set(0)
entry16.set(0)

# <<<<<<<<<<<<<<<<<<<<<<< End Variable Initialization >>>>>>>>>>>>>>>>>>>>

# **** Checkbox Button ****

checkbox1 = Checkbutton(frame1TopLeft, font=('arial', 15, 'bold'), text='CheckBox 1 \t\t', variable=check1, onvalue=1, offvalue=0, command=check_button)
checkbox1.grid(row=0, column=0, sticky=W)
checkbox2 = Checkbutton(frame1TopLeft, font=('arial', 15, 'bold'), text='CheckBox 2', variable=check2, onvalue=1, offvalue=0, command=check_button)
checkbox2.grid(row=1, column=0, sticky=W)
checkbox3 = Checkbutton(frame1TopLeft, font=('arial', 15, 'bold'), text='CheckBox 3', variable=check3, onvalue=1, offvalue=0, command=check_button)
checkbox3.grid(row=2, column=0, sticky=W)
checkbox4 = Checkbutton(frame1TopLeft, font=('arial', 15, 'bold'), text='CheckBox 4', variable=check4, onvalue=1, offvalue=0, command=check_button)
checkbox4.grid(row=3, column=0, sticky=W)
checkbox5 = Checkbutton(frame1TopLeft, font=('arial', 15, 'bold'), text='CheckBox 5', variable=check5, onvalue=1, offvalue=0, command=check_button)
checkbox5.grid(row=4, column=0, sticky=W)
checkbox6 = Checkbutton(frame1TopLeft, font=('arial', 15, 'bold'), text='CheckBox 6', variable=check6, onvalue=1, offvalue=0, command=check_button)
checkbox6.grid(row=5, column=0, sticky=W)
checkbox7 = Checkbutton(frame1TopLeft, font=('arial', 15, 'bold'), text='CheckBox 7', variable=check7, onvalue=1, offvalue=0, command=check_button)
checkbox7.grid(row=6, column=0, sticky=W)
checkbox8 = Checkbutton(frame1TopLeft, font=('arial', 15, 'bold'), text='CheckBox 8', variable=check8, onvalue=1, offvalue=0, command=check_button)
checkbox8.grid(row=7, column=0, sticky=W)
checkbox9 = Checkbutton(frame1TopRight, font=('arial', 15, 'bold'), text='CheckBox 9 \t\t\t', variable=check9, onvalue=1, offvalue=0, command=check_button)
checkbox9.grid(row=0, column=0, sticky=W)
checkbox10 = Checkbutton(frame1TopRight, font=('arial', 15, 'bold'), text='CheckBox 10', variable=check10, onvalue=1, offvalue=0, command=check_button)
checkbox10.grid(row=1, column=0, sticky=W)
checkbox11 = Checkbutton(frame1TopRight, font=('arial', 15, 'bold'), text='CheckBox 11', variable=check11, onvalue=1, offvalue=0, command=check_button)
checkbox11.grid(row=2, column=0, sticky=W)
checkbox12 = Checkbutton(frame1TopRight, font=('arial', 15, 'bold'), text='CheckBox 12', variable=check12, onvalue=1, offvalue=0, command=check_button)
checkbox12.grid(row=3, column=0, sticky=W)
checkbox13 = Checkbutton(frame1TopRight, font=('arial', 15, 'bold'), text='CheckBox 13', variable=check13, onvalue=1, offvalue=0, command=check_button)
checkbox13.grid(row=4, column=0, sticky=W)
checkbox14 = Checkbutton(frame1TopRight, font=('arial', 15, 'bold'), text='CheckBox 14', variable=check14, onvalue=1, offvalue=0, command=check_button)
checkbox14.grid(row=5, column=0, sticky=W)
checkbox15 = Checkbutton(frame1TopRight, font=('arial', 15, 'bold'), text='CheckBox 15', variable=check15, onvalue=1, offvalue=0, command=check_button)
checkbox15.grid(row=6, column=0, sticky=W)
checkbox16 = Checkbutton(frame1TopRight, font=('arial', 15, 'bold'), text='CheckBox 16', variable=check16, onvalue=1, offvalue=0, command=check_button)
checkbox16.grid(row=7, column=0, sticky=W)

# <<<<<<<<<<<<<<<<<<<<<<<<<<< End CheckBox Button >>>>>>>>>>>>>>>>>>>>>>>>>>>>

# **** Entry Field ****

entryField1 = Entry(frame1TopLeft, textvariable=entry1, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField1.grid(row=0, column=1)
entryField2 = Entry(frame1TopLeft, textvariable=entry2, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField2.grid(row=1, column=1)
entryField3 = Entry(frame1TopLeft, textvariable=entry3, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField3.grid(row=2, column=1)
entryField4 = Entry(frame1TopLeft, textvariable=entry4, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField4.grid(row=3, column=1)
entryField5 = Entry(frame1TopLeft, textvariable=entry5, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField5.grid(row=4, column=1)
entryField6 = Entry(frame1TopLeft, textvariable=entry6, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField6.grid(row=5, column=1)
entryField7 = Entry(frame1TopLeft, textvariable=entry7, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField7.grid(row=6, column=1)
entryField8 = Entry(frame1TopLeft, textvariable=entry8, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField8.grid(row=7, column=1)
entryField9 = Entry(frame1TopRight, textvariable=entry9, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField9.grid(row=0, column=1)
entryField10 = Entry(frame1TopRight, textvariable=entry10, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField10.grid(row=1, column=1)
entryField11 = Entry(frame1TopRight, textvariable=entry11, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField11.grid(row=2, column=1)
entryField12 = Entry(frame1TopRight, textvariable=entry12, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField12.grid(row=3, column=1)
entryField13 = Entry(frame1TopRight, textvariable=entry13, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField13.grid(row=4, column=1)
entryField14 = Entry(frame1TopRight, textvariable=entry14, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField14.grid(row=5, column=1)
entryField15 = Entry(frame1TopRight, textvariable=entry15, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField15.grid(row=6, column=1)
entryField16 = Entry(frame1TopRight, textvariable=entry16, state=DISABLED, width=10, font=('arial', 10, 'bold'), bd=6, justify=LEFT)
entryField16.grid(row=7, column=1)

# <<<<<<<<<<<<<<<<<<<< End Entry Field >>>>>>>>>>>>>>>>>>>>>>>>>

# **** (Total, Receipt, Reset, Quit Button) ****

totalButton = Button(frame2Bottom, text='Total', padx=6, pady=6, bd=2, font=('arial', 15, 'bold'))
totalButton.grid(row=0, column=0)
receiptButton = Button(frame2Bottom, text='Receipt', padx=6, pady=6, bd=2, font=('arial', 15, 'bold'))
receiptButton.grid(row=0, column=1)
resetButton = Button(frame2Bottom, text='Reset', padx=6, pady=6, bd=2, font=('arial', 15, 'bold'), command=reset_project)
resetButton.grid(row=0, column=2)
exitButton = Button(frame2Bottom, text='Exit', padx=6, pady=6, bd=2, font=('arial', 15, 'bold'), command=exit_project)
exitButton.grid(row=0, column=3)

# <<<<<<<<<<<<<<<<<<<<< End Button >>>>>>>>>>>>>>>>>>>>

root.mainloop()
