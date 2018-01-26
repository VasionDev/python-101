from tkinter import *
import tkinter.messagebox
import time
import random


root = Tk()
root.geometry('1350x800+0+0')
root.title('GUI Management System')

localTime = time.asctime(time.localtime(time.time()))

# **** Create Basic Layout ****

Tops = Frame(root, width=1300, height=50, relief=SUNKEN)
Tops.pack(side=TOP)
frame_1 = Frame(root, width=600, height=700, relief=SUNKEN)
frame_1.pack(side=LEFT)
frame_2 = Frame(root, width=750, height=700, bg='powder blue', relief=SUNKEN)
frame_2.pack(side=RIGHT)
label_1 = Label(Tops, font=('arial', 40, 'bold'), text='GUI Management System', fg='steel blue', bd=10, anchor=W)
label_1.grid(row=0)
label_2 = Label(Tops, font=('arial', 20, 'bold'), text=localTime, fg='steel blue', bd=10, anchor=W)
label_2.grid(row=1, column=0)

# **** Initialization ****

text_input = StringVar()
operator = ''
calculation = ''
rand = StringVar()
fries = StringVar()
burger = StringVar()
filet = StringVar()
chicken = StringVar()
cheese = StringVar()
drinks = StringVar()
cost = StringVar()
service = StringVar()
tax = StringVar()
subtotal = StringVar()
totalcost = StringVar()

# **** Display and button Layout ****

# **** Functions/Methods ****


def btnClick(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)


def clearDisplay():
    global operator
    operator = ''
    text_input.set(operator)


def evaluate():
    global operator
    global calculation
    try:
        calculation = eval(operator)
        text_input.set(calculation)
        print('ok')
    except SyntaxError:
        text_input.set('Syntax Error')
        print('not ok')
    except ZeroDivisionError:
        text_input.set('Math Error')
        print('not ok')
    else:
        operator = ''
        btnClick(calculation)


def ref():
    random_number = random.randrange(10034, 500342)
    randstr = str(random_number)
    rand.set(randstr)
    try:
        CoFries = float(fries.get()) * 60
        fries.set(CoFries)
    except ValueError:
        CoFries = 0
        fries.set(CoFries)
        print('Initialize', type(CoFries))
    try:
        CoBurger = float(burger.get()) * 220
        burger.set(CoBurger)
    except ValueError:
        CoBurger = 0
        burger.set(CoBurger)
        print('Initialize', type(CoBurger))
    try:
        CoFilet = float(filet.get()) * 110
        filet.set(CoFilet)
    except ValueError:
        CoFilet = 0
        filet.set(CoFilet)
        print('Initialize', type(CoFilet))
    try:
        Cochicken = float(chicken.get()) * 90
        chicken.set(Cochicken)
    except ValueError:
        Cochicken = 0
        chicken.set(Cochicken)
        print('Initialize', type(Cochicken))
    try:
        Cocheese = float(cheese.get()) * 55
        cheese.set(Cocheese)
    except ValueError:
        Cocheese = 0
        cheese.set(Cocheese)
        print('Initialize', type(Cocheese))
    try:
        Codrinks = float(drinks.get()) * 40
        drinks.set(Codrinks)
    except ValueError:
        Codrinks = 0
        drinks.set(Codrinks)
        print('Initialize', type(Codrinks))
    mealcost = CoFries + CoBurger + CoFilet + Cochicken + Cocheese + Codrinks
    cost.set(mealcost)
    Coservice = mealcost * (5/100)
    service.set(Coservice)
    Cotax = mealcost * (15/100)
    tax.set(Cotax)
    Cosubtotal = mealcost + Coservice
    subtotal.set(Cosubtotal)
    Cototalcost = Cosubtotal + Cotax
    totalcost.set(Cototalcost)


def reset():
    rand.set('')
    fries.set('')
    burger.set('')
    filet.set('')
    chicken.set('')
    cheese.set('')
    drinks.set('')
    cost.set('')
    service.set('')
    tax.set('')
    subtotal.set('')
    totalcost.set('')


def btnexit():
    confirm = tkinter.messagebox.askyesno('Confirmation', 'Are you sure?')
    if confirm is True:
        root.destroy()

# **** Start Calculator Layout ****

entry1 = Entry(frame_2, font=('arial', 20, 'bold'), textvariable=text_input, bg='powder blue', bd=30, insertwidth=4, justify='right')
entry1.grid(columnspan=4)

# ==================Button(7, 8, 9, '+')====================

button7 = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick(7), text='7')
button7.grid(row=2, column=0)
button8 = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick(8), text='8')
button8.grid(row=2, column=1)
button9 = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick(9), text='9')
button9.grid(row=2, column=2)
add = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick('+'), text='+')
add.grid(row=2, column=3)

# ====================Button(4, 5, 6, '-')===================

