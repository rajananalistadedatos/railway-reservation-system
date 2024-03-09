from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont
import time
import random
import sqlite3
global  x1,x2,x3,x4
import tkinter.ttk as ttk
import requests
from tkcalendar import DateEntry
import razorpay
import tkinter as tk
import webbrowser

#amount_entry = None
# Create a new instance of Razorpay client
keyid = 'rzp_live_5ZpQe6njT1nrd3'
keysecret = 'ukjQIwQzV7a9oJM0whWc9yJM'
client = razorpay.Client(auth=(keyid, keysecret))

global conn, cursor , amount_entry
conn = sqlite3.connect('Railway.db')
c = conn.cursor()

global LoginId,count
global Password
global Source
global Destination
global Date
global Name
global Age,Gender,IdProof
global variable,variable1,variable2,v2,var
global DepartureTime, TrainNumber, Number
root = Tk()
root.title("Railway Reservation System")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 400
height = 400
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)



w = 400
h = 400
canvas = Canvas(root, width=w, height=h)
canvas.config(bg='light blue')
canvas.pack()

my_image = PhotoImage(file='Train.gif')
my_img = canvas.create_image(0, 0, anchor=NW, image=my_image)

Label(root, text="INDIAN RAILWAYS",font=('Slab Serif',17),bg='Orange').place(x=100,y=150)
Label(root, text="Username",font=('Slab Serif',15),bg='#0B1D51', foreground='white').place(x=60,y=200)
Label(root, text="Password",font=('Slab Serif',15), bg='#0B1D51', foreground='white').place(x=60,y=240)
entry_1 = Entry(root, font=('Slab Serif',13))
entry_1.place(x=160,y=200,height=30)

entry_2 = Entry(root, font=('Slab Serif',13),show="*")
entry_2.place(x=160,y=240,height=30)

def newUser():
    db=sqlite3.connect('railway.db')
    signUp = Tk()
    signUp.title("Sign Up Page")
    screen_width = signUp.winfo_screenwidth()
    screen_height = signUp.winfo_screenheight()
    width = 400
    height = 250
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    signUp.geometry('%dx%d+%d+%d' % (width, height, x+450, y))
    signUp.resizable(0, 0)


    lb1=Label(signUp,text='Username',bg='black',font=('Arial',10,'bold'),fg='white')
    lb1.place(x=80,y=40)
    e1=Entry(signUp,width=22,font=('arial',9,'bold'),bd=4,relief='groove')
    e1.place(x=160,y=40)

    lb2=Label(signUp,text='Password',bg='black',font=('Arial',10,'bold'),fg='white')
    lb2.place(x=80,y=100)
    e2=Entry(signUp,width=22,show='*',font=('arial',9,'bold'),bd=4,relief='groove')
    e2.place(x=160,y=100)

    def signUpBtn():
        if len(e1.get()) == 0 or len(e2.get()) == 0:
            tkinter.messagebox.showinfo('sign up result', 'ENTER BOTH YOUR USERNAME & PASSWORD TO SIGN UP')
        else:
            cursor=db.cursor()
            cursor.execute(f"INSERT INTO NewUser VALUES('{e1.get()}','{e2.get()}');")
            db.commit()
            db.close()
            tkinter.messagebox.showinfo('sign up result', 'CONGRATULATIONS!! SIGN UP IS SUCCESSFUL')
            signUp.destroy()

    btn1=Button(signUp,text='Sign Up',fg='black',bg='yellow',font=('Arial',11,'bold'),activebackground='black',activeforeground='yellow',command=signUpBtn,cursor='hand2')
    btn1.place(x=150,y=160,width=100)





def printMsg():
    db=sqlite3.connect('railway.db')
    cursor=db.cursor()
    # fetching usernames
    cursor.execute(f"SELECT Username FROM NewUser")
    usernames = [row[0] for row in cursor.fetchall()]
    # fetching passwords
    cursor.execute(f"SELECT Password FROM NewUser")
    passwords = [row[0] for row in cursor.fetchall()]

    if((entry_1.get() in usernames and entry_2.get() in passwords)):
        # tkinter.messagebox.showinfo('login result', 'CONGRATULATIONS!! LOGIN SUCCESSFUL')
        root.destroy()
        createWindow()
    else:
        tkinter.messagebox.showinfo('login result', 'LOGIN FAILED!:( TRY AGAIN')

def createWindow():
    window = Tk()
    window.title("Login Frame")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width = 410
    height = 400
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.resizable(0, 0)

    window.config(bg='light blue')

    entry1 =Entry(window,justify='center',font=('Slab Serif',3))
    entry1.place(x=210,y=70)

    entry2 = Entry(window, justify='center',font=('Slab Serif', 3))
    entry2.place(x=210, y=115)

    entry3 = Entry(window, justify='center',font=('Slab Serif', 3))
    entry3.place(x=210, y=205)


    def fun_1(*args):
        entry1.insert(10,variable.get())
        print(variable.get())

    def fun_2(*args):
        entry2.insert(10,variable1.get())
        print(variable1.get())

    def fun_3(*args):
        entry3.insert(10,variable2.get())

    cities = ['Kolkata', 'Ajmer','Mumbai','Hyderabad','Delhi','Bangalore','Amritsar','Lucknow']

    variable = StringVar(window)
    variable.set('Select')
    variable.trace("w", fun_1)
    popupMenu = OptionMenu(window, variable, *cities)
    popupMenu.place(x=210, y=70,width=130)
    popupMenu.config(font=('Slab Serif',10),bg="#218380")
    Label(window, text="Source",font=('Slab Serif',15), bg="#0B1D51", foreground="white").place(x=100,y=72,width=100)

    variable1 = StringVar(window)
    print(variable1)
    variable1.set('Select')
    variable1.trace("w", fun_2)
    popupMenu1 = OptionMenu(window, variable1, *cities)
    Label(window, text="Destination",font=('Slab Serif',15), bg='#0B1D51', foreground='white').place(x=100,y=117,width=100)
    popupMenu1.config(font=('Slab Serif',10),bg="#218380")
    popupMenu1.place(x=210,y=115,width=130)

    variable2 = StringVar(window)
    classes = ['1A','2A','3A']
    variable2.set('Select')
    variable2.trace("w", fun_3)

    popupMenu1 = OptionMenu(window, variable2, *classes)
    Label(window, text="Class", font=('Slab Serif', 15), bg='#0B1D51', foreground='white').place(x=100, y=207, width=100)
    popupMenu1.config(font=('Slab Serif', 10), bg="#218380")
    popupMenu1.place(x=210, y=205, width=130)

    def ins_date(*args):
        e1.insert(10,cal.get_date())

    Label(window,text="Date",font=('Slab Serif',15), bg='#0B1D51', foreground='white').place(x=100,y=162,width=100)
    Date=StringVar()
    e1=Entry(window,textvariable=Date,font=('Slab Serif',13),bg="#218380",width=150)
    cal = DateEntry(window, height=2, width=17,date_pattern='dd/mm/yyyy', background="#0B1D51", foreground='white', borderwidth=2)
    cal.place(x=210,y=165)
    cal.bind("<<DateEntrySelected>>", ins_date)



    def Check():
        if len(e1.get()) == 0 or len(entry1.get()) == 0 or len(entry2.get()) == 0 or len(entry3.get()) == 0:
            tkinter.messagebox.showinfo('Error','enter all required fields!')
        elif variable.get() == variable1.get():
            tkinter.messagebox.showinfo('Error','both the fields are same can\'t proceed further')
        else:
            window.destroy()
            showTrains()


    def showTrains():
        show=Tk()
        show.title("Railway Schedule")
        show.config(bg='light blue')
        screen_width = show.winfo_screenwidth()
        screen_height = show.winfo_screenheight()
        width = 1200
        height = 200
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        show.geometry('%dx%d+%d+%d' % (width, height, x, y))
        show.resizable(0, 0)
        entries = {}
        buttons = {}
        counter = 0
        for row in range(5):
            for column in range(7):
                entry = tk.Entry(show, justify="center",font=('Slab Serif',10))
                entry.grid(row=row, column=column,sticky="nsew")
                entries[f"{counter}"] = entry
                counter += 1


        def PassengerDetails():
            show.destroy()
            passdet = Tk()
            passdet.title("Passengers Details")
            passdet.config(bg="light blue")
            screen_width = passdet.winfo_screenwidth()
            screen_height = passdet.winfo_screenheight()
            width = 720
            height = 200
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            passdet.geometry('%dx%d+%d+%d' % (width, height, x, y))
            passdet.resizable(0, 0)

            pentries = {}
            counter = 0
            for row in range(5):
                for column in range(5):
                    if counter<5:
                        entry = tk.Entry(passdet, justify="center",font=('Slab Serif', 10), bg="orange")
                    else:
                        entry = tk.Entry(passdet, justify="center",font=('Slab Serif', 10), bg="#218380")
                    entry.grid(row=row, column=column,sticky="nsew")
                    pentries[f"{counter}"] = entry
                    counter += 1

            # inserting headings to the table
            pentries["0"].insert(10, "S.No")
            pentries["1"].insert(10, "Name")
            pentries["2"].insert(10, "Age")
            pentries["3"].insert(10, "Gender")
            pentries["4"].insert(10, "IdProof")
            pentries["5"].insert(10, "1")
            pentries["10"].insert(10, "2")
            pentries["15"].insert(10, "3")
            pentries["20"].insert(10, "4")

            genders = ['Male', 'Female','Other']
            # gen.trace("w", fun2)
            genmenus = {}
            for i in range(1,5):
                gen = StringVar(passdet)
                genMenu = OptionMenu(passdet, gen, *genders)
                genMenu.config(font=('Slab Serif', 9),width=9, bg='#0B1D51', fg='white')
                genMenu.grid(row=i, column=3,sticky="nsew")
                gen.set('Select')
                genmenus[f"{i}"] = genMenu

            proofs = ["Aadhar Card","Pan Card"]
            proofmenus = {}
            for i in range(1,5):
                pf = StringVar(passdet)
                proofMenu = OptionMenu(passdet, pf, *proofs)
                proofMenu.config(font=('Slab Serif', 9),width=9,bg='#0B1D51', fg='white')
                proofMenu.grid(row=i, column=4,sticky="nsew")
                pf.set('Select')
                proofmenus[f"{i}"] = proofMenu

                def process_payment():         
                    paypage = Tk()
                    paypage.title("Payment Page")
                    screen_width = paypage.winfo_screenwidth()
                    screen_height = paypage.winfo_screenheight()
                    width = 400
                    height = 400
                    x = (screen_width/2) - (width/2)
                    y = (screen_height/2) - (height/2)
                    paypage.geometry('%dx%d+%d+%d' % (width, height, x-450, y))
                    paypage.resizable(0, 0)
                    canvas = Canvas(paypage, width=400, height=400)
                    canvas.config(bg='light blue')
                    canvas.pack()


                    def pay():
                        keyid = 'rzp_live_5ZpQe6njT1nrd3'
                        keysecret = 'ukjQIwQzV7a9oJM0whWc9yJM'
                        client = razorpay.Client(auth=(keyid, keysecret))
                        webbrowser.open_new('https://rzp.io/l/ZyeFnkH')
                        tkinter.messagebox.showinfo("Ticket", "You will get your ticket in your E-mail box")

                    # Define the widgets
                    Label(paypage, text="Would you like to proceed?",font=('Slab Serif',17),bg='#6cadd4',fg="yellow").place(x=0,y=120,width=400)
                    Label(paypage, text="Your ticket Price is ₹1 ",font=('Slab Serif',17),bg='#509ccc',fg="yellow").place(x=0,y=170,width=400)
                    Button(paypage, text="Pay ",font=('Slab Serif',15),bg='blue',fg='white', command=pay).place(x=150,y=290,width=100)
                    paybtn = Button(paypage, text="Pay",font=('Slab Serif',15),bg='blue',fg='white', command=pay)
                    paybtn.place(x=150,y=290,width=100)

            paypgbtn = Button(passdet, text="Payment",font=('Slab Serif',15),bg='blue',fg='white', command=process_payment)
            paypgbtn.place(x=310,y=155,width=100)

                        
        # making an placing book buttons
        for row in range(1,5):
            button = Button(show,text="Book",font=('Slab Serif',9),width=26,bg="#218380",command=PassengerDetails)
            button.grid(row=row,column=7,sticky="nsew")
            buttons[f"{counter}"] = button
            counter += 1


        # inserting train details
        entries["0"].insert(10, "Train No.")
        entries["1"].insert(10, "Train Name")
        entries["2"].insert(10, "Source")
        entries["3"].insert(10, "Departure time")
        entries["4"].insert(10, "Destination")
        entries["5"].insert(10, "Arrival Time")
        entries["6"].insert(10, "Class")


        db=sqlite3.connect('railway.db')
        cursor=db.cursor()
        # fetching dataas from databases
        cursor.execute(f"SELECT TrainNo FROM {variable.get()}2{variable1.get()}")
        TrainNo = [data[0] for data in cursor.fetchall()]
        cursor.execute(f"SELECT TrainName FROM {variable.get()}2{variable1.get()}")
        TrainNms = [data[0] for data in cursor.fetchall()]
        cursor.execute(f"SELECT dtime FROM {variable.get()}2{variable1.get()}")
        dtime = [data[0] for data in cursor.fetchall()]
        cursor.execute(f"SELECT atime FROM {variable.get()}2{variable1.get()}")
        atime = [data[0] for data in cursor.fetchall()]

        # inserting datas into the entries
        counter = 0
        for i in range(7,35,7):
            entries[f"{i}"].insert(10,TrainNo[counter])
            entries[f"{i+1}"].insert(10,TrainNms[counter])
            entries[f"{i+2}"].insert(10,variable.get())
            entries[f"{i+3}"].insert(10,dtime[counter])
            entries[f"{i+4}"].insert(10,variable1.get())
            entries[f"{i+5}"].insert(10,atime[counter])
            entries[f"{i+6}"].insert(10,variable2.get())
            counter+=1

        for i in range(35):
            if i<7:
                entries[f"{i}"].config(state="disabled",disabledbackground="blue",disabledforeground="white")
            else:
                entries[f"{i}"].config(state="disabled",disabledforeground="black")
        # back button
        def back():
            show.destroy()
            createWindow()

        button5 = Button(show, text="Back",font=('Slab Serif',17), bg="cyan", command=back)
        button5.place(x=500,y=150,width=200)


    
    def Cancellation():
        window.destroy()
        window4 = Tk()
        window4.title("Cancel Ticket")

        screen_width = window4.winfo_screenwidth()
        screen_height = window4.winfo_screenheight()
        width = 400
        height = 400
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window4.geometry('%dx%d+%d+%d' % (width, height, x, y))
        window4.resizable(0, 0)

        window4.config(bg='purple')
        cancel = Label(window4, text="PNR NO", font=('Slab Serif', 15), bg="purple", fg="white").place(x=100, y=150,
                                                                                                       width=90)
        e=Entry(window4,justify="center", font=('Slab Serif', 15), bg="white")
        e.place(x=210, y=150, width=150)


        def Delete1():
            result = tkinter.messagebox.askquestion('Ask', 'Are you sure you want to delete your booked ticket?',
                                              icon="warning")
            if result == 'yes':
                cursor = conn.cursor()
                cursor.execute("Select pnr from Rail999")
                d = cursor.fetchall()

                at=str(d)
                d1=at.replace('(','')
                d2 = d1.replace(')', '')
                d3 = d2.replace(',', '')
                d4=d3.replace('[','')
                d5 = d4.replace(']', '')
                d6=d5.split(' ')


                q=0
                for i in range(1,len(d6)):
                    if e.get()==d6[i]:
                        x123=e.get()
                        q=1
                if q==1:
                    cursor.execute("Delete from Rail999 where pnr=?",(x123,))
                    tkinter.messagebox.showinfo('Success', 'Ticket Deleted Successfully')
                    window4.destroy()
                else:
                    tkinter.messagebox.showinfo('Error', 'Ticket Not Found!')

                cursor.close()
                conn.close()


        def Delete():
            if (len(e.get())==""):
                tkinter.messagebox.showinfo('Error', 'Enter required pnr no.')
            else:
                Delete1()
        
        def Back():
            window4.destroy()
            createWindow()


        Button(window4, text="Back", font=('Slab Serif', 15), bg="green", fg="white",command=Back).place(x=80,y=250, width=120)

        Button(window4, text="Delete", font=('Slab Serif', 15), bg="green", fg="white",command=Delete
               ).place(x=220, y=250, width=120)
        mainloop()
    e1.config(bg="#218380")
    e1.place(x=210,y=165,height=10,width=125)

    Button(window,text="Search trains",font=('Slab Serif',15), bg="green",fg="white",command=Check).place(x=80,y=250,width=120)

    Button(window, text="Cancellation",font=('Slab Serif',15), bg="green",fg="white",command=Cancellation).place(x=220,y=250,width=120)

    mainloop()


button_1 = Button(root, text="Login",font=('Slab Serif',15),bg='blue',fg='white', command=printMsg).place(x=70,y=290,width=100)
button_2 = Button(root, text="Quit",font=('Slab Serif',15),bg='blue',fg='white', command=root.destroy).place(x=230,y=290,width=100)
button_3 = Button(root, text="Sign Up",font=('Slab Serif',15),bg='blue',fg='white',command=newUser).place(x=150,y=340,width=100)

while(True):
    for x in range(0, 60):
        canvas.move(my_img, 3, 0)
        root.update()
        time.sleep(0.1)

    for x in range(0, 60):
        canvas.move(my_img, -3, 0)
        root.update()
        time.sleep(0.1)