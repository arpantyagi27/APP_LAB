import tkinter as t
from tkinter import messagebox
root =t.Tk()

l=t.Label(None,text="Form")
title=t.Label(None,text="TITLE")
Lastname=t.Label(None,text="LAST NAME")
Firstname= t.Label(None,text="First name")
Sharewith=t.Label(None,text="Share with")
businessno=t.Label(None,text="Business Number")
mobno=t.Label(None,text="Mobile Number")
emailadd=t.Label(None,text="Email Address")
DateofArrival=t.Label(None,text="Date of Arrival")
DateofDeparture=t.Label(None,text="Date of Departure")
Nameoncredit=t.Label(None,text="Name on Credit Card")
Creditno=t.Label(None,text="Credit card Number")
Expirydate=t.Label(None,text="Expiry Date")
cvv=t.Label(None,text="CVV Number")
paymentmethod=t.Label(None,text="Payment Method")

titlee=t.Entry(None,text="TITLE")
Lastnamee=t.Entry(None,text="LAST NAME")
Firstnamee= t.Entry(None,text="First name")
Sharewithe=t.Entry(None,text="Share with")
businessnoe=t.Entry(None,text="Business Number")
mobnoe=t.Entry(None,text="Mobile Number")
emailadde=t.Entry(None,text="Email Address")
DateofArrivale=t.Entry(None,text="Date of Arrival")
DateofDeparturee=t.Entry(None,text="Date of Departure")
Nameoncredite=t.Entry(None,text="Name on Credit Card")
Creditnoe=t.Entry(None,text="Credit card Number")
Expirydatee=t.Entry(None,text="Expiry Date")
cvve=t.Entry(None,text="CVV Number")
v = t.IntVar()

l.grid(row=0,column=6)
title.grid(row=2,column=5)
titlee.grid(row=2,column=7)
Lastname.grid(row=5,column=5)
Lastnamee.grid(row=5,column=7)
Firstname.grid(row=8,column=5)
Firstnamee.grid(row=8,column=7)
Sharewith.grid(row=11,column=5)
Sharewithe.grid(row=11,column=7)
businessno.grid(row=14,column=5)
businessnoe.grid(row=14,column=7)
mobno.grid(row=17,column=5)
mobnoe.grid(row=17,column=7)
emailadd.grid(row=20,column=5)
emailadde.grid(row=20,column=7)
DateofArrival.grid(row=23,column=5)
DateofArrivale.grid(row=23,column=7)
DateofDeparture.grid(row=26,column=5)
DateofDeparturee.grid(row=26,column=7)
Nameoncredit.grid(row=29,column=5)
Nameoncredite.grid(row=29,column=7)
Creditno.grid(row=32,column=5)
Creditnoe.grid(row=32,column=7)
Expirydate.grid(row=35,column=5)
Expirydatee.grid(row=35,column=7)
cvv.grid(row=38,column=5)
cvve.grid(row=38,column=7)
paymentmethod.grid(row=40,column=5)
CreditCard =t.Radiobutton(root,text = "Credit Card", variable = v, value =1)
CreditCard.grid(row=40, column = 7)
DBT =t.Radiobutton(root,text = "Direct Bank Transfer", variable = v, value =2)
DBT.grid(row=40, column =8)
def smit():
        messagebox.showinfo("Submitted", "Your Data has been submitted!!")
submit = t.Button(root, text = 'Submit', bd = '5', command = smit).grid(row=42,column=7)

t.mainloop()