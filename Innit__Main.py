import tkinter as tk
from Core import startupVariables as SVP

root = tk.Tk()
root.title("Control Panel")
root.geometry('500x300')

rootMenubar = tk.Menu(root)

# Create Menu
ServerMenu = tk.Menu(rootMenubar, tearoff=0)
ServerMenu.add_command(label="New Server")
ServerMenu.add_command(label="Website...")
ServerMenu.add_separator()
ServerMenu.add_command(label="About")
ServerMenu.add_command(label="Settings")
rootMenubar.add_cascade(label="Server", menu=ServerMenu)

root.config(menu=rootMenubar)
root.mainloop()
