import tkinter as tk
from tkinter import messagebox
import sqlite3
from tabulate import tabulate
import pandas as pd

# Creating database connection
myConnection = sqlite3.connect("mewar_db.db")
myCursor = myConnection.cursor()

# Creating student table
query = """
CREATE TABLE IF NOT EXISTS student (
    roll INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT,
    phone TEXT
);
"""
myCursor.execute(query)
myConnection.commit()

# Function to add a student
def add_student():
    try:
        roll = int(entry_roll.get())
        name = entry_name.get()
        age = int(entry_age.get())
        email = entry_email.get()
        phone = entry_phone.get()

        query = "INSERT INTO student VALUES (?, ?, ?, ?, ?)"
        myCursor.execute(query, (roll, name, age, email, phone))
        myConnection.commit()

        messagebox.showinfo("Success", "Student added successfully")
        clear_entries()
    except Exception as e:
        messagebox.showerror("Error", f"{e}")

# Function to view students
def view_students():
    query = "SELECT * FROM student"
    myCursor.execute(query)
    records = myCursor.fetchall()

    if records:
        result = tabulate(records, headers=["Roll", "Name", "Age", "Email", "Phone"], tablefmt="psql")
        messagebox.showinfo("Student Records", result)
    else:
        messagebox.showinfo("Info", "No student records found")

# Function to search a student
def search_student():
    try:
        roll = int(entry_roll.get())
        query = "SELECT * FROM student WHERE roll = ?"
        myCursor.execute(query, (roll,))
        record = myCursor.fetchone()

        if record:
            result = tabulate([record], headers=["Roll", "Name", "Age", "Email", "Phone"], tablefmt="psql")
            messagebox.showinfo("Student Found", result)
        else:
            messagebox.showinfo("Info", "No student found with this roll number")
    except Exception as e:
        messagebox.showerror("Error", f"{e}")

# Function to update a student
def update_student():
    try:
        roll = int(entry_roll.get())
        new_phone = entry_phone.get()

        query = "UPDATE student SET phone = ? WHERE roll = ?"
        myCursor.execute(query, (new_phone, roll))
        myConnection.commit()

        if myCursor.rowcount:
            messagebox.showinfo("Success", "Student updated successfully")
        else:
            messagebox.showinfo("Info", "No student found with this roll number")
    except Exception as e:
        messagebox.showerror("Error", f"{e}")

# Function to delete a student
def delete_student():
    try:
        roll = int(entry_roll.get())

        query = "DELETE FROM student WHERE roll = ?"
        myCursor.execute(query, (roll,))
        myConnection.commit()

        if myCursor.rowcount:
            messagebox.showinfo("Success", "Student deleted successfully")
        else:
            messagebox.showinfo("Info", "No student found with this roll number")
    except Exception as e:
        messagebox.showerror("Error", f"{e}")

# Function to clear entry fields
def clear_entries():
    entry_roll.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

# Creating the main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x400")

# Labels and Entry Widgets
lbl_roll = tk.Label(root, text="Roll Number:")
lbl_roll.pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

lbl_name = tk.Label(root, text="Name:")
lbl_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

lbl_age = tk.Label(root, text="Age:")
lbl_age.pack()
entry_age = tk.Entry(root)
entry_age.pack()

lbl_email = tk.Label(root, text="Email:")
lbl_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

lbl_phone = tk.Label(root, text="Phone:")
lbl_phone.pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

# Buttons
btn_add = tk.Button(root, text="Add Student", command=add_student)
btn_add.pack()

btn_view = tk.Button(root, text="View Students", command=view_students)
btn_view.pack()

btn_search = tk.Button(root, text="Search Student", command=search_student)
btn_search.pack()

btn_update = tk.Button(root, text="Update Student", command=update_student)
btn_update.pack()

btn_delete = tk.Button(root, text="Delete Student", command=delete_student)
btn_delete.pack()

btn_clear = tk.Button(root, text="Clear", command=clear_entries)
btn_clear.pack()

root.mainloop()
