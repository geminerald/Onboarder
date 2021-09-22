import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import win32com.client as client

def send_mail():
    outlook = client.Dispatch("Outlook.Application")
    message = outlook.CreateItem(0)
    message.Display()
    message.To = email_entry.get()
    message.CC = manager_entry.get()
    message.Subject = subject_entry.get()
    message.Body = text_entry.get()


window = tk.Tk()
window.title("Onboarder")

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

text_entry.pack()
text_label.pack()

subject_entry.pack()
subject_label.pack()

manager_label.pack()
manager_entry.pack()

email_label.pack()
email_entry.pack()

name_label.pack()
name_entry.pack()

btn_sendmail = tk.Button(master=row_two, text="Send", command=send_mail)

btn_sendmail.pack()

window.mainloop()