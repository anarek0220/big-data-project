import tensorflow as tf
import keras
import pandas as pd
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import glob as gb
import os

trainpath = "train/"
testpath = "test/"
predpath = "predict/"
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
len(trainpath)

for folder in os.listdir(trainpath):
    files = gb.glob(pathname=str(trainpath+folder + "/*.jpeg"))
    print(f"for training data , found {len(files)} in folder {folder}")

for folder in os.listdir(testpath):
    files = gb.glob(pathname=str(testpath+folder + "/*.jpeg"))
    print(f"for training data , found {len(files)} in folder {folder}")


files = gb.glob(pathname=str(predpath+"/*.jpeg"))
print(len(files))
code_train = {"apple": 0, "avocado": 1, "banana": 2, "cherry": 3, "kiwi": 4, "mango": 5, "orange": 6, "pinenapple": 7,
              "strawberries": 8, "watermelon": 9}


def getcode_train(n):
    for x, y in code_train.items():
        if n == y:
            return x


code_train["apple"]
code_test = {"apple": 0, "avocado": 1, "banana": 2, "cherry": 3, "kiwi": 4, "mango": 5, "orange": 6, "pinenapple": 7,
             "stawberries": 8, "watermelon": 9}


def getcode_test(n):
    for x, y in code_test.items():
        if n == y:
            return x


code_test["mango"]

size = []
for folder in os.listdir(trainpath):
    files = gb.glob(pathname=str(trainpath + folder + "/*.jpeg"))
    for file in files:
        image = plt.imread(file)
        size.append(image.shape)

df = pd.Series(size)
pd.DataFrame(df.value_counts())  # [:60]

size = []
for folder in os.listdir(testpath):
    files = gb.glob(pathname=str(testpath + folder + "/*.jpeg"))
    for file in files:
        image = plt.imread(file)
        size.append(image.shape)

df = pd.Series(size)
pd.DataFrame(df.value_counts())[:30]



s = 150
x_test = []
y_test = []
#os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
for folder in os.listdir(testpath):
    files = gb.glob(pathname=str(testpath+folder + "/*.jpeg"))
    for file in files:
        image = cv.imread(file)
        image_array = cv.resize(image , (s,s))
        x_test.append(list(image_array))
        y_test.append(code_test[folder])

l = len(x_test)
plt.figure(figsize=(20 , 20))
for n , i in enumerate(list(np.random.randint(0 , l ,36 ))) :
    plt.subplot(6 , 6 , n+1)
    plt.imshow(x_test[i])
    plt.axis("off")
    plt.title(getcode_test(y_test[i]))

x_train = []
y_train = []
for folder in os.listdir(trainpath):
    files = gb.glob(pathname=str(trainpath+folder + "/*.jpeg"))
    for file in files:
        image = cv.imread(file)
        if image is None:
            continue
        image_array = cv.resize(image , (s,s))
        x_train.append(list(image_array))
        y_train.append(code_train[folder])
plt.figure(figsize=(20 , 20))
for n , i in enumerate(list(np.random.randint(0 , l ,36 ))) :
    plt.subplot(6 , 6 , n+1)
    plt.imshow(x_train[i])
    plt.axis("off")
    plt.title(getcode_train(y_train[i]))
x_pred = []
files = gb.glob(pathname=str(predpath +"/*.jpeg"))
for file in files:
    image = cv.imread(file)
    image_array = cv.resize(image , (s , s))
    x_pred.append(list(image_array))
len(x_pred)

plt.figure(figsize=(20 , 20))
for o , p in enumerate(list(np.random.randint(0 , 48 ,36))):
    plt.subplot(6 , 6 , o+1)
    plt.imshow(x_pred[p])
    plt.axis("off")

x_train = np.array(x_train)
y_train = np.array(y_train)
x_pred_array = np.array(x_pred)
x_test = np.array(x_test)
y_test = np.array(y_test)
print(x_test.shape)
model = keras.models.Sequential([
    keras.layers.Conv2D(250, kernel_size=(3, 3), activation="relu", input_shape=(s, s, 3)),
    keras.layers.Conv2D(230, kernel_size=(3, 3), activation="relu"),
    keras.layers.Conv2D(200, kernel_size=(3, 3), activation="relu"),
    keras.layers.MaxPool2D(6, 6),
    keras.layers.Conv2D(180, kernel_size=(3, 3), activation="relu"),
    keras.layers.Conv2D(100, kernel_size=(3, 3), activation="relu"),
    keras.layers.Conv2D(80, kernel_size=(3, 3), activation="relu"),
    keras.layers.MaxPool2D(6, 6),
    keras.layers.Flatten(),
    keras.layers.Dense(120, activation="relu"),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dense(50, activation="relu"),
    keras.layers.Dropout(rate=0.3),
    keras.layers.Dense(10, activation="softmax"),

])

model.compile(optimizer="adam" , loss="sparse_categorical_crossentropy" , metrics=["accuracy"])
model.summary()

model.fit(x_train , y_train , epochs=30 , batch_size = 64)

modelloss , modelaccuracy = model.evaluate(x_test , y_test)
y_pred = model.predict(x_test)
y_result = model.predict(x_pred_array)
y_result.shape
plt.figure(figsize=(20 , 20))
for n , i in enumerate(list(np.random.randint(0 , 48 , 36))):
    plt.subplot(6 , 6 , n+1)
    plt.imshow(x_pred[i])
    plt.axis("off")
    plt.title(getcode_train(np.argmax(y_result[i])))

tf.keras.models.save_model(
        model,
        "model/",
        overwrite=True,
        include_optimizer=True,
        save_format=None,
        signatures=None,
        options=None,
        save_traces=True
)