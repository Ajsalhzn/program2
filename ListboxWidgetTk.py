import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Fruit Listbox")

# Set window size
root.geometry("300x250")

# Create Listbox widget with size
listbox = tk.Listbox(root)

# List of fruits
fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple"]

# Insert fruits into the Listbox
for fruit in fruits:
    listbox.insert(tk.END, fruit)

# Display the Listbox
listbox.pack(pady=20)

# Run the application
root.mainloop()
