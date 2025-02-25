import tkinter as tk
import pathlib
import json

root = tk.Tk()
root.title("Control Panel")
root.geometry('500x300')

rootMenubar = tk.Menu(root)

# Creating User Settings If Not Found And Dumping Settings And Stuff.
SettingsPath = pathlib.Path('userSettings.json')

def SettingsDumpJson():
    from Core import startupVariables as SVP
    print('Creating User Settings')
    with open("userSettings.json", "w") as FileToBeDumped:
        json.dump(SVP.Setting_Vars, FileToBeDumped, indent=1)


if SettingsPath.exists():
    print("Settings Exsist.")
else:
    SettingsDumpJson()
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
