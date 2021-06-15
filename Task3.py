from tkinter import *
from tkinter import ttk

#Create object
frame = Tk()

#Declaring Window Title
frame.title("Registration Screen")

#Declaring Window size
frame.geometry('300x300')

#Declaring Window Color
frame.configure(background = "cyan")

#below four fields are declared
Firstname = Label(frame ,text = "First Name",width=15,font=("bold",18)).grid(row = 0,column = 0)
LastName = Label(frame ,text = "Last Name",width=15,font=("bold",18)).grid(row = 1,column = 0)
Email = Label(frame,text = "Email Id",width=15,font=("bold",18)).grid(row = 2,column = 0)
Mobile = Label(frame,text = "Contact Number",width=15,font=("bold",18)).grid(row = 3,column = 0)
Address = Label(frame,text = "Address",width=15,font=("bold",18)).grid(row = 4,column = 0)
Country = Label(frame,text = "Country",width=15,font=("bold",18)).grid(row = 5,column = 0)
Pincode= Label(frame,text = "Pincode",width=15,font=("bold",18)).grid(row = 6,column = 0)

#List of country
list_of_country=['India','UK','US','China','Japan']

#Dropdown menu
a=StringVar()
dropdown = OptionMenu(frame,a,*list_of_country)
dropdown.config(width=18)
a.set('Select Country')
dropdown.grid(row = 5,column = 1)

Gender =Label(frame ,text = "Gender",width=15,font=("bold", 18)).grid(row = 9,column = 0)
Emp_id = Label(frame ,text = "Emp id",width=15,font=("bold", 18)).grid(row = 8,column = 0)
var=IntVar()
Radiobutton(frame, text="Male",padx = 20, variable=var, value=1).grid(row = 9,column = 1)
Radiobutton(frame, text="Female",padx = 20, variable=var, value=2).grid(row = 9,column = 2)
Choose =Label(frame ,text = "Date of Birth",width=15,font=("bold", 18)).grid(row = 11,column = 0)
var=IntVar()
L2 = Label(frame, text="Language known",width=15,font=("bold", 18))
L2.grid(row = 10,column = 0)
var = IntVar()
Checkbutton(frame, text="java", variable=var).grid(row = 10,column = 1)
var = IntVar()
Checkbutton(frame, text="python", variable=var).grid(row = 10,column = 2)

Firstname1 = Entry(frame).grid(row = 0,column = 1)
Lastname1 = Entry(frame).grid(row = 1,column = 1)
Email1 = Entry(frame).grid(row = 2,column = 1)
Mobile = Entry(frame).grid(row = 3,column = 1)
Country = Entry(frame).grid(row = 4,column = 1)
Pincode = Entry(frame).grid(row = 6,column = 1)
Employee_id = Entry(frame).grid(row = 8,column = 1)
DateofBirth = Entry(frame).grid(row = 11,column = 1)


#fubction declaration
def clicked():
    frame= "Welcome" + txt.get()
L2.configure(text= frame)
Button(frame, text="Submit", command=clicked,width=15).grid(row = 14,column = 3)
frame.mainloop()
