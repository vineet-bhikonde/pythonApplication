from tkinter import*
import time
import random
from threading import Thread
root=Tk()
root.geometry("1600x800+0+0")
root.title("Restaurent Management System")

text_Input=StringVar()
operator=""

Tops=Frame(root,width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)



#systemInfo
lblinfo=Label(Tops,font=('arial',50,'bold'),text="Restaurent Management System",fg="Steel Blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)

#TimeInfo
def timer():
	while True:
		localtime=time.asctime(time.localtime(time.time()))	
		timelbl=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
		timelbl.grid(row=1,column=0)
t1=Thread(target=timer)
t1.start()
#Calculator
def btnClick(number):
	global operator
	operator=operator+str(number)
	text_Input.set(operator)

def btnClearDisplay():
	global operator
	operator=""
	text_Input.set(operator)

def btnEquals():
	global operator
	sumup=str(eval(operator))
	text_Input.set(sumup)
	operator=""

txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=10,insertwidth=4,
						bg="powder blue",justify='right').grid(row=0,column=0)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='7',bg="powder blue",
						command=lambda:btnClick(7),justify="left").grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='8',bg="powder blue",
						command=lambda:btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='9',bg="powder blue",
						command=lambda:btnClick(9)).grid(row=2,column=2)

add=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='+',bg="powder blue",
						command=lambda:btnClick('+')).grid(row=2,column=3)

btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='4',bg="powder blue",
						command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='5',bg="powder blue",
						command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='6',bg="powder blue",
						command=lambda:btnClick(6)).grid(row=3,column=2)

sub=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='-',bg="powder blue",
						command=lambda:btnClick('-')).grid(row=3,column=3)

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='1',bg="powder blue",
						command=lambda:btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='2',bg="powder blue",
						command=lambda:btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='3',bg="powder blue",
						command=lambda:btnClick(3)).grid(row=4,column=2)

mul=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='*',bg="powder blue",
						command=lambda:btnClick('*')).grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='0',bg="powder blue",
						command=lambda:btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='C',bg="powder blue",
						command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='=',bg="powder blue",
						command=btnEquals).grid(row=5,column=2)

div=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',10,'bold'),text='/',bg="powder blue",
						command=lambda:btnClick('/')).grid(row=5,column=3)

#frame1
rand=StringVar()
Fries=StringVar()
Burger=StringVar()
Filet=StringVar()
Chicken=StringVar()
Cheese=StringVar()
Subtotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()

def btnTotal():
	x=random.randint(12908,50809)
	rand.set(str(x))

	CostFries=float(Fries.get())*0.99
	CostDrinks=float(Drinks.get())*1.00
	CostBurger=float(Burger.get())*2.99
	CostFilet=float(Filet.get())*2.87
	CostChicken=float(Chicken.get())*2.89
	CostCheese=float(Cheese.get())*2.69

	sumup=CostFries+CostCheese+CostChicken+CostFilet+CostBurger+CostDrinks
	Cost.set(("$",str('%.2f'%(sumup))))
	Tax.set(("$",str('%.2f'%(sumup*0.2))))
	Service_Charge.set(("$",str('%.2f'%(sumup/99))))
	totalCost=float(Tax.get())+sumup+float(Service_Charge.get())
	Total.set(("$",str('%.2f'%(totalCost))))
	Subtotal.set(("$",str(float(Tax.get())+sumup)))


def btnExit():
	root.destroy()

def btnReset():
	rand.set("")
	Fries.set("")
	Burger.set("")
	Filet.set("")
	Chicken.set("")
	Cheese.set("")
	Subtotal.set("")
	Total.set("")
	Service_Charge.set("")
	Drinks.set("")
	Tax.set("")
	Cost.set("")


lblReference=Label(f1,font=('arial',16,'bold'),text="Reference",bd=16,anchor="w").grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=0,column=1)

lblFries=Label(f1,font=('arial',16,'bold'),text="LargeFries",bd=16,anchor="w").grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=1,column=1)

lblBurger=Label(f1,font=('arial',16,'bold'),text="Burger",bd=16,anchor="w").grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=2,column=1)

lblFilet=Label(f1,font=('arial',16,'bold'),text="Filel_o_Meal",bd=16,anchor="w").grid(row=3,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=Filet,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=3,column=1)

lblChicken=Label(f1,font=('arial',16,'bold'),text="Chicken",bd=16,anchor="w").grid(row=4,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=Chicken,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=4,column=1)

lblCheese=Label(f1,font=('arial',16,'bold'),text="Cheese",bd=16,anchor="w").grid(row=5,column=0)
txtCheese=Entry(f1,font=('arial',16,'bold'),textvariable=Cheese,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=5,column=1)

lblDrinks=Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor="w").grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=0,column=3)

lblCost=Label(f1,font=('arial',16,'bold'),text="Cost",bd=16,anchor="w").grid(row=1,column=2)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=1,column=3)

lblService=Label(f1,font=('arial',16,'bold'),text="Service Charge",bd=16,anchor="w").grid(row=2,column=2)
txtService=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=2,column=3)

lblStateTax=Label(f1,font=('arial',16,'bold'),text="State Tax",bd=16,anchor="w").grid(row=3,column=2)
txtStateTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=3,column=3)

lblSubTotal=Label(f1,font=('arial',16,'bold'),text="Sub Total",bd=16,anchor="w").grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Subtotal,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=4,column=3)

lblTotalCost=Label(f1,font=('arial',16,'bold'),text="Total Cost",bd=16,anchor="w").grid(row=5,column=2)
txtCheese=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,
						bg="powder blue",justify="right").grid(row=5,column=3)

#buttons
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',10,'bold'),width=10,
					text="Total",bg="powder blue",command=btnTotal).grid(row=7,column=1)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',10,'bold'),width=10,
					text="Exit",bg="powder blue",command=btnExit).grid(row=7,column=3)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',10,'bold'),width=10,
					text="Reset",bg="powder blue",command=btnReset).grid(row=7,column=2)

root.mainloop()