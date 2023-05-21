import tkinter as tk
from tkinter import filedialog
import os
def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        listbox.delete(0, tk.END)  # Clear the listbox
        files = os.listdir(folder_path)
        for file_name in files:
            listbox.insert(tk.END, file_name)

root = tk.Tk()
root.title("File Explorer")

# Create a listbox to display the files
listbox = tk.Listbox(root, width=50)
listbox.pack(padx=10, pady=10)

# Create a button to browse the folder
browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(pady=10)

root.mainloop()
