import os
import tkinter as tk
from tkinter import filedialog
from ttkthemes import themed_tk
import ttkbootstrap as ttk

def edit_files(folder_path: str, insert_before: str, insert_after: str) -> None:
    """Edit text files in a given folder by inserting text before and after the content.

    Args:
        folder_path (str): The path of the folder containing the text files.
        insert_before (str): The text to insert before the content of each file.
        insert_after (str): The text to insert after the content of each file.

    Returns:
        None
    """
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r+") as f:
                content = f.read()
                f.seek(0, 0)
                f.write(insert_before + content + insert_after)

def browse_folder() -> None:
    """Browse a folder and update an entry widget with its path.

    Returns:
        None
    """
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END) 
    folder_path_entry.insert(0, folder_path)

def run_script() -> None:
    """Run the script using user inputs from entry widgets."""
    folder_path = folder_path_entry.get()
    insert_before = insert_before_entry.get()
    insert_after = insert_after_entry.get()
    edit_files(folder_path, insert_before, insert_after)

root = themed_tk.ThemedTk()
root.title("Text File Editor")
root.style = ttk.Style()
root.style.theme_use("superhero")

folder_path_label = ttk.Label(root, text="Folder Path:")
folder_path_label.pack(padx=26,pady=16)

folder_path_entry = ttk.Entry(root)
folder_path_entry.pack(padx=26,pady=6)

browse_button = ttk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(padx=26,pady=6)

insert_before_label = ttk.Label(root, text="Insert Before:")
insert_before_label.pack(padx=26,pady=6)

insert_before_entry = ttk.Entry(root)
insert_before_entry.pack(padx=26,pady=6)

insert_after_label = ttk.Label(root, text="Insert After:")
insert_after_label.pack(padx=26,pady=6)

insert_after_entry = ttk.Entry(root)
insert_after_entry.pack(padx=26,pady=6)

run_button = ttk.Button(root, text="Run", command=run_script)
run_button.pack(padx=26,pady=32)

root.mainloop()