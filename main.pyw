import tkinter as tk
import os
from tkinter import filedialog
import time


# Asks for a directory and makes a list of all the txt files in that directory
current_file_path = filedialog.askdirectory()
txt_files = []
os.chdir(current_file_path)
for i in os.listdir():
    temp = i.split('.')
    if(temp[len(temp) -1] == "txt"):
        txt_files.append(i)
num = 0

# If there are no txt files it makes a new temp.txt file
if(len(txt_files) == 0):
    open(current_file_path + "temp.txt","w")

# Opens a file using file dialog
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            window.title(file_path.split('/')[-1][:-4])
            content = file.read()
            text_editor.delete("1.0", tk.END)
            text_editor.insert(tk.END, content)

# Opens a file using a file path      
def open_file_path(file_path):
    #file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            window.title(file_path[:-4])
            content = file.read()
            text_editor.delete("1.0", tk.END)
            text_editor.insert(tk.END, content)

# Function to open a file dialogue to save the notes
def save_file():
    global txt_files,num
    file_path = txt_files[num]
    #file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    if file_path:
        with open(file_path, "w") as file:
            content = text_editor.get("1.0", tk.END)
            file.write(content)
    window.title("Saving")
    time.sleep(0.5)
    window.title("Saved")
    time.sleep(0.5)
    window.title(file_path.split('/')[-1][:-4])

# Function to open next file (>>)
def open_next_file():
    global num, txt_files
    if num == len(txt_files) - 1:
        num = 0
    else:
        num += 1
    open_file_path(txt_files[num])

# Function to select previous file (<<)
def open_previous_file():
    global num, txt_files
    if num == 0:
        num = len(txt_files) -1
    else:
        num -= 1
    open_file_path(txt_files[num])


# Create the main window
window = tk.Tk()
window.title("Switchit |" + txt_files[0][:-4])
window.geometry("400x300")
window.iconbitmap("main2.ico")

# Create a menu bar
menu_bar = tk.Menu(window)
menu_bar.add_command(label = "<<", command = open_previous_file)
menu_bar.add_command(label = "Save", command = save_file)
menu_bar.add_command(label = "Quit", command = window.quit)
menu_bar.add_command(label = "Open", command = open_file)
menu_bar.add_command(label = ">>", command = open_next_file)


window.config(menu=menu_bar)

# Create a text editor
text_editor = tk.Text(window,font=("times new roman",16), background="#ffff4d" )
text_editor.pack(fill=tk.BOTH, expand=True)
open_file_path(txt_files[0])

# Run the main loop
window.mainloop()
