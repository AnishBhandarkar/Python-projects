from tkinter import *
import random
import time 
import datetime
import tkinter.messagebox

root = Tk()
root.geometry("1530x790+0+0")
root.title("Restaurant Management System")
root.configure(background = 'Dark Orchid3')

Tops = Frame(root, bg='Dark Orchid3', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('arial', 60, 'bold'), text="     Restaurant Management System    ", bd=21, bg='green2',
                 fg='navy', justify=CENTER)
lblTitle.grid(row=0, column=0)

RecieptCal_F = Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
RecieptCal_F.pack(side=RIGHT)
Buttons_F=Frame(RecieptCal_F, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(RecieptCal_F, bg='Powder Blue', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)
Reciept_F=Frame(RecieptCal_F, bg='Powder Blue', bd=4, relief=RIDGE)
Reciept_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='Dark Orchid3', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame, bg='Cyan', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='Dark Orchid3', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='deep sky blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F=Frame(MenuFrame, bg='deep sky blue', bd=10, relief=RIDGE)
Cake_F.pack(side=RIGHT)

#---------------------------------------------------Variables--------------------------------------------------------------------

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Black_tea= StringVar()
E_Green_tea= StringVar()
E_Sharbat= StringVar()
E_Coffee= StringVar()
E_Cappuccino= StringVar()
E_Lassi= StringVar()
E_Badam_milk= StringVar()
E_Sugarcane_Juice= StringVar()

E_Dal_Makhni= StringVar()
E_Dal_Tadka= StringVar()
E_Paneer_Tikka= StringVar()
E_Gobi_Masala= StringVar()
E_Veg_Biryani= StringVar()
E_Veg_Manchoorian= StringVar()
E_Mushroom_Masala= StringVar()
E_Paneer_Chilly= StringVar()


E_Black_tea.set("0")
E_Green_tea.set("0")
E_Sharbat.set("0")
E_Coffee.set("0")
E_Cappuccino.set("0")
E_Lassi.set("0")
E_Badam_milk.set("0")
E_Sugarcane_Juice.set("0")

E_Dal_Makhni.set("0")
E_Dal_Tadka.set("0")
E_Paneer_Tikka .set("0")
E_Gobi_Masala.set("0")
E_Veg_Biryani.set("0")
E_Veg_Manchoorian.set("0")
E_Mushroom_Masala.set("0")
E_Paneer_Chilly.set("0")


DateofOrder.set(time.strftime("%d/%m/%Y"))

#--------------------------------------------------------iExit function---------------------------------------------

def iExit():
        iExit = tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if u want to exit")
        if iExit > 0:
                root.destroy()
                return

def Reset():

        PaidTax.set("")
        SubTotal.set("")
        TotalCost.set("")
        CostofCakes.set("")
        CostofDrinks.set("")
        ServiceCharge.set("")
        txtReceipt.delete("1.0", END)

        E_Black_tea.set("0")
        E_Green_tea.set("0")
        E_Sharbat.set("0")
        E_Coffee.set("0")
        E_Cappuccino.set("0")
        E_Lassi.set("0")
        E_Badam_milk.set("0")
        E_Sugarcane_Juice.set("0")

        E_Dal_Makhni.set("0")
        E_Dal_Tadka.set("0")
        E_Paneer_Tikka .set("0")
        E_Gobi_Masala.set("0")
        E_Veg_Biryani.set("0")
        E_Veg_Manchoorian.set("0")
        E_Mushroom_Masala.set("0")
        E_Paneer_Chilly.set("0")

        var1 .set(0)
        var2 .set(0)
        var3 .set(0)
        var4 .set(0)
        var5 .set(0)
        var6 .set(0)
        var7 .set(0)
        var8 .set(0)
        var9 .set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)

        txtBlack_tea.configure(state=DISABLED)
        txtGreen_tea.configure(state=DISABLED)
        txtSharbat.configure(state=DISABLED)
        txtCoffee.configure(state=DISABLED)
        txtCappucino.configure(state=DISABLED)
        txtLassi.configure(state=DISABLED)
        txtBadam.configure(state=DISABLED)
        txtSugarcane.configure(state=DISABLED)

        txtDal_Makhni.configure(state=DISABLED)
        txtDal_Tadka.configure(state=DISABLED)
        txtPaneer.configure(state=DISABLED)
        txtGobi.configure(state=DISABLED)
        txtBiryani.configure(state=DISABLED)
        txtManchoorian.configure(state=DISABLED)
        txtMushroom.configure(state=DISABLED)
        txtChilly.configure(state=DISABLED)


