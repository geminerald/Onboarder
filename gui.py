import tkinter as tk
from tkinter.constants import END
from tkinter.filedialog import askopenfilename, asksaveasfilename
import win32com.client as client
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from datetime import datetime
import threading

def send_mail():
    outlook = client.Dispatch("Outlook.Application")
    message = outlook.CreateItem(0)
    message.Display()
    message.To = email_entry.get()
    message.CC = manager_entry.get()
    message.Subject = subject_entry.get()
    message.Body = text_entry.get(0.0, END)
    


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

# cal = Calendar(row_one, font="Arial 14", selectmode='day',ursor="hand1", year=2018, month=2, day=5)
    
# def print_sel():
#         print(cal.selection_get())

# cal.pack(fill="both", expand=True)
# ttk.Button(row_one, text="ok", command=print_sel).pack()


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

def delaysending():
    now = datetime.now()
    from datetime import timedelta
    run_at = now + timedelta(minutes=3)
    delay = (run_at - now).total_seconds()
    threading.Timer(delay, send_mail).start()

btn_sendmail = tk.Button(master=row_two, text="Send", command=delaysending)

btn_sendmail.pack()

window.mainloop()