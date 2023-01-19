import tensorflow as tf
import keras
import pandas as pd
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import glob as gb
import os

testpath_2 = "test_1/"
load_model = tf.keras.models.load_model(
    "model/", custom_objects=None, compile=True, options=None
)


trainpath = "train/"
testpath = "test/"
predpath = "predict/"

len(trainpath)

for folder in os.listdir(trainpath):
    files = gb.glob(pathname=str(trainpath+folder + "/*.jpeg"))

for folder in os.listdir(testpath):
    files = gb.glob(pathname=str(testpath+folder + "/*.jpeg"))


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
for o , p in enumerate(list(np.random.randint(0 , 1 ,36))):
    plt.subplot(6 , 6 , o+1)
    plt.imshow(x_pred[p])
    plt.axis("off")

x_train = np.array(x_train)
y_train = np.array(y_train)
x_pred_array = np.array(x_pred)
x_test = np.array(x_test)
y_test = np.array(y_test)

y_result = load_model.predict(x_pred_array)


plt.figure(figsize=(20 , 20))
for n , i in enumerate(list(np.random.randint(0 , 1 , 36))):
    plt.subplot(6 , 6 , n+1)
    plt.imshow(x_pred[i])
    plt.axis("off")
    plt.title(getcode_train(np.argmax(y_result[i])))

result_dic = {0: "apple", 1: "avocado", 2: "banana", 3: "cherry", 4: "kiwi", 5: "mango", 6: "orange", 7: "pinenapple", 8: "stawberries", 9: "watermelon"}

for abc in y_result:
    print(result_dic[abc.argmax()])


