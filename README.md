# Simple DeepFace GUI by Ehtz

This is a *simple* graphical user interface (GUI) for DeepFace, a deep learning framework for facial recognition. The GUI allows you to find similar faces in a database using various face recognition models. Here's how to use it:

## Getting Started
1. Ensure you have Python installed on your system.

2. Clone this repository or download the `deepface_gui.py` file to your local machine.

3. Install the required Python libraries by running the following command:
`pip install deepface pandas`


## Running the Application
1. Open a terminal or command prompt.

2. Navigate to the directory where the `deepface_gui.py` file is located.

3. Run the application by executing the following command:
`python deepface_gui.py`

5. The GUI application window will open.

## How to Use
- **Database Images Folder**: Click the "Select Folder" button to choose a folder containing your database images. This is the collection of images you want to search for similar faces in.

- **Base Image**: Click the "Select Image" button to choose the image you want to find similar faces for. You can also click "Open Base Image" to view the selected image.

- **Select Model**: Choose a face recognition model from the dropdown menu. The default is "Facenet512," but you can select other models provided in the list.

- Click the "Find Similar Faces" button to start the face recognition process.

- The results will be displayed in the text area below. You will see a list of similar faces found in the database, along with similarity scores for the selected model.

- Use the scrollbar on the right to scroll through the results.

## Important Notes
- This application uses DeepFace for face recognition. Make sure to provide a database folder with images and a base image for comparison.

- The accuracy of the results depends on the selected model and the quality of the images in your database.

- If you encounter any errors or issues, please make sure you have correctly installed the required libraries and provided valid file paths.



---




![Screenshot](Screenshot.png)
<div align="center">
<p>(Screen shot taken of the GUI)</p>
</div>




---


Only used the `DeepFace.find` command:


```python
dfs = DeepFace.find(img2_path, db_path=db_path, model_name=selected_model, enforce_detection=False)
```
Added Drop Down -  Chose between certain models
FaceNet, VGG-Face, ArcFace and Dlib are [overperforming](https://youtu.be/i_MOwvhbLdI) ones based on experiments. You can find out the scores of those models below on both [Labeled Faces in the Wild](https://sefiks.com/2020/08/27/labeled-faces-in-the-wild-for-face-recognition/) and YouTube Faces in the Wild data sets declared by its creators.

<div align="center">
  <table>
    <tr>
      <th>Model</th>
      <th>LFW Score</th>
      <th>YTF Score</th>
    </tr>
    <tr>
      <td>Facenet512</td>
      <td>99.65%</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SFace</td>
      <td>99.60%</td>
      <td>-</td>
    </tr>
    <tr>
      <td>ArcFace</td>
      <td>99.41%</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Dlib</td>
      <td>99.38%</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Facenet</td>
      <td>99.20%</td>
      <td>-</td>
    </tr>
    <tr>
      <td>VGG-Face</td>
      <td>98.78%</td>
      <td>97.40%</td>
    </tr>
    <tr>
      <td><i>Human-beings</i></td>
      <td><i>97.53%</i></td>
      <td>-</td>
    </tr>
    <tr>
      <td>OpenFace</td>
      <td>93.80%</td>
      <td>-</td>
    </tr>
    <tr>
      <td>DeepID</td>
      <td>-</td>
      <td>97.05%</td>
    </tr>
  </table>
</div>


---
Enjoy using this **Simple DeepFace GUI**!

**Author**: Ehtz

**GitHub Repository**: [link](https://github.com/Ehtz)

**Link towards the main DeepFace project**: [link](https://github.com/serengil/deepface)

Please report any issues or suggestions on the GitHub repository.