button4 = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick(4), text='4')
button4.grid(row=3, column=0)
button5 = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick(5), text='5')
button5.grid(row=3, column=1)
button6 = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick(6), text='6')
button6.grid(row=3, column=2)
sub = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick('-'), text='-')
sub.grid(row=3, column=3)

# ====================Button(1, 2, 3, '*')===================

button1 = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick(1), text='1')
button1.grid(row=4, column=0)
button2 = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick(2), text='2')
button2.grid(row=4, column=1)
button3 = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick(3), text='3')
button3.grid(row=4, column=2)
multi = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick('*'), text='*')
multi.grid(row=4, column=3)

# =====================Button(0, 'C', '=', '/')==================

button0 = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick(0), text='0')
button0.grid(row=5, column=0)
c = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=clearDisplay, text='C')
c.grid(row=5, column=1)
equal = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=evaluate, text='=')
equal.grid(row=5, column=2)
div = Button(frame_2, font=('arial', 20, 'bold'), fg='black', bg='powder blue', bd=15, command=lambda: btnClick('/'), text='/')
div.grid(row=5, column=3)

# <<<<<<<<<< End calculator layout >>>>>>>>>>>


# **** Start food input field ****

labelReference = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Reference', anchor=W)
labelReference.grid(row=0, sticky=W)
entryReference = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=rand, justify=RIGHT, insertwidth=4)
entryReference.grid(row=0, column=1)

labelFries = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Chicken Fries', anchor=W)
labelFries.grid(row=1, sticky=W)
entryFries = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=fries, justify=RIGHT, insertwidth=4)
entryFries.grid(row=1, column=1)

labelBurger = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Burger Meal', anchor=W)
labelBurger.grid(row=2, sticky=W)
entryBurger = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=burger, justify=RIGHT, insertwidth=4)
entryBurger.grid(row=2, column=1)

labelFilet = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Filet_o_Meal', anchor=W)
labelFilet.grid(row=3, sticky=W)
entryFilet = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=filet, justify=RIGHT, insertwidth=4)
entryFilet.grid(row=3, column=1)

labelChicken = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Chicken Meal', anchor=W)
labelChicken.grid(row=4, sticky=W)
entryChicken = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=chicken, justify=RIGHT, insertwidth=4)
entryChicken.grid(row=4, column=1)

labelCheese = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Cheese Meal', anchor=W)
labelCheese.grid(row=5, sticky=W)
entryCheese = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=cheese, justify=RIGHT, insertwidth=4)
entryCheese.grid(row=5, column=1)

# ==================================================

labelDrinks = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Drinks', anchor=W)
labelDrinks.grid(row=0, column=2, sticky=W)
entryDrinks = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=drinks, justify=RIGHT, insertwidth=4)
entryDrinks.grid(row=0, column=3)

labelCost = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Cost of Meal', anchor=W)
labelCost.grid(row=1, column=2, sticky=W)
entryCost = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=cost, justify=RIGHT, insertwidth=4)
entryCost.grid(row=1, column=3)

labelService = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Service charge(5%)', anchor=W)
labelService.grid(row=2, column=2, sticky=W)
entryService = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=service, justify=RIGHT, insertwidth=4)
entryService.grid(row=2, column=3)

labelTax = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Vat(15%)', anchor=W)
labelTax.grid(row=3, column=2, sticky=W)
entryTax = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=tax, justify=RIGHT, insertwidth=4)
entryTax.grid(row=3, column=3)

labelSubtotal = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Sub Total', anchor=W)
labelSubtotal.grid(row=4, column=2, sticky=W)
entrySubtotal = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=subtotal, justify=RIGHT, insertwidth=4)
entrySubtotal.grid(row=4, column=3)

labelTotalcost = Label(frame_1, font=('arial', 16, 'bold'), bd=16, text='Total Cost', anchor=W)
labelTotalcost.grid(row=5, column=2, sticky=W)
entryTotalcost = Entry(frame_1, font=('arial', 16, 'bold'), bg='powder blue', bd=16, textvariable=totalcost, justify=RIGHT, insertwidth=4)
entryTotalcost.grid(row=5, column=3)

# ===================== Button =====================

blankLabel = Label(frame_1, text='')
blankLabel.grid(row=6)
blankLabel = Label(frame_1, text='')
blankLabel.grid(row=7)

buttonTotal = Button(frame_1, font=('arial', 16, 'bold'), text='Total', padx=8, pady=8, command=ref, bg='powder blue', bd=10, width=10)
buttonTotal.grid(row=8, column=1)

buttonReset = Button(frame_1, font=('arial', 16, 'bold'), text='Reset', padx=8, pady=8, command=reset, bg='powder blue', bd=10, width=10)
buttonReset.grid(row=8, column=2)

buttonExit = Button(frame_1, font=('arial', 16, 'bold'), text='Exit', padx=8, pady=8, command=btnexit, bg='powder blue', bd=10, width=10)
buttonExit.grid(row=8, column=3)

# <<<<<<<<<< End Input layout >>>>>>>>>>>

root.mainloop()
