import tkinter as tk
from Python.ManageFeatures import CreateServer

Main = tk.Tk()

# Properties of main
Main.title("Main Control Panel")
Main.geometry("500x300")
Main.resizable(False, False)

# Create Menubar
menubar = tk.Menu(Main)

Server = tk.Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "Server", menu= Server)

Server.add_command(label= "Create Folder", command= CreateServer.CreateFolder)
Server.add_command(label= "Manage Server")
Server.add_command(label= "Start Server")

Main.config(menu = menubar)
Main.mainloop()

