from tkinter import filedialog
import tkinter as tk
import os

def CreateServer():

    ServerTk = tk.Tk()
    ServerTk.title("Enter Folder Name")
    ServerTk.geometry("200x150")
    NameVariable = tk.StringVar()

    ServerTk.withdraw()

    def Submit():
        Name = NameVariable.get()
        Directory = filedialog.askdirectory()

        Path = os.path.join(Directory, Name)
        os.makedirs(Path)
        ServerTk.deiconify()

        OkTk = tk.Toplevel(ServerTk)
        OkTk.title("Server Created Sucessfully Created Sucessfully!")

        OkLabel = tk.Label(OkTk, text="Folder Created Sucessfully!")

    FolderEntry = tk.Entry(ServerTk, relief="sunken", textvariable= NameVariable)
    FolderButton = tk.Button(ServerTk, text= "Submit", command= Submit)

    FolderEntry.place(x=15, y=50)
    FolderButton.place(x=65, y=100)

    ServerTk.deiconify()
    ServerTk.mainloop()

CreateServer()