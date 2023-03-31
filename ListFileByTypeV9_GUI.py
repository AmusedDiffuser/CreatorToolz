import os
import tkinter as tk
from tkinter import filedialog
from ttkbootstrap import Style

def list_files():
    folder_path = folder_path_entry.get()
    extensions = extensions_entry.get().split(',')
    output_file = output_file_entry.get()
    include_extension = include_extension_var.get()
    include_subfolders = include_subfolders_var.get()
    include_full_path = include_full_path_var.get()
    filters = filters_entry.get().split(',')

    style = Style(theme='darkly')
    with open(output_file, "w") as f:
        for root, dirs, files in os.walk(folder_path):
            if not include_subfolders and root != folder_path:
                continue
            for file in files:
                if file.endswith(tuple(extensions)):
                    if include_subfolders:
                        path = os.path.join(root, file)
                    else:
                        path = file
                    if all(filter in path for filter in filters):
                        if include_full_path:
                            if include_extension:
                                f.write(os.path.abspath(os.path.join(folder_path, path)) + '\n')
                            else:
                                f.write(os.path.splitext(os.path.abspath(os.path.join(folder_path, path)))[0] + '\n')
                        else:
                            if include_extension:
                                f.write(os.path.splitext(path)[0] + os.path.splitext(path)[1] + '\n')
                            else:
                                f.write(os.path.splitext(path)[0] + '\n')

root = tk.Tk()
root.title("File Scanner")

style = Style(theme='darkly')

folder_path_label = tk.Label(root, text="Input Folder Path:", font=("Helvetica", 14))
folder_path_label.grid(row=0, column=0, padx=10, pady=(30,10))

folder_path_entry = tk.Entry(root)
folder_path_entry.grid(row=0, column=1)

extensions_label = tk.Label(root, text="File Type Extensions (comma-separated):", font=("Helvetica", 14))
extensions_label.grid(row=1, column=0, padx=10, pady=10)

extensions_entry = tk.Entry(root)
extensions_entry.grid(row=1, column=1)

output_file_label = tk.Label(root, text="Output File Name:", font=("Helvetica", 14))
output_file_label.grid(row=2, column=0, padx=10, pady=10)

output_file_entry = tk.Entry(root)
output_file_entry.grid(row=2, column=1)

include_extension_var = tk.BooleanVar()
include_extension_checkbox = tk.Checkbutton(root, text="Include File Extension", variable=include_extension_var)
include_extension_checkbox.grid(row=3, columnspan=2)

include_subfolders_var = tk.BooleanVar()
include_subfolders_checkbox = tk.Checkbutton(root, text="Include Subfolders", variable=include_subfolders_var)
include_subfolders_checkbox.grid(row=4, columnspan=2)

include_full_path_var = tk.BooleanVar()
include_full_path_checkbox = tk.Checkbutton(root, text="Include Full Path", variable=include_full_path_var)
include_full_path_checkbox.grid(row=5, columnspan=2)

filters_label = tk.Label(root, text="Filters (comma-separated):", font=("Helvetica", 14))
filters_label.grid(row=6, column=0, padx=10, pady=(10,30))

filters_entry = tk.Entry(root)
filters_entry.grid(row=6, column=1)

browse_button = tk.Button(root,text="Browse",command=lambda: folder_path_entry.insert(0,filedialog.askdirectory()))
browse_button.grid(row=0,column=2,pady=(30))

run_button = tk.Button(root,text="Run Scan",command=list_files,height=2,width=20)
run_button.grid(row=7,columnspan=3,pady=(30))

for child in root.winfo_children():
    child.grid_configure(padx=(20),pady=(5))

root.geometry("680x320")
root.mainloop()