def CostofItem():
        Item1=float(E_Black_tea.get())
        Item2=float(E_Green_tea.get())
        Item3=float(E_Sharbat.get())
        Item4=float(E_Coffee.get())
        Item5=float(E_Cappuccino.get())
        Item6=float(E_Lassi.get())
        Item7=float(E_Badam_milk.get())
        Item8=float(E_Sugarcane_Juice.get())

        Item9=float(E_Dal_Makhni.get())
        Item10=float(E_Dal_Tadka.get())
        Item11=float(E_Paneer_Tikka.get())
        Item12=float(E_Gobi_Masala.get())
        Item13=float(E_Veg_Biryani.get())
        Item14=float(E_Veg_Manchoorian.get())
        Item15=float(E_Mushroom_Masala.get())
        Item16=float(E_Paneer_Chilly.get())

        PriceofDrinks = (Item1 * 15) + (Item2 * 20) + (Item3 * 15) + (Item4 * 20) + (Item5 * 50) +(Item6 * 10) +(Item7 * 15) +(Item8 * 25)

        PriceofCakes = (Item9 * 85) + (Item10 * 60) + (Item11 * 75) + (Item12 * 100) + (Item13 * 250) + (Item14 * 150) + (Item15 * 120) +(Item16 * 140) 

        DrinksPrice = "₹", str('%.2f'%(PriceofDrinks))
        CakesPrice = "₹", str('%.2f'%(PriceofCakes))
        CostofCakes.set(CakesPrice)
        CostofDrinks.set(DrinksPrice)
        SC="₹", str('%.2f'%(1.59))
        ServiceCharge.set(SC)

        SubTotalofItems = "₹", str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59))
        SubTotal.set(SubTotalofItems)

        Tax = "₹", str('%.2f'%((PriceofDrinks + PriceofCakes + 1.59) * 0.15))
        PaidTax.set(Tax)
        TT = ((PriceofDrinks + PriceofCakes + 1.59) * 0.15)
        TC = "₹", str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59 + TT))
        TotalCost.set(TC) 


def chkBlack_tea():
        if (var1.get() == 1):
                txtBlack_tea.configure(state = NORMAL)
                txtBlack_tea.focus() 
                txtBlack_tea.delete(0, END)
        elif (var1.get() == 0):
                txtBlack_tea.configure(state=DISABLED)
                E_Black_tea.set("0")


def chkGreen_tea():
        if (var2.get() == 1):
                txtGreen_tea.configure(state = NORMAL)
                txtGreen_tea.focus() 
                txtGreen_tea.delete(0, END)
        elif (var2.get() == 0):
                txtGreen_tea.configure(state=DISABLED)
                E_Green_tea.set("0")


def chkSharbat():
        if (var3.get() == 1):
                txtSharbat.configure(state = NORMAL)
                txtSharbat.focus() 
                txtSharbat.delete(0, END)
        elif (var3.get() == 0):
                txtSharbat.configure(state=DISABLED)
                E_Sharbat.set("0")


def chkCoffee():
        if (var4.get() == 1):
                txtCoffee.configure(state = NORMAL)
                txtCoffee.focus() 
                txtCoffee.delete(0, END)
        elif (var4.get() == 0):
                txtCoffee.configure(state=DISABLED)
                E_Coffee.set("0")


