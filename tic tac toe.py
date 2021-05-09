from tkinter import *
from tkinter import messagebox

#design of game
root=Tk()
root.title("TIC TAC TOE")
root.configure(background="black")
frame=LabelFrame(root,padx=50,pady=50).grid(padx=50,pady=50)
label1=Label(root,text="PLAYER 1 : ❌",font="Helvetica 10",bg="black",fg="white")
label1.grid(row=0,column=0)
label2=Label(root,text="🏆",font="Helvetica 50",bg="black",fg="yellow")
label2.grid(row=0,column=1)
label3=Label(root,text="PLAYER 2 : ⭕",font="Helvetica 10",bg="black",fg="white")
label3.grid(row=0,column=2)
photo = PhotoImage(file = "xo.png")
root.iconphoto(False, photo)



#winner declaration function:
def result():
    global winner,count
    winner=False
    if button1["text"]=="❌"and button2["text"]=="❌" and button3["text"]=="❌":
        button1.config(bg="#00FFFF")
        button2.config(bg="#00FFFF")
        button3.config(bg="#00FFFF")
        winner=True
        messagebox.showinfo("TIC TAC TOE 🤩","Congratulations \n Player1 has won! 🎉🏆")
    elif button4["text"]=="❌"and button5["text"]=="❌" and button6["text"]=="❌":
        button4.config(bg="#00FFFF")
        button5.config(bg="#00FFFF")
        button6.config(bg="#00FFFF")
        winner=True
        messagebox.showinfo("TIC TAC TOE 🤩","Congratulations \n Player1 has won! 🎉🏆")
    elif button7["text"]=="❌"and button8["text"]=="❌" and button9["text"]=="❌":
        button7.config(bg="#00FFFF")
        button8.config(bg="#00FFFF")
        button9.config(bg="#00FFFF")
        winner=True
        messagebox.showinfo("TIC TAC TOE 🤩","Congratulations \n Player1 has won! 🎉🏆")
    elif button1["text"]=="❌" and button4["text"]=="❌" and button7["text"]=="❌":
        button1.config(bg="#00FFFF")
        button4.config(bg="#00FFFF")
        button7.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player1 has won! 🎉🏆")
    elif button2["text"]=="❌" and button5["text"]=="❌" and button8["text"]=="❌":
        button2.config(bg="#00FFFF")
        button5.config(bg="#00FFFF")
        button8.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player1 has won! 🎉🏆")
    elif button3["text"]=="❌" and button6["text"]=="❌" and button9["text"]=="❌":
        button3.config(bg="#00FFFF")
        button6.config(bg="#00FFFF")
        button9.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player1 has won! 🎉🏆")
    elif button1["text"]=="❌" and button5["text"]=="❌" and button9["text"]=="❌":
        button1.config(bg="#00FFFF")
        button5.config(bg="#00FFFF")
        button9.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player1 has won! 🎉🏆")
    elif button3["text"]=="❌" and button5["text"]=="❌" and button7["text"]=="❌":
        button3.config(bg="#00FFFF")
        button5.config(bg="#00FFFF")
        button7.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player1 has won! 🎉🏆")
    elif button1["text"]=="⭕" and button2["text"]=="⭕" and button3["text"]=="⭕":
        button1.config(bg="#00FFFF")
        button2.config(bg="#00FFFF")
        button3.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player2 has won! 🎉🏆")
    elif button4["text"]=="⭕" and button5["text"]=="⭕" and button6["text"]=="⭕":
        button4.config(bg="#00FFFF")
        button5.config(bg="#00FFFF")
        button6.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player2 has won! 🎉🏆")
    elif button7["text"]=="⭕" and button8["text"]=="⭕" and button9["text"]=="⭕":
        button7.config(bg="#00FFFF")
        button8.config(bg="#00FFFF")
        button9.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player2 has won! 🎉🏆")
    elif button1["text"]=="⭕" and button4["text"]=="⭕" and button7["text"]=="⭕":
        button1.config(bg="#00FFFF")
        button4.config(bg="#00FFFF")
        button7.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player2 has won! 🎉🏆")
    elif button2["text"]=="⭕" and button5["text"]=="⭕" and button8["text"]=="⭕":
        button2.config(bg="#00FFFF")
        button5.config(bg="#00FFFF")
        button8.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player2 has won! 🎉🏆")
    elif button3["text"]=="⭕" and button6["text"]=="⭕" and button9["text"]=="⭕":
        button3.config(bg="#00FFFF")
        button6.config(bg="#00FFFF")
        button9.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player2 has won! 🎉🏆")
    elif button1["text"]=="⭕" and button5["text"]=="⭕" and button9["text"]=="⭕":
        button1.config(bg="#00FFFF")
        button5.config(bg="#00FFFF")
        button9.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player2 has won! 🎉🏆")
    elif button3["text"]=="⭕" and button5["text"]=="⭕" and button7["text"]=="⭕":
        button3.config(bg="#00FFFF")
        button5.config(bg="#00FFFF")
        button7.config(bg="#00FFFF")
        winner = True
        messagebox.showinfo("TIC TAC TOE 🤩", "Congratulations \n Player2 has won! 🎉🏆")
    elif count==9:
        messagebox.showinfo("TIC TAC TOE 🤩", "Game draw \n Try again!" )

press=True
count=0
# button function:
def game(button):

    global press
    global count
    if button["text"]== "" and press==True:
        button["text"] ="❌"
        count=count+1
        press = False
        result()

    elif button["text"]== "" and press==False:
        button["text"] ="⭕"
        count=count+1
        press = True
        result()


#creating buttons
button1=Button(frame,border=5,text="",font=("Helvetica",20),height=3,width=6,bg="white",command=lambda:game(button1))
button2=Button(frame,border=5,text="",font=("Helvetica",20),height=3,width=6,bg="white",command=lambda:game(button2))
button3=Button(frame,border=5,text="",font=("Helvetica",20),height=3,width=6,bg="white",command=lambda:game(button3))

button4=Button(frame,border=5,text="",font=("Helvetica",20),height=3,width=6,bg="White",command=lambda:game(button4))
button5=Button(frame,border=5,text="",font=("Helvetica",20),height=3,width=6,bg="white",command=lambda:game(button5))
button6=Button(frame,border=5,text="",font=("Helvetica",20),height=3,width=6,bg="White",command=lambda:game(button6))

button7=Button(frame,border=5,text="",font=("Helvetica",20),height=3,width=6,bg="white",command=lambda:game(button7))
button8=Button(frame,border=5,text="",font=("Helvetica",20),height=3,width=6,bg="white",command=lambda:game(button8))
button9=Button(frame,border=5,text="",font=("Helvetica",20),height=3,width=6,bg="white",command=lambda:game(button9))

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

root.mainloop()

