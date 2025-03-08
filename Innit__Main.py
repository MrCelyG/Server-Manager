import tkinter as tk
from tkinter import messagebox
import pathlib
import json
import CreateServer as CS

# Initialize the main application window
app = tk.Tk()
app.title("Control Panel")
app.geometry('500x300')

# Define the path for user settings
settings_file_path = pathlib.Path('userSettings.json')

# Function to create user settings file if not found
def create_user_settings():
    try:
        print('Creating userSettings.json file.')
        from Core import startupVariables as svp  # Import startup variables
        
        with open(settings_file_path, "w") as settings_file:
            json.dump(svp.Setting_Vars, settings_file, indent=1)
    
    except Exception as error:
        print(f"Error in create_user_settings: {error}")

# Function to prompt user for tips
def prompt_user_tips():
    try:
        user_response = messagebox.askyesno("Receive Tips?", "Receive tips on how to use (Can be turned off in settings)")

        # Load settings
        with open(settings_file_path, 'r') as settings_file:
            settings_data = json.load(settings_file)

        # Update settings based on user response
        settings_data["FIRST_TIME_COMPLETE"] = True if user_response else False
        if not user_response:
            settings_data['USER_WANT_HELP'] = False
            settings_data['FIRST_TIME_COMPLETE'] = True
        else:
            settings_data['USER_WANT_HELP'] = True
            settings_data['FIRST_TIME_COMPLETE'] = True
            
        # Save updated settings
        with open(settings_file_path, 'w') as settings_file:
            json.dump(settings_data, settings_file, indent=1)

    except Exception as error:
        print(f"Error in prompt_user_tips: {error}")

# Check if the settings file exists; create if it doesn’t
if not settings_file_path.exists():
    print("Settings file does not exist. Creating it.")
    create_user_settings()

# Function to check if user wants tips
def check_user_tips_preference():
    try:
        with open(settings_file_path, 'r') as settings_file:
            settings_data = json.load(settings_file)
        
        if not settings_data.get('FIRST_TIME_COMPLETE', False):
            prompt_user_tips()
    
    except Exception as error:
        print(f"Error in check_user_tips_preference: {error}")

# Call function to check user's preference for tips
check_user_tips_preference()

# Create menu bar
main_menu = tk.Menu(app)

server_menu = tk.Menu(main_menu, tearoff=0)
server_menu.add_command(label="New Server", command=CS.RunServerCreation)
server_menu.add_command(label="Website...")
server_menu.add_separator()
server_menu.add_command(label="About")
server_menu.add_command(label="Settings")
main_menu.add_cascade(label="Server", menu=server_menu)

app.config(menu=main_menu)

# Run Tkinter event loop
app.mainloop()
