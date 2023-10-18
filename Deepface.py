#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import ttk 
from deepface import DeepFace
import os
import pandas as pd

db_path = ""
img2_path = ""
dfs = []  # Initialize dfs as an empty list
models = [
    "VGG-Face",
    "Facenet",
    "Facenet512",
    "OpenFace",
    "DeepFace",
    "DeepID",
    "ArcFace",
    "Dlib",
    "SFace",
]




# Function to open a folder dialog and update db_path
def select_folder():
    global db_path
    db_path = filedialog.askdirectory()
    db_path_entry.delete(0, tk.END)
    db_path_entry.insert(0, db_path)

# Function to open a file dialog and update img2_path
def select_image():
    global img2_path
    img2_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    img2_path_entry.delete(0, tk.END)
    img2_path_entry.insert(0, img2_path)

# Function to open the selected second image
def open_second_image():
    global img2_path
    if img2_path:
        try:
            os.startfile(img2_path)
        except Exception as e:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Error opening the image: {str(e)}")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please select a second image.")

# Function to perform the DeepFace.find() when the user clicks a button
def find_similar_faces():
    global db_path, img2_path, dfs
    if not db_path or not img2_path:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please select both a database folder and a second image.")
    else:
        pd.set_option('display.max_colwidth', -1)
        pd.options.display.max_rows = 4000
        selected_model = model_selection.get()  # Get the selected model from the dropdown
        dfs = DeepFace.find(img2_path, db_path=db_path, model_name=selected_model, enforce_detection=False)

        # Display the results in the text widget
        result_text.delete(1.0, tk.END)  # Clear previous results

        for i, item in enumerate(dfs):
            combined_text = f"{i + 1}. {item['identity']}  {selected_model}_cosine: {item[selected_model + '_cosine']}\n"
            result_text.insert(tk.END, combined_text)

            
        
# Create a main window
root = tk.Tk()
root.title("Simple DeepFace Gui by Ehtz")


# Create a label and an entry widget for db_path
db_path_label = tk.Label(root, text="Database Images Folder:")
db_path_label.grid(row=0, column=0)

select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.grid(row=0, column=1)

db_path_entry = tk.Entry(root, textvariable=db_path, width=50)
db_path_entry.grid(row=0, column=2)





# Create a label and an entry widget for img2_path
img2_path_label = tk.Label(root, text="Base Image:")
img2_path_label.grid(row=1, column=0, pady=25)

# Create a button to open the file selection dialog for img2_path
select_image_button = tk.Button(root, text="Select Image", command=select_image)
select_image_button.grid(row=1, column=1)

# Create a button to open the selected second image
open_second_image_button = tk.Button(root, text="Open Base Image", command=open_second_image)
open_second_image_button.grid(row=1, column=3)

img2_path_entry = tk.Entry(root, textvariable=img2_path, width=50)
img2_path_entry.grid(row=1, column=2)





# Create a dropdown menu for selecting the model
model_label = tk.Label(root, text="Select Model:")
model_label.grid(row=4, column=0)

model_selection = ttk.Combobox(root, values=models)
model_selection.set("Facenet512")
model_selection.grid(row=4, column=1)




# Create a button to trigger the find_similar_faces function
find_button = tk.Button(root, text="Find Similar Faces", pady=15, bg="red", fg='white', command=find_similar_faces)
find_button.grid(row=6, column=0, columnspan=5, padx=10, pady=10)

# Create a text wido display the results
result_text = tk.Text(root, width=200, height=25, selectbackground="yellow", selectforeground='black', undo=True)
result_text.grid(row=7, column=0, columnspan=5, padx=10, pady=10)

# Create a scrollbar and attach it to the text widget
text_scroll = tk.Scrollbar(root, command=result_text.yview)
text_scroll.grid(row=7, column=5, sticky="ns")
result_text.config(yscrollcommand=text_scroll.set)



# Start the tkinter main loop
root.geometry("1650x500")
root.mainloop()
