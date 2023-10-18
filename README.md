# Simple DeepFace GUI by Ehtz

This is a simple graphical user interface (GUI) for DeepFace, a deep learning framework for facial recognition. The GUI allows you to find similar faces in a database using various face recognition models. Here's how to use it:

## Getting Started
1. Ensure you have Python installed on your system.

2. Clone this repository or download the `deepface_gui.py` file to your local machine.

3. Install the required Python libraries by running the following command:
   ```shell
   pip install deepface pandas
Running the Application
Open a terminal or command prompt.

Navigate to the directory where the deepface_gui.py file is located.

Run the application by executing the following command:

shell
Copy code
python deepface_gui.py
The GUI application window will open.

How to Use
Database Images Folder: Click the "Select Folder" button to choose a folder containing your database images. This is the collection of images you want to search for similar faces in.

Base Image: Click the "Select Image" button to choose the image you want to find similar faces for. You can also click "Open Base Image" to view the selected image.

Select Model: Choose a face recognition model from the dropdown menu. The default is "Facenet512," but you can select other models provided in the list.

Click the "Find Similar Faces" button to start the face recognition process.

The results will be displayed in the text area below. You will see a list of similar faces found in the database, along with similarity scores for the selected model.

Use the scrollbar on the right to scroll through the results.

Important Notes
This application uses DeepFace for face recognition. Make sure to provide a database folder with images and a base image for comparison.

The accuracy of the results depends on the selected model and the quality of the images in your database.

If you encounter any errors or issues, please make sure you have correctly installed the required libraries and provided valid file paths.





![Screenshot](Screenshot.png)








[Face recognition](https://sefiks.com/2020/05/25/large-scale-face-recognition-for-deep-learning/) requires applying face verification many times. Herein, deepface has an out-of-the-box find function to handle this action. It's going to look for the identity of input image in the database path and it will return list of pandas data frame as output. Meanwhile, facial embeddings of the facial database are stored in a pickle file to be searched faster in next time. Result is going to be the size of faces appearing in the source image. Besides, target images in the database can have many faces as well.


```python
dfs = DeepFace.find(img2_path, db_path=db_path, model_name=selected_model, enforce_detection=False)
```
Added Drop Down -  Chose between certain models
FaceNet, VGG-Face, ArcFace and Dlib are [overperforming](https://youtu.be/i_MOwvhbLdI) ones based on experiments. You can find out the scores of those models below on both [Labeled Faces in the Wild](https://sefiks.com/2020/08/27/labeled-faces-in-the-wild-for-face-recognition/) and YouTube Faces in the Wild data sets declared by its creators.

| Model | LFW Score | YTF Score |
| ---   | --- | --- |
| Facenet512 | 99.65% | - |
| SFace | 99.60% | - |
| ArcFace | 99.41% | - |
| Dlib | 99.38 % | - |
| Facenet | 99.20% | - |
| VGG-Face | 98.78% | 97.40% |
| *Human-beings* | *97.53%* | - |
| OpenFace | 93.80% | - |
| DeepID | - | 97.05% |
