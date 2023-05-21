import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog





class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PANNO!")
        self.text = tk.Text(root)
        self.text.pack(fill=tk.BOTH, expand=True)
        self.undo_stack = []
        self.redo_stack = []
        self.bind_keyboard_shortcuts()
        self.current_file = None  # Variable to store the current file name

        # Create the menu bar
        menu_bar = tk.Menu(root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.load_file)
        file_menu.add_command(label="Save", command=self.save_file)
        menu_bar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menu_bar)

        # Create the toolbar
        toolbar = tk.Frame(root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        load_button = tk.Button(toolbar, text="Load", command=self.load_file)
        load_button.pack(side=tk.LEFT)

        save_button = tk.Button(toolbar, text="Save", command=self.save_file)
        save_button.pack(side=tk.LEFT)

        redo_button = tk.Button(toolbar, text="Redo", command=self.redo)
        redo_button.pack(side=tk.LEFT)

        

    def bind_keyboard_shortcuts(self):
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-z>", self.undo)
        self.root.bind("<Control-y>", self.redo)

    def load_file(self, event=None):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.text.delete("1.0", tk.END)
                    self.text.insert(tk.END, file.read())
                    self.current_file = file_path  # Update the current file name
                    self.update_title()  # Update the title
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def save_file(self, event=None):
        if self.current_file:
            try:
                with open(self.current_file, "w") as file:
                    file.write(self.text.get("1.0", tk.END))
                    messagebox.showinfo("Save", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_path:
                try:
                    with open(file_path, "w") as file:
                        file.write(self.text.get("1.0", tk.END))
                        self.current_file = file_path  # Update the current file name
                        self.update_title()  # Update the title
                        messagebox.showinfo("Save", "File saved successfully.")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def undo(self, event=None):
        if self.undo_stack:
            text = self.undo_stack.pop()
            self.redo_stack.append(self.text.get("1.0", tk.END))
            self.text.delete("1.0",)
            self.text.insert(tk.END, text)

    def redo(self, event=None):
        if self.redo_stack:
            text = self.redo_stack.pop()
            self.undo_stack.append(self.text.get("1.0", tk.END))
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, text)


    

    def update_title(self):
        if self.current_file:
            self.root.title(f"Text Editor - {self.current_file}")
        else:
            self.root.title("Text Editor")





if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()