def chkCappucino():
        if (var5.get() == 1):
                txtCappucino.configure(state = NORMAL)
                txtCappucino.focus() 
                txtCappucino.delete(0, END)
        elif (var5.get() == 0):
                txtCappucino.configure(state=DISABLED)
                E_Cappuccino.set("0")


def chkLassi():
        if (var6.get() == 1):
                txtLassi.configure(state = NORMAL)
                txtLassi.focus() 
                txtLassi.delete(0, END)
        elif (var6.get() == 0):
                txtLassi.configure(state=DISABLED)
                E_Lassi.set("0")


def chkBadam_Milk():
        if (var7.get() == 1):
                txtBadam.configure(state = NORMAL)
                txtBadam.focus() 
                txtBadam.delete(0, END)
        elif (var7.get() == 0):
                txtBadam.configure(state=DISABLED)
                E_Badam_milk.set("0")


def chkSugarcane():
        if (var8.get() == 1):
                txtSugarcane.configure(state = NORMAL)
                txtSugarcane.focus() 
                txtSugarcane.delete(0, END)
        elif (var8.get() == 0):
                txtSugarcane.configure(state=DISABLED)
                E_Sugarcane_Juice.set("0")


def chkDal_Makhni():
        if (var9.get() == 1):
                txtDal_Makhni.configure(state = NORMAL)
                txtDal_Makhni.focus() 
                txtDal_Makhni.delete(0, END)
        elif (var9.get() == 0):
                txtDal_Makhni.configure(state=DISABLED)
                E_Dal_Makhni.set("0")


def chkDal_Tadka():
        if (var10.get() == 1):
                txtDal_Tadka.configure(state = NORMAL)
                txtDal_Tadka.focus() 
                txtDal_Tadka.delete(0, END)
        elif (var10.get() == 0):
                txtDal_Tadka.configure(state=DISABLED)
                E_Dal_Tadka.set("0")


def chkPaneer_Tikka():
        if (var11.get() == 1):
                txtPaneer.configure(state = NORMAL)
                txtPaneer.focus() 
                txtPaneer.delete(0, END)
        elif (var11.get() == 0):
                txtPaneer.configure(state=DISABLED)
                E_Paneer_Tikka.set("0")


def chkGobi():
        if (var12.get() == 1):
                txtGobi.configure(state = NORMAL)
                txtGobi.focus() 
                txtGobi.delete(0, END)
        elif (var12.get() == 0):
                txtGobi.configure(state=DISABLED)
                E_Gobi_Masala.set("0")


def chkBiryani():
        if (var13.get() == 1):
                txtBiryani.configure(state = NORMAL)
                txtBiryani.focus() 
                txtBiryani.delete(0, END)
        elif (var13.get() == 0):
                txtBiryani.configure(state=DISABLED)
                E_Veg_Biryani.set("0")


def chkManchoorian():
        if (var14.get() == 1):
                txtManchoorian.configure(state = NORMAL)
                txtManchoorian.focus() 
                txtManchoorian.delete(0, END)
        elif (var14.get() == 0):
                txtManchoorian.configure(state=DISABLED)
                E_Veg_Manchoorian.set("0")


def chkMushroom():
        if (var15.get() == 1):
                txtMushroom.configure(state = NORMAL)
                txtMushroom.focus() 
                txtMushroom.delete(0, END)
        elif (var15.get() == 0):
                txtMushroom.configure(state=DISABLED)
                E_Mushroom_Masala.set("0")


def chkChilly():
        if (var16.get() == 1):
                txtChilly.configure(state = NORMAL)
                txtChilly.focus() 
                txtChilly.delete(0, END)
        elif (var16.get() == 0):
                txtChilly.configure(state=DISABLED)
                E_Paneer_Chilly.set("0")


