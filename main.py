#!/usr/bin/env python3

import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

def main():
    traindata = pd.read_csv(r"C:\Users\rwadams\Documents\GitHub_Files\Stocking-on-Data\AAPL_train_data.csv")
    testdata = pd.read_csv(r"C:\Users\rwadams\Documents\GitHub_Files\Stocking-on-Data\AAPL_test_data.csv")
    properties = list(traindata.columns.values)
    properties.remove("Up_or_Down")
    trainX = traindata[properties]
    trainY = traindata["Up_or_Down"]
    testX = testdata[properties]
    testY = testdata["Up_or_Down"]
   
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(13,)),
        keras.layers.Dense(16, activation=tf.nn.relu),
	keras.layers.Dense(16, activation=tf.nn.relu),
        keras.layers.Dense(1, activation=tf.nn.sigmoid),
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    hist = model.fit(trainX, trainY, epochs=50, batch_size=1)

    #print(hist.history)

    test_loss, test_acc = model.evaluate(testX, testY)
    print('Test accuracy:', test_acc)
    print('Test loss: ' , test_loss)

    predictions = model.predict_classes(testX)
    predProbs = model.predict(testX)
    #rounded = [round(x[0]) for x in predictions]
    #print(predictions)
    #print(predProbs)

if __name__ == "__main__":
    main()
