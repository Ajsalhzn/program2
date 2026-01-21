import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry_name.get()
    email = entry_email.get()
    message = entry_message.get()

    if name == "" or email == "" or message == "":
        messagebox.showwarning("Warning", "All fields are required")
    else:
        messagebox.showinfo("Success", "Form submitted successfully")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_message.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Contact Form")
root.geometry("400x300")

# Name
tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack()

# Email
tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.pack()

# Message
tk.Label(root, text="Message:").pack(pady=5)
entry_message = tk.Entry(root, width=40)
entry_message.pack()

# Submit button
tk.Button(root, text="Submit", command=submit).pack(pady=15)

# Run the application
root.mainloop()
