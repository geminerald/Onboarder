
from datetime import datetime
import threading
import win32com.client as client
import gui
from tkinter import END



# cal = Calendar(row_one, font="Arial 14", selectmode='day',ursor="hand1", year=2018, month=2, day=5)
    
# def print_sel():
#         print(cal.selection_get())

# cal.pack(fill="both", expand=True)
# ttk.Button(row_one, text="ok", command=print_sel).pack()


def test():
    print("Hello, testing")

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

def send_mail():
    outlook = client.Dispatch("Outlook.Application")
    message = outlook.CreateItem(0)
    message.Display()
    message.To = gui.email_entry.get()
    message.CC = gui.manager_entry.get()
    message.Subject = gui.subject_entry.get()
    message.Body = gui.text_entry.get(0.0, END)

def delaysending():
    now = datetime.now()
    from datetime import timedelta
    run_at = now + timedelta(minutes=1)
    delay = (run_at - now).total_seconds()
    threading.Timer(delay, send_mail).start()
