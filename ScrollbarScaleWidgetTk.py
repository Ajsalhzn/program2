import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Scrollbar and Scale Example")
root.geometry("300x300")

# ---------- Scrollbar with Listbox ----------

# Create a frame
frame = tk.Frame(root)
frame.pack(pady=10)

# Create Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create Listbox
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=6)
listbox.pack(side=tk.LEFT)

# Configure scrollbar
scrollbar.config(command=listbox.yview)

# Add items to Listbox
for i in range(1, 21):
    listbox.insert(tk.END, f"Item {i}")

# ---------- Scale Widget ----------

# Create Scale
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack(pady=20)

# Run the application
root.mainloop()
