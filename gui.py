import tkinter as tk
from tkinter.constants import END
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from functions import delaysending

window = tk.Tk()
window.title("Onboarder")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(0, minsize=800, weight=1)

container_frame = tk.Frame()
container_frame.pack()

row_one = tk.Frame(master=container_frame)
row_one.pack()

row_two = tk.Frame(master=container_frame)
row_two.pack()

name_label = tk.Label(master=row_one, text="Enter Name")
name_entry = tk.Entry(master=row_one)

email_label = tk.Label(master=row_one, text="Enter Email")
email_entry = tk.Entry(master=row_one)

manager_label = tk.Label(master=row_one, text="Enter Manager's Email")
manager_entry = tk.Entry(master=row_one)

subject_label = tk.Label(master=row_two, text="Enter Subject")
subject_entry = tk.Entry(master=row_two)

text_label = tk.Label(master=row_two, text="Enter Message Body")
text_entry = tk.Text(master=row_two)

subject_label.pack()
subject_entry.pack()

text_label.pack()
text_entry.pack()


manager_label.pack()
manager_entry.pack()

email_label.pack()
email_entry.pack()

name_label.pack()
name_entry.pack()

btn_sendmail = tk.Button(master=row_two, text="Send", command=delaysending)

btn_sendmail.pack()

window.mainloop()