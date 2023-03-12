import os
from tkinter import Tk, filedialog
from tkinter.ttk import Label, Entry, Button
from ttkbootstrap import Style

def replace_text_in_files(folder_path: str, old_text: str, new_text: str):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            with open(file_path) as f:
                content = f.read()
            content = content.replace(old_text, new_text)
            with open(file_path,'w') as f:
                f.write(content)

def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_entry.delete(0,'end')
    folder_entry.insert(0,folder_selected)

def run_replace():
    folder = folder_entry.get()
    old_text = old_text_entry.get()
    new_text = new_text_entry.get()
    replace_text_in_files(folder, old_text,new_text)

root = Tk()
style = Style(theme='superhero')
root.title('Text Replace')

folder_label = Label(root,text='Folder:')
folder_label.grid(row=0,column=0,padx=5,pady=5)

folder_entry = Entry(root)
folder_entry.grid(row=0,column=1,padx=5,pady=5)

browse_button = Button(root,text='Browse',command=select_folder)
browse_button.grid(row=0,column=2,padx=5,pady=5)

old_text_label = Label(root,text='Text that will be replaced:')
old_text_label.grid(row=1,column=0,padx=5,pady=5)

old_text_entry = Entry(root)
old_text_entry.grid(row=1,column=1,padx=5,pady=5)

new_text_label = Label(root,text='New Text:')
new_text_label.grid(row=2,column=0,padx=5,pady=5)

new_text_entry = Entry(root)
new_text_entry.grid(row=2,column=1,padx=5,pady=5)

run_button = Button(root,text='Run',command=run_replace)
run_button.grid(row=3,columnspan=3,padx=(10,0),pady=(10,0))

root.mainloop()
