import win32com.client as client

def send_mail(recipient, cc, subject, body):
    outlook = client.Dispatch("Outlook.Application")
    message = outlook.CreateItem(0)
    message.Display()
    message.To = recipient
    message.CC = cc
    message.Subject = subject
    message.Body = body

# onboard(first_name, last_name, reports_to, email, role, start_date, acceptance_date)