#!/usr/bin/env python
# coding: utf-8

# In[79]:


import tkinter as tk
from tkinter import filedialog
from deepface import DeepFace
import os

# Initialize global variables
db_path = ""
img2_path = ""
dfs = []  # Initialize dfs as an empty list

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
        
def open_first_image_from_list():
    global dfs
    if dfs:
        try:
            # Convert the Series object to a string and then open the image
            os.startfile(str(dfs[0]['identity']))
        except Exception as e:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Error opening the image: {str(e)}")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "No results available.")
        
# Function to perform the DeepFace.find() when the user clicks a button
def find_similar_faces():
    global db_path, img2_path, dfs
    if not db_path or not img2_path:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please select both a database folder and a second image.")
    else:
        pd.options.display.max_columns = None
        dfs = DeepFace.find(img2_path, db_path=db_path, model_name='Facenet512', enforce_detection=False)

        # Display the results in the text widget
        result_text.delete(1.0, tk.END)  # Clear previous results
        for item in dfs:
            result_text.insert(tk.END, f"Image Path: {item['identity']}\n")
            result_text.insert(tk.END, f"Facenet512_cosine: {item['Facenet512_cosine']}\n\n")
            
        # Enable the "Open First Image from List" button
        open_first_image_from_list_button.config(state=tk.DISABLED)

# Initialize the tkinter GUI
root = tk.Tk()
root.title("Folder and Image Selection")

# Create a label and an entry widget for db_path
db_path_label = tk.Label(root, text="Database Images Folder:")
db_path_label.pack()

db_path_entry = tk.Entry(root, textvariable=db_path, width=50)
db_path_entry.pack()

# Create a button to open the folder selection dialog for db_path
select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.pack()

# Create a label and an entry widget for img2_path
img2_path_label = tk.Label(root, text="Base Image:")
img2_path_label.pack()

img2_path_entry = tk.Entry(root, textvariable=img2_path, width=50)
img2_path_entry.pack()

# Create a button to open the file selection dialog for img2_path
select_image_button = tk.Button(root, text="Select Image", command=select_image)
select_image_button.pack()

# Create a button to open the selected second image
open_second_image_button = tk.Button(root, text="Open Base Image", command=open_second_image)
open_second_image_button.pack()

# Create a button to open the picture of the first image from the dfs list
open_first_image_from_list_button = tk.Button(root, text="Open First Image from List", command=open_first_image_from_list,state=tk.DISABLED)
open_first_image_from_list_button.pack()

# Create a button to trigger the find_similar_faces function
find_button = tk.Button(root, text="Find Similar Faces", pady=15, bg="green", command=find_similar_faces)
find_button.pack()

# Create a text widget to display the results
result_text = tk.Text(root, width=200, height=100)
result_text.pack()

# Start the tkinter main loop
root.mainloop()


# In[ ]:




