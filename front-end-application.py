from tkinter import *
import sqlite3
from tkinter import messagebox


connection = sqlite3.connect("example.db")
cursor = connection.cursor()
top = Tk()  
top.geometry("850x600")


def course():
    top4=Toplevel(top)
    top4.geometry("850x500")

    def my_delete1(id):
        my_var=messagebox.askyesnocancel("Delete ?","Delete id:"+str(id),icon='warning',default='no')
        if my_var: # True if yes button is clicked
            r_set=connection.execute("DELETE FROM course WHERE course_id=" + str(id) );
            messagebox.showerror("Deleted ","No of records deleted = " + str(r_set.rowcount))
            connection.commit()
            data2()


    def data2():
        top5=Toplevel(top)
        top5.geometry("850x500")
        connection.execute("SELECT * FROM course")
        i=0

        for std in connection.execute("SELECT * FROM course"):
            for j in range(len(std)):
                e = Entry(top5, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, std[j])
            i=i+1
            e = Button(top5, text='Delete',command=lambda d=std[0] : my_delete1(d)) 
            e.grid(row=i-1, column=j+1)

    
    def Insert2():

        
        


        

        cursor.execute("INSERT INTO course Values(?,?,?)",(entryNum7.get(),entryNum8.get(),entryNum9.get()))
        connection.commit()
        cursor.close()
        #cursor.execute(sql,val)
        
       
        messagebox.showinfo("Inserting Data", "Data Inserted Successfully")  
        print("Alhumdulillah")


    
    label7 = Label(top4, text = "Course Table",font=("Arial", 25)).place(x = 140,y = 20) 
    label8 = Label(top4, text = "course_id",font=("Arial", 10)).place(x = 20,y = 100) 
    label9 = Label(top4, text = "semester",font=("Arial", 10)).place(x = 20,y = 140) 
    label10 = Label(top4, text = "course_title",font=("Arial", 10)).place(x = 20,y = 180)
    global entryNum7
    global entryNum8
    global entryNum9

    number7 = IntVar()
    number8= IntVar()
    number9 =StringVar()

    entryNum7 = Entry(top4, textvariable=number7)
    entryNum7.place(x = 200,y = 100) 
    entryNum8= Entry(top4, textvariable=number8)
    entryNum8.place(x = 200,y = 140)
    entryNum9= Entry(top4, textvariable=number9)
    entryNum9.place(x = 200,y = 180)
    button5 = Button(top4, text = "Insert", fg = "black",font=("Arial", 15),command= Insert2)
    button5.place(x =300,y = 400)
    button6 = Button(top4, text = "Show data", fg = "black",font=("Arial", 15),command= data2)
    button6.place(x =300,y = 450)
    
    


def student():
 
    top1=Toplevel(top)
    top1.geometry("850x500")

    def my_delete(id):
        my_var=messagebox.askyesnocancel("Delete ?","Delete id:"+str(id),icon='warning',default='no')
        if my_var: # True if yes button is clicked
            r_set=connection.execute("DELETE FROM student WHERE student_id=" + str(id) );
            messagebox.showerror("Deleted ","No of records deleted = " + str(r_set.rowcount))
            connection.commit()
            data() 
    def data():
        top3=Toplevel(top1)
        top3.geometry("850x500")
        connection.execute("SELECT * FROM student")
        i=0

        for std in connection.execute("SELECT * FROM student"):
            for j in range(len(std)):
                e = Entry(top3, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, std[j])
            i=i+1
            e = Button(top3, text='Delete',command=lambda d=std[0] : my_delete(d)) 
            e.grid(row=i-1, column=j+1)
# refresh the window with new records

 
        


    
    def Insert1():

        print(entryNum1.get())
        
        


        

        cursor.execute("INSERT INTO Student Values(?,?,?,?,?,?)",(entryNum1.get(),entryNum2.get(),entryNum3.get(),entryNum4.get(),entryNum5.get(),entryNum6.get()))
        connection.commit()
        #cursor.close()
        #cursor.execute(sql,val)
        
       
        messagebox.showinfo("Inserting Data", "Data Inserted Successfully")  
        print("Alhumdulillah")

        
    global entryNum1
    global entryNum2
    global entryNum3
    global entryNum4
    global entryNum5
    global entryNum6
    
    
    number1 = IntVar()
    number2= StringVar()
    number3 =StringVar()
    number4 =IntVar()
    number5 =IntVar()
    number6 =IntVar()
    
    
    label1 = Label(top1, text = "Student Table",font=("Arial", 25)).place(x = 140,y = 20) 
    label2 = Label(top1, text = "Student_id",font=("Arial", 10)).place(x = 20,y = 100) 
    label3 = Label(top1, text = "student_name",font=("Arial", 10)).place(x = 20,y = 140) 
    label4 = Label(top1, text = "student_address",font=("Arial", 10)).place(x = 20,y = 180) 
    label5 = Label(top1, text = "student_contact",font=("Arial", 10)).place(x = 20,y = 220)
    label6 = Label(top1, text = "dept_no",font=("Arial", 10)).place(x = 20,y = 260)
    label7 = Label(top1, text = "semester",font=("Arial", 10)).place(x = 20,y = 300)
    entryNum1 = Entry(top1, textvariable=number1)
    entryNum1.place(x = 200,y = 100) 
    entryNum2= Entry(top1, textvariable=number2)
    entryNum2.place(x = 200,y = 140)
    entryNum3= Entry(top1, textvariable=number3)
    entryNum3.place(x = 200,y = 180)
    entryNum4= Entry(top1, textvariable=number4)
    entryNum4.place(x = 200,y = 220)
    entryNum5= Entry(top1, textvariable=number5)
    entryNum5.place(x = 200,y = 260)
    entryNum6= Entry(top1, textvariable=number6)
    entryNum6.place(x = 200,y = 300)
    button2 = Button(top1, text = "Insert", fg = "black",font=("Arial", 15),command= Insert1)
    button2.place(x =300,y = 400)
    button3 = Button(top1, text = "Show data", fg = "black",font=("Arial", 15),command= data)
    button3.place(x =300,y = 450)
                     
                      
    
    

    #print(b)





label = Label(top, text = "Select table for Insertion & deletion",font=("Arial", 25)).place(x = 140,y = 60) 

redbutton = Button(top, text = "Student", fg = "black",font=("Arial", 15),command=student)  
redbutton.place(x =340,y = 160)   
greenbutton = Button(top, text = "Department", fg = "black",font=("Arial", 15))  
greenbutton.place(x = 340,y = 240)   
bluebutton = Button(top, text = "Professor", fg = "blue",font=("Arial", 15))  
bluebutton.place(x = 340,y = 320)   
blackbutton = Button(top, text = "Course", fg = "red",font=("Arial", 15),command=course)  
blackbutton.place(x = 340,y = 400)    
top.mainloop() 
