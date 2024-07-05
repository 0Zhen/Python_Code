import os
import tkinter as tk
import subprocess
from tkinter import filedialog
import webbrowser
# pyinstaller --onefile A_PLUS.py
def open_test_robot():
    file_paths = filedialog.askopenfilenames()
    global filename

    for filename_TEMP in file_paths:
        basename = os.path.basename(filename_TEMP)
        filename = filename_TEMP
    global robot_name
    robot_name = ''.join(basename)
    label.config(text=robot_name)

def run_command():

    # Create a subprocess to execute the command
    command = "robot -d results"
    report_name = "--reporttitle"
    log_name = "--logtitle"
    subprocess.run(command+" "+report_name+" "+robot_name+" "+log_name+" "+robot_name+" "+filename, shell=True, check=True)



def open_file():
    filename = os.path.join("./results", "report.html")
    #"D:\SSB\development\robot-scripts\project1\Results\report.html"
    try:
        webbrowser.open_new_tab(filename)
    except Exception as e:
        print(f"Error opening file: {e}")

# Create the main window
root = tk.Tk()
root.title("A_PLUS")
root.geometry("250x200")

x_width = 2
y_width = 2

# Create the button to execute the command
input_file_button = tk.Button(root, text="Choose robot file", command=open_test_robot)
input_file_button.pack(pady=10)

label = tk.Label(root,text='')
label.pack(pady=10)

run_button = tk.Button(root, text="Run robot file", command=run_command)
run_button.pack(pady=10)

open_button = tk.Button(root, text="Open Result", command=open_file)
open_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()