import tkinter as tk

# Creat the main window
window = tk.Tk()
window.title("Checkbutton Example")
window.geometry("300x150") #Width x Height

# create a variable  to store the state of the checkbutton
check_var = tk.IntVar() 

# function to display the checkbutton state
def show_state():
    if check_var.get() == 1:
        label.config(text="Checkbutton is checked")
    else:
        label.config(text="Checkbutton is unchecked")

# Create a Checkbutton
check_button = tk.Checkbutton(window, text="Click me", variable=check_var, command=show_state)
check_button.pack(pady=20)

# Label to show the current state
label = tk.Label(window, text="Checkbutton is unchecked")
label.pack()

# Run the main event loop
window.mainloop()