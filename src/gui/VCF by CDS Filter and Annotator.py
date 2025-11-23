import os
import glob
import threading
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def run_merge(input_folder, progress_bar):

    # Start the progress bar
    progress_bar.start()

    # Go to input gff/gff3 file folder
    os.chdir(input_folder)

    # Get input gff file
    gff_file = list(glob.glob("*.gff") or glob.glob("*.gff3"))[0]

    # Get input vcf file
    vcf_file = glob.glob("*.vcf")[0]

    # Get gff filename
    gff_filename = os.path.splitext(gff_file)[0]

    # Get vcf filename
    vcf_filename = os.path.splitext(vcf_file)[0]

    # Run command
    command = f'gff2bed_features {gff_file} CDS > {gff_filename}.cds.bed && bedtk flt -c {gff_filename}.cds.bed  {vcf_file} | wsl vcfannotate -b {gff_filename}.cds.bed -k cds -d noannot > {vcf_filename}.cds.vcf'

    try:
        subprocess.run(command, check=True, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        progress_bar.stop()
        messagebox.showinfo("Success",f"Output files created at:\n{input_folder}".replace('/','\\'))


    except subprocess.CalledProcessError as e:
        progress_bar.stop()
        print(e)
        messagebox.showerror(f"Error: {e}")
        
def start_thread():
    input_folder = input_folder_var.get()

    if not input_folder:
        messagebox.showwarning("Input Error", "Please select an input folder.")
        return

    # Start command in a new thread
    thread = threading.Thread(target=run_merge, args=(input_folder, progress_bar))
    thread.start()

def select_folder():
    file_path = filedialog.askdirectory()
    input_folder_var.set(file_path)

# Set up tkinter app
app = tk.Tk()
app.title("VCF by CDS Filter and Annotator")

# Input file selection
input_folder_var = tk.StringVar()
tk.Label(app, text="Input folder:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(app, textvariable=input_folder_var, width=40).grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_folder).grid(row=0, column=2, padx=10, pady=10)

# Progress Bar (indeterminate)
progress_bar = ttk.Progressbar(app, mode="indeterminate", length=200)
progress_bar.grid(row=1, column=0, columnspan=3, padx=10, pady=20)

# Start button
tk.Button(app, text="Filter vcf", command=start_thread).grid(row=2, column=1, padx=10, pady=20)

# Trademark label
trademark_label = tk.Label(app,  text="Copyright (c) Olga Tsiouri, 2025 <olgatsiouri@outlook.com>", font=("Arial", 10), fg="black")
trademark_label.grid(row=3, column=0, columnspan=3, pady=(20, 10), sticky="s")

app.mainloop()
