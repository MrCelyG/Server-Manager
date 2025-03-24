import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes

root = tk.Tk()
root.title("Server Manager")
root.geometry('500x300')

theme = [
    "adapta", 
    "aquativo",
    "arc",
    "black",
    "blue",
    "breeze",
    "clearlooks",
    "elegance",
    "equilux",
    "itft1",
    "keramik",
    "kroc",
    "plastik",
    "radiance",
    "smog",
    "winxpblue",
    "yaru"
    ]

style = ThemedStyle(root)
style.set_theme(theme[16])

# Create widgets using ttk for styling
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

menubar = tk.Menu(root)

fileMenu = tk.Menu(menubar, tearoff=0)
fileMenu.add_command(label="New...")
fileMenu.add_command(label="Open...")
fileMenu.add_command(label="Exit")
fileMenu.add_separator()
fileMenu.add_command(label="Settings")

serverMenu = tk.Menu(menubar, tearoff=0)
serverMenu.add_command(label="New...")
serverMenu.add_command(label="Initialize...")
serverMenu.add_command(label="Configure...")

controlPanelMenu = tk.Menu(menubar, tearoff=0)
controlPanelMenu.add_command(label="New...")
controlPanelMenu.add_command(label="Open...")

menubar.add_cascade(menu=fileMenu, label="File")
menubar.add_cascade(menu=serverMenu, label="Server")
menubar.add_cascade(menu=controlPanelMenu, label="Control Panel")

root.config(menu=menubar)

systemonitor = ttk.Button(root, text="System Monitor")
systemonitor.place(x=15, y=15)

root.mainloop()
