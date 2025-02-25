import tkinter as tk
from tkinter import messagebox
import pathlib
import json

root = tk.Tk()
root.title("Control Panel")
root.geometry('500x300')

rootMenubar = tk.Menu(root)

# Creating User Settings If Not Found And Dumping Settings And Stuff.
SettingsPath = pathlib.Path('userSettings.json')

def SettingsDumpJson():
    try:
        print('Creating userSettings.json file.')
        from Core import startupVariables as SVP
        
        with open("userSettings.json", "w") as FileToBeDumped:
            json.dump(SVP.Setting_Vars, FileToBeDumped, indent=1)
    
    except Exception as e:
        print(f"Error in SettingsDumpJson: {e}")

def ShowUserTips():
    try:
        MessageBox = messagebox.askyesno("Recive Tips?", "Recive Tips On How To Use (Can Be Turned Off In Settings)")

        # Open the JSON file to read it
        with open('userSettings.json', 'r') as FileToBeLoaded:
            JsonData = json.load(FileToBeLoaded)

        # Ensure Python-style Boolean values
        JsonData["FIRST_TIME_COMPLETE"] = True if MessageBox else False
        if not MessageBox:
            JsonData['USER_WANT_HELP'] = False
            JsonData['FIRST_TIME_COMPLETE'] = True

        # Save the updated JSON data
        with open('userSettings.json', 'w') as FileToBeDumped:
            json.dump(JsonData, FileToBeDumped, indent=1)

    except Exception as e:
        print(f"Error in ShowUserTips: {e}")

# Check if the settings file exists
if SettingsPath.exists():
    print("Settings file exists.")
else:
    print("Settings file does not exist. Creating it.")
    SettingsDumpJson()

# Create Menu
ServerMenu = tk.Menu(rootMenubar, tearoff=0)
ServerMenu.add_command(label="New Server")
ServerMenu.add_command(label="Website...")
ServerMenu.add_separator()
ServerMenu.add_command(label="About")
ServerMenu.add_command(label="Settings")
rootMenubar.add_cascade(label="Server", menu=ServerMenu)

def CheckIfUserWantTips():
    try:
        with open('userSettings.json', 'r') as Flag1:
            JsonData = json.load(Flag1)
        
        # Check if FIRST_TIME_COMPLETE is False
        Bored = JsonData.get('FIRST_TIME_COMPLETE', False)
        
        if Bored == False:
            ShowUserTips()
    
    except Exception as e:
        print(f"Error in CheckIfUserWantTips: {e}")

# Calling the function to check if user wants tips
CheckIfUserWantTips()

root.config(menu=rootMenubar)

# Run Tkinter main loop
root.mainloop()