def Receipt():
        txtReceipt.delete("1.0", END)
        x = random.randint(10903, 609235)
        randomRef = str(x)
        Receipt_Ref.set("BILL" + randomRef)

        txtReceipt.insert(END, 'Receipt Ref:\t' + Receipt_Ref.get() + '\t\t\t    ' + 'Date : ' + DateofOrder.get() + "\n")
        txtReceipt.insert(END, 'Item:\t\t\t\t    ' + "Number of Items\n")
        txtReceipt.insert(END, 'Black tea:\t\t\t\t\t' + E_Black_tea.get() + "\n")
        txtReceipt.insert(END, 'Green tea:\t\t\t\t\t' + E_Green_tea.get() + "\n")
        txtReceipt.insert(END, 'Sharbat:\t\t\t\t\t' + E_Sharbat.get() + "\n")
        txtReceipt.insert(END, 'Coffee:\t\t\t\t\t' + E_Coffee.get() + "\n")
        txtReceipt.insert(END, 'Cappucino:\t\t\t\t\t' + E_Cappuccino.get() + "\n")
        txtReceipt.insert(END, 'Lassi:\t\t\t\t\t' + E_Lassi.get() + "\n")
        txtReceipt.insert(END, 'Badam milk:\t\t\t\t\t' + E_Badam_milk.get() + "\n")
        txtReceipt.insert(END, 'Sugarcane juice:\t\t\t\t\t' + E_Sugarcane_Juice.get() + "\n")
        txtReceipt.insert(END, 'Dal Makhni:\t\t\t\t\t' + E_Dal_Makhni.get() + "\n")
        txtReceipt.insert(END, 'Dal Tadka:\t\t\t\t\t' + E_Dal_Tadka.get() + "\n")
        txtReceipt.insert(END, 'Paneer Tikka:\t\t\t\t\t' + E_Paneer_Tikka.get() + "\n")
        txtReceipt.insert(END, 'Gobi Masala:\t\t\t\t\t' + E_Gobi_Masala.get() + "\n")
        txtReceipt.insert(END, 'Veg Biryani:\t\t\t\t\t' + E_Veg_Biryani.get() + "\n")
        txtReceipt.insert(END, 'Veg Manchoorian:\t\t\t\t\t' + E_Veg_Manchoorian.get() + "\n")
        txtReceipt.insert(END, 'Mushroom Masala:\t\t\t\t\t' + E_Mushroom_Masala.get() + "\n")
        txtReceipt.insert(END, 'Paneer Chilly:\t\t\t\t\t' + E_Paneer_Chilly.get() + "\n----------------------------------------------------------------------------------------------\n")
        txtReceipt.insert(END, 'Cost of Drinks:\t\t\t' + CostofDrinks.get() + '\nTax Paid:\t\t\t'+ PaidTax.get() +"\n")
        txtReceipt.insert(END, 'Cost of Meals:\t\t\t' + CostofCakes.get() + '\nSubTotal:\t\t\t'+ str(SubTotal.get()) +"\n")
        txtReceipt.insert(END, 'Service Charge:\t\t\t' + ServiceCharge.get() + '\nTotal Cost:\t\t\t'+ str(TotalCost.get()))

#------------------------------------------Beverages--------------------------------------------------------------------
Black_tea = Checkbutton(Drinks_F, text="Black tea", variable=var1, onvalue=1, offvalue=0, font=('Courier', 18, 'bold'),
        bg='deep sky blue', command = chkBlack_tea).grid(row=0, sticky=W)
Green_tea = Checkbutton(Drinks_F, text="Green tea", variable=var2, onvalue=1, offvalue=0, font=('Courier', 18, 'bold'),
        bg='deep sky blue', command = chkGreen_tea).grid(row=1, sticky=W)
Sharbat = Checkbutton(Drinks_F, text="Sharbat", variable=var3, onvalue=1, offvalue=0, font=('Courier', 18, 'bold'),
        bg='deep sky blue', command = chkSharbat).grid(row=2, sticky=W)
