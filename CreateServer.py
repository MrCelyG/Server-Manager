from tkinter import messagebox, filedialog
import tkinter as tk
import json
import os

def CheckIfUserTips():
    """Checks if the user wants tips and shows the first server tip if needed."""
    try:
        with open('userSettings.json', 'r') as JsonSettings:
            SettingsLoaded = json.load(JsonSettings)
            tipsDictionary = SettingsLoaded.get('HOW_TO_TIPS', {})

        if not tipsDictionary.get('FirstServer', False) and SettingsLoaded.get("USER_WANT_HELP", False):
            messagebox.askokcancel("How to make a server", 
                                   "To make a server, choose a name and directory. Then it will be created.")

            # Update the settings file to mark the tip as shown
            tipsDictionary['FirstServer'] = True
            SettingsLoaded['HOW_TO_TIPS'] = tipsDictionary
            with open('userSettings.json', 'w') as JsonSettings:
                json.dump(SettingsLoaded, JsonSettings, indent=2)

    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Could not read settings. Ensure 'userSettings.json' exists and is valid.")

CreateServerWindow = tk.Tk()
CreateServerWindow.title("Server Creation Menu")
CreateServerWindow.geometry('300x200')

DirectoryLabel = tk.Label(CreateServerWindow, text="Choose Directory")
DirectoryLabel.place(x=95, y=15)

def AskDirectory():
    """Asks the user for a directory and prompts for a server name."""
    CreateServerWindow.withdraw()
    Directory = filedialog.askdirectory()
    
    if not Directory:
        CreateServerWindow.deiconify()
        return  # User canceled the selection

    print(f'Selected directory: {Directory}')

    def JoinAndCreateFolder():
        """Creates a folder with the chosen name inside the selected directory."""
        FolderName = entry.get().strip()
        if not FolderName:
            messagebox.showerror("Error", "Server name cannot be empty!")
            return

        DirectoryValue = os.path.join(Directory, FolderName)
        try:
            os.mkdir(DirectoryValue)
            messagebox.showinfo("Success", f"Server folder '{FolderName}' created successfully!")
        except FileExistsError:
            messagebox.showerror("Error", "A folder with this name already exists!")
        except OSError as e:
            messagebox.showerror("Error", f"Failed to create folder: {e}")

        ChooseNameWindow.destroy()
        CreateServerWindow.deiconify()

    ChooseNameWindow = tk.Toplevel(CreateServerWindow)
    ChooseNameWindow.geometry('300x100')
    ChooseNameWindow.title('Enter Server Name')

    entry = tk.Entry(ChooseNameWindow)
    entry.place(x=60, y=15)

    SubmitButton = tk.Button(ChooseNameWindow, text="Submit", command=JoinAndCreateFolder)
    SubmitButton.place(x=100, y=50)

DirectoryButton = tk.Button(CreateServerWindow, text="Directory...", command=AskDirectory)
DirectoryButton.place(x=105, y=45)

CreateServerWindow.withdraw()

def RunServerCreation():
    """Runs the server creation process by checking for tips and showing the window."""
    CheckIfUserTips()
    CreateServerWindow.deiconify()
