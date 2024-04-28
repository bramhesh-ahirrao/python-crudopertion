import tkinter as tk
import messagebox as MessageBox
import mysql.connector as mysql
r = tk.Tk()
r.geometry("800x900")
heading = tk.Label(r, text="Registration Form", font="Arial 50 bold")
heading.place(x=80, y=10)


def details():
    i = Id_entry.get()
    n = name_entry.get()
    e = email_entry.get()
    p = password_entry.get()
    m = mob_entry.get()
    g = q.get()

    if i == "" or n == "" or e == "" or p == "" or m == "" or g == "":
        MessageBox.showinfo("Alert", "Please Enter All Fields")
    else:
        conn = mysql.connect(host="localhost", user="root", password="R3vfy@74011", database="myb",auth_plugin="mysql_native_password")
        cursor = conn.cursor()
        cursor.execute("insert into stud values('"+i+"','"+n+"','"+e+"','"+p+"','"+m+"','"+g+"')")
        cursor.execute("commit")
        MessageBox.showinfo("status", "Record inserted successfully")
        conn.close()
        r.destroy()


def select():
    i = Id_entry.get()
    n = name_entry.get()
    e = email_entry.get()
    p = password_entry.get()
    m = mob_entry.get()
    g = q.get()

    conn = mysql.connect(host="localhost", user="root", password="R3vfy@74011", database="myb",auth_plugin="mysql_native_password")
    cursor = conn.cursor()
    cursor.execute("select * from stud where Id = '"+Id_entry.get()+"'")

    t = cursor.fetchall()
    for y in t:
        name_entry.insert(0, y[1])
        email_entry.insert(0, y[2])
        password_entry.insert(0, y[3])
        mob_entry.insert(0, y[4])
        q.insert(0, y[5])

    conn.close()


def edit():
    i = Id_entry.get()
    n = name_entry.get()
    e = email_entry.get()
    p = password_entry.get()
    m = mob_entry.get()
    g = q.get()

    if i == "" or n == "" or e == "" or p == "" or m == "" or g == "":
        MessageBox.showinfo("Alert", "Please Enter All Fields")
    else:
        conn = mysql.connect(host="localhost", user="root", password="R3vfy@74011", database="myb",auth_plugin="mysql_native_password")
        cursor = conn.cursor()
        cursor.execute("update stud set name='"+n+"', email='"+e+"', password='"+p+"', mob='"+m+"', q='"+g+"' where Id='"+i+"'")
        cursor.execute("commit")
        MessageBox.showinfo("status", "Record updated successfully")
        conn.close()
        r.destroy()


def delete():
    if Id_entry.get() == "":
        MessageBox.showinfo("Alert", "Please enter all feilds")
    else:
        conn = mysql.connect(host="localhost", user="root", password="R3vfy@74011", database="myb",auth_plugin="mysql_native_password")
        cursor = conn.cursor()
        cursor.execute("delete from stud where Id = '"+Id_entry.get()+"'")
        cursor.execute("commit")

        Id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        mob_entry.delete(0, 'end')

        MessageBox.showinfo("status", "Record deleted Successfully")
        conn.close()
        r.destroy()


Id = tk.Label(r, text="Enter Id", font="Arial 20 bold")
Id.place(x=80, y=150)

name = tk.Label(r, text="Enter your name", font="Arial 20 bold")
name.place(x=80, y=200)

email = tk.Label(r, text="Enter your email", font="Arial 20 bold")
email.place(x=80, y=245)

password = tk.Label(r, text="Enter password", font="Arial 20 bold")
password.place(x=80, y=300)

mob = tk.Label(r, text="Contact Number", font="Arial 20 bold")
mob.place(x=80, y=350)

Id_entry = tk.Entry(width=60)
Id_entry.place(x=320, y=155)

name_entry = tk.Entry(width=60)
name_entry.place(x=320, y=205)

email_entry = tk.Entry(width=60)
email_entry.place(x=320, y=250)

password_entry = tk.Entry(width=60)
password_entry.place(x=320, y=305)

mob_entry = tk.Entry(width=60)
mob_entry.place(x=320, y=355)

gender = tk.Label(r, text="Select gender", font="Arial 20 bold")
gender.place(x=80, y=400)

q = tk.StringVar()
q.set(None)

male = tk.Radiobutton(text="Male", value="Male", variable=q)
male.place(x=350, y=400)

female = tk.Radiobutton(text="Female", value="Female", variable=q)
female.place(x=400, y=400)

btn = tk.Button(r, text="Submit", fg="white", bg="blue", width="10", command=details)
btn.place(x=200, y=450)

show = tk.Button(r, text="Show", fg="white", bg="blue", width="10", command=select)
show.place(x=300, y=450)

update = tk.Button(r, text="Update", fg="white", bg="blue", width="10", command=edit)
update.place(x=400, y=450)

clear = tk.Button(r, text="Delete", fg="white", bg="blue", width="10", command=delete)
clear.place(x=500, y=450)
r.mainloop()