Coffee = Checkbutton(Drinks_F, text="Coffee", variable=var4, onvalue=1, offvalue=0, font=('Courier', 18, 'bold'),
        bg='deep sky blue', command = chkCoffee).grid(row=3, sticky=W)
Cappuccino = Checkbutton(Drinks_F, text="Cappuccino", variable=var5, onvalue=1, offvalue=0, font=('Courier', 18, 'bold'),
        bg='deep sky blue', command = chkCappucino).grid(row=4, sticky=W)
Lassi = Checkbutton(Drinks_F, text="Lassi", variable=var6, onvalue=1, offvalue=0, font=('Courier', 18, 'bold'),
        bg='deep sky blue', command = chkLassi).grid(row=5, sticky=W)
Badam_milk = Checkbutton(Drinks_F, text="Badam milk", variable=var7, onvalue=1, offvalue=0, font=('Courier', 18, 'bold'),
        bg='deep sky blue', command = chkBadam_Milk).grid(row=6, sticky=W)
Sugarcane_Juice = Checkbutton(Drinks_F, text="Sugarcane Juice\t       ", variable=var8, onvalue=1, offvalue=0, font=('Courier', 18, 'bold'),
        bg='deep sky blue', command = chkSugarcane).grid(row=7, sticky=W)

#-------------------------------------------------Entry Box for Beverages-------------------------------------------------------------------

txtBlack_tea = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Black_tea)
txtBlack_tea.grid(row = 0, column=1)
txtGreen_tea = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Green_tea)
txtGreen_tea.grid(row = 1, column=1)
txtSharbat = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Sharbat)
txtSharbat.grid(row = 2, column=1)
txtCoffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Coffee)
txtCoffee.grid(row = 3, column=1)
txtCappucino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Cappuccino)
txtCappucino.grid(row = 4, column=1)
txtLassi = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Lassi)
txtLassi.grid(row = 5, column=1)
txtBadam = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Badam_milk)
txtBadam.grid(row = 6, column=1)
txtSugarcane = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Sugarcane_Juice)
txtSugarcane.grid(row = 7, column=1)


#-------------------------------------------------Meals-------------------------------------------------------------------

Dal_Makhni = Checkbutton(Cake_F, text="Dal Makhni\t\t", variable=var9, onvalue=1, offvalue=0, font=('Courier', 17, 'bold'),
        bg='deep sky blue', command = chkDal_Makhni).grid(row=0, sticky=W)
Dal_Tadka = Checkbutton(Cake_F, text="Dal Tadka", variable=var10, onvalue=1, offvalue=0, font=('Courier', 17, 'bold'),
        bg='deep sky blue', command = chkDal_Tadka).grid(row=1, sticky=W)
Paneer_Tikka = Checkbutton(Cake_F, text="Paneer Tikka", variable=var11, onvalue=1, offvalue=0, font=('Courier', 17, 'bold'),
        bg='deep sky blue', command = chkPaneer_Tikka).grid(row=2, sticky=W)
Gobi_Masala = Checkbutton(Cake_F, text="Gobi Masala", variable=var12, onvalue=1, offvalue=0, font=('Courier', 17, 'bold'),
        bg='deep sky blue', command = chkGobi).grid(row=3, sticky=W)
Veg_Biryani = Checkbutton(Cake_F, text="Veg Biryani", variable=var13, onvalue=1, offvalue=0, font=('Courier', 17, 'bold'),
        bg='deep sky blue', command = chkBiryani).grid(row=4, sticky=W)
Veg_Manchoorian = Checkbutton(Cake_F, text="Veg Manchoorian", variable=var14, onvalue=1, offvalue=0, font=('Courier', 17, 'bold'),
        bg='deep sky blue', command = chkManchoorian).grid(row=5, sticky=W)
