from tkinter import *

root = Tk()

text_Input = StringVar() 
operator = " "

f1 = Frame(root, width=800, height=700, bg="black", relief=SUNKEN)
f1.pack(side=RIGHT)

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = " "
    text_Input.set(" ")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = " "

txtDisplay = Entry(f1, font=('arial', 20, 'bold'), textvariable=text_Input,
                       bd=30, insertwidth=4, bg="grey", justify='right')
txtDisplay.grid(columnspan=4)

##---------- row 2 --------------------------------------------------------------------
btn7=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="7", bg="powderblue", command=lambda: btnClick(7)).grid(row=2, column=0)

btn8=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="8", bg="powderblue", command=lambda: btnClick(8)).grid(row=2, column=1) 

btn9=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="9", bg="powderblue", command=lambda: btnClick(9)).grid(row=2, column=2)

Addition=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="+", bg="blue", command=lambda: btnClick("+")).grid(row=2, column=3)

##------------ row 3 -------------------------------------------------------------------    
btn4=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="4", bg="powderblue", command=lambda: btnClick(4)).grid(row=3, column=0)

btn5=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="5", bg="powderblue", command=lambda: btnClick(5)).grid(row=3, column=1)
    
btn6=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="6", bg="powderblue", command=lambda: btnClick(6)).grid(row=3, column=2)

Subtraction=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="-", bg="blue", command=lambda: btnClick("-")).grid(row=3, column=3)

##---------- row 4 ---------------------------------------------------------------------
btn1=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="1", bg="powderblue", command=lambda: btnClick(1)).grid(row=4, column=0)

btn2=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="2", bg="powderblue", command=lambda: btnClick(2)).grid(row=4, column=1)
    
btn3=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="3", bg="powderblue", command=lambda: btnClick(3)).grid(row=4, column=2)

Multiply=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="*", bg="blue", command=lambda: btnClick("*")).grid(row=4, column=3)

##---------- row 5 -----------------------------------------------------------------------
btn0=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="0", bg="powderblue", command=lambda: btnClick(0)).grid(row=5, column=0)

btnClear=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="C", bg="green", command= btnClearDisplay).grid(row=5, column=1)
    
btnEquals=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="=", bg="red", command= btnEqualsInput).grid(row=5, column=2)

Division=Button(f1, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="/", bg="blue", command=lambda: btnClick("/")).grid(row=5, column=3)

##-----------------------------------------------------------------------------------------

    
root.mainloop()
