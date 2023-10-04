# deepface-gui
Simple GUI for deepface ONLY "DeepFace.find"

[Face recognition](https://sefiks.com/2020/05/25/large-scale-face-recognition-for-deep-learning/) requires applying face verification many times. Herein, deepface has an out-of-the-box find function to handle this action. It's going to look for the identity of input image in the database path and it will return list of pandas data frame as output. Meanwhile, facial embeddings of the facial database are stored in a pickle file to be searched faster in next time. Result is going to be the size of faces appearing in the source image. Besides, target images in the database can have many faces as well.


```python
dfs = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
```

<p align="center"><img src="https://raw.githubusercontent.com/serengil/deepface/master/icon/stock-6-v2.jpg" width="95%" height="95%"></p>