Mushroom_Masala = Checkbutton(Cake_F, text="Mushroom Masala", variable=var15, onvalue=1, offvalue=0, font=('Courier', 17, 'bold'),
        bg='deep sky blue', command = chkMushroom).grid(row=6, sticky=W)
Paneer_Chilly = Checkbutton(Cake_F, text="Paneer Chilly", variable=var16, onvalue=1, offvalue=0, font=('Courier', 17, 'bold'),
        bg='deep sky blue', command = chkChilly).grid(row=7, sticky=W)


#-------------------------------------------------Entry Box for Meals-------------------------------------------------------------------

txtDal_Makhni = Entry(Cake_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Dal_Makhni)
txtDal_Makhni.grid(row = 0, column=1)
txtDal_Tadka = Entry(Cake_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Dal_Tadka)
txtDal_Tadka.grid(row = 1, column=1)
txtPaneer = Entry(Cake_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Paneer_Tikka)
txtPaneer.grid(row = 2, column=1)
txtGobi = Entry(Cake_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Gobi_Masala)
txtGobi.grid(row = 3, column=1)
txtBiryani = Entry(Cake_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Veg_Biryani)
txtBiryani.grid(row = 4, column=1)
txtManchoorian = Entry(Cake_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Veg_Manchoorian)
txtManchoorian.grid(row = 5, column=1)
txtMushroom = Entry(Cake_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Mushroom_Masala)
txtMushroom.grid(row = 6, column=1)
txtChilly = Entry(Cake_F, font=('arial', 16, 'bold'), bd=8, width=8, justify=LEFT, state=DISABLED, textvariable=E_Paneer_Chilly)
txtChilly.grid(row = 7, column=1)

#------------------------------------------------------Total Cost-----------------------------------------------------------------

lblCostOfDrinks = Label(Cost_F, font=('arial', 14, 'bold'), text="   Cost of Beverages\t  ", bd=21, bg='Cyan', fg='black')
lblCostOfDrinks.grid(row=0, column=0, sticky=W)
txtCostOfDrinks = Entry(Cost_F, bg="white", bd = 7, insertwidth=2, font=('arial', 14, 'bold'), justify=RIGHT, textvariable=CostofDrinks)
txtCostOfDrinks.grid(row=0, column=1)

lblCostOfMeals = Label(Cost_F, font=('arial', 14, 'bold'), text="  Cost of Meals   ", bd=21, bg='Cyan', fg='black')
lblCostOfMeals.grid(row=1, column=0, sticky=W)
txtCostOfMeals = Entry(Cost_F, bg="white", bd = 7, insertwidth=2, font=('arial', 14, 'bold'), justify=RIGHT, textvariable=CostofCakes)
txtCostOfMeals.grid(row=1, column=1)

lblServicecharge = Label(Cost_F, font=('arial', 14, 'bold'), text="  Service Charge   ", bd=21, bg='Cyan', fg='black')
lblServicecharge.grid(row=2, column=0, sticky=W)
txtServicecharge = Entry(Cost_F, bg="white", bd = 7, font=('arial', 14, 'bold'), justify=RIGHT, textvariable=ServiceCharge)
txtServicecharge.grid(row=2, column=1)

#------------------------------------------------------Payment information-----------------------------------------------------------------

lblPaidTax = Label(Cost_F, font=('arial', 14, 'bold'), text="\tPaid Tax\t", bd=7, bg='Cyan', fg='black')
lblPaidTax.grid(row=0, column=2, sticky=W)
txtPaidTax = Entry(Cost_F, bg="white", bd = 7, insertwidth=2, font=('arial', 14, 'bold'), justify=RIGHT, textvariable=PaidTax)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F, font=('arial', 14, 'bold'), text="\tSub Total", bd=7, bg='Cyan', fg='black')
lblSubTotal.grid(row=1, column=2, sticky=W)
txtSubTotal = Entry(Cost_F, bg="white", bd = 7, insertwidth=2, font=('arial', 14, 'bold'), justify=RIGHT, textvariable=SubTotal)
txtSubTotal.grid(row=1, column=3)

