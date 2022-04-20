from cProfile import label
from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title(":) KATA (X)  ZERO(O) :)")
beclick = True
flag = 0

def buttonclicked(b):
    global beclick , flag , plA , plB , p1_name , p2_name
    if(b["text"]==" " and beclick == True):
        b["text"] = "X"    
        flag = flag+1
        beclick = False
        Win_CHK()

    elif(b["text"]==" " and beclick == False):
        b["text"] =  "O"
        flag = flag+1
        beclick = True
        Win_CHK()

def Disable_BT():
    button1.configure(state = DISABLED)
    button2.configure(state = DISABLED)
    button3.configure(state = DISABLED)
    button4.configure(state = DISABLED)
    button5.configure(state = DISABLED)
    button6.configure(state = DISABLED)
    button7.configure(state = DISABLED)
    button8.configure(state = DISABLED)
    button9.configure(state = DISABLED)


def Win_CHK():
    if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"
    or button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"
    or button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"
    or button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"
    or button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"
    or button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"
    or button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"
    or button7["text"] == "X" and button5["text"] == "X" and button3["text"] == "X"):
        plA = P1.get()+" Wins😎"
        Disable_BT()
        tkinter.messagebox.showinfo("TIKTACTOE",plA)

    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"
    or button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"
    or button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"
    or button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"
    or button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"
    or button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"
    or button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"
    or button7["text"] == "X" and button5["text"] == "X" and button3["text"] == "X"):
        plB = p2.get()+" Wins😎"
        Disable_BT()
        tkinter.messagebox.showinfo("TIKTACTOE",plB)

    elif(flag == 9):
        Disable_BT()
        tkinter.messagebox.showinfo("TIKTACTOE","DRAW")






plA = StringVar()
plB = StringVar()
P1 = StringVar()
p2 = StringVar()


p1_name = Entry(tk, textvariable=P1)
p1_name.grid(row=1, column=1, columnspan=8)
p2_name = Entry(tk, textvariable=p2)
p2_name.grid(row=2, column=1, columnspan=8)


label = Label(tk, text="Player 1 : ",
              font="Times 20 bold", bg="white", fg="black")
label.grid(row=1, column=0)
label = Label(tk, text="Player 2 : ",
              font="Times 20 bold", bg="white", fg="black")
label.grid(row=2, column=0)


button1 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button1))
button1.grid(row=3,column=0)

button2 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button2))
button2.grid(row=4,column=0)

button3 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button3))
button3.grid(row=5,column=0)

button4 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button4))
button4.grid(row=3,column=1)

button5 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button5))
button5.grid(row=4,column=1)

button6 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button6))
button6.grid(row=5,column=1)

button7 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button7))
button7.grid(row=3,column=2)

button8 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button8))
button8.grid(row=4,column=2)

button9 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button9))
button9.grid(row=5,column=2)







tk.mainloop()
