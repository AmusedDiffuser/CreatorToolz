import os
from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog
from ttkbootstrap import Style

def trim_mp3_files(folder_path: str, milliseconds: int):
    print(f"Trimming mp3 files in {folder_path} by {milliseconds} milliseconds")
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3") or filename.endswith(".MP3"):
            print(f"Trimming {filename}")
            file_path = os.path.join(folder_path, filename)
            audio = AudioSegment.from_mp3(file_path)
            trimmed_audio = audio[:-milliseconds]
            trimmed_audio.export(file_path, format="mp3")
        else:
            print(f"Not an mp3 file: {filename}")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

def start_trimming():
    folder_path = folder_entry.get()
    milliseconds = int(milliseconds_entry.get())
    trim_mp3_files(folder_path, milliseconds)

style = Style(theme="superhero")
root = style.master

folder_label = tk.Label(root, text="Folder:")
folder_label.pack(padx=16, pady=16)

folder_entry = tk.Entry(root)
folder_entry.pack(padx=16)

browse_button = tk.Button(root, text="Browse", command=select_folder)
browse_button.pack(pady=16)

milliseconds_label = tk.Label(root, text="Milliseconds:")
milliseconds_label.pack(padx=16)

milliseconds_entry = tk.Entry(root)
milliseconds_entry.pack(padx=16)

trim_button = tk.Button(root, text="Trim MP3 Files", command=start_trimming)
trim_button.pack(pady=16)

root.mainloop()