lblTotalCost = Label(Cost_F, font=('arial', 14, 'bold'), text="\tTotal Cost", bd=7, bg='Cyan', fg='black')
lblTotalCost.grid(row=2, column=2, sticky=W)
txtTotalCost = Entry(Cost_F, bg="white", bd = 7, insertwidth=2, font=('arial', 14, 'bold'), justify=RIGHT, textvariable=TotalCost)
txtTotalCost.grid(row=2, column=3)

#------------------------------------------------------Reciept-----------------------------------------------------------------

txtReceipt = Text(Reciept_F, width = 53, height = 12, bg="white", bd = 4, font=('arial', 12, 'bold'))
txtReceipt.grid(row=0, column=0)

#------------------------------------------------------Receipt Buttons-----------------------------------------------------------------

btnTotal = Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="Total", 
           bg='deep sky blue', command=CostofItem).grid(row=0, column=0)
btnReceipt = Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="Receipt", 
           bg='deep sky blue', command=Receipt).grid(row=0, column=1)
btnReset = Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="Reset", 
           bg='deep sky blue', command=Reset).grid(row=0, column=2)
btnExit = Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="Exit", 
           bg='deep sky blue', command=iExit).grid(row=0, column=3)

#------------------------------------------------------Calculator Display-----------------------------------------------------------------

def btnClick(numbers):
        global operator
        operator = operator + str(numbers)
        text_Input.set(operator)

def btnClear():
        global operator
        operator = ""
        text_Input.set("")

def btnEquals():
        global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ""

txtDisplay = Entry(Cal_F, width = 53, bg="white", bd = 4, font=('arial', 12, 'bold'), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

#------------------------------------------------------Calculator Buttons-----------------------------------------------------------------

btn1 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="1", 
           bg='cyan3', command = lambda:btnClick(1)).grid(row=2, column=0)
btn2 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="2", 
           bg='cyan3', command = lambda:btnClick(2)).grid(row=2, column=1)
btn3 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="3", 
           bg='cyan3', command = lambda:btnClick(3)).grid(row=2, column=2)
btnAdd = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="+", 
           bg='deep sky blue', command = lambda:btnClick("+")).grid(row=2, column=3)

btn4 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="4", 
           bg='cyan3', command = lambda:btnClick(4)).grid(row=3, column=0)
btn5 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="5", 
           bg='cyan3', command = lambda:btnClick(5)).grid(row=3, column=1)
btn6 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="6", 
           bg='cyan3', command = lambda:btnClick(6)).grid(row=3, column=2)
btnSub = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="-", 
           bg='deep sky blue', command = lambda:btnClick("-")).grid(row=3, column=3)

btn7 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="7", 
           bg='cyan3', command = lambda:btnClick(7)).grid(row=4, column=0)
btn8 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="8", 
           bg='cyan3', command = lambda:btnClick(8)).grid(row=4, column=1)
btn9 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="9", 
           bg='cyan3', command = lambda:btnClick(9)).grid(row=4, column=2)
btnMul = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="*", 
           bg='deep sky blue', command = lambda:btnClick("*")).grid(row=4, column=3)

btn0 = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="0", 
           bg='deep sky blue', command = lambda:btnClick(0)).grid(row=5, column=0)
btnClear = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="C", 
           bg='deep sky blue', command = btnClear).grid(row=5, column=1)
btnEquals = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="=", 
           bg='deep sky blue', command = btnEquals).grid(row=5, column=2)
btnDiv = Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=5, text="/", 
           bg='deep sky blue', command = lambda:btnClick("/")).grid(row=5, column=3)

#----------------------------------------------------------------------------------------------------------------------


menubar = Menu(Tops)
aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="Created By Anish Bhandarkar")

root.config(menu=menubar)

root.mainloop()


