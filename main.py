#!/usr/bin/env python3

import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

def highlight(val):
    if row['Up_or_Down'] == row['Predictions']:
        color =  'green'
    else:
        color =  'white'

    return ['background-color: {}'.format(color) for _ in row]

def main():
#    traindata = pd.read_csv(r"C:\Users\rwadams\Documents\GitHub_Files\Stocking-on-Data\MSFT_train_data.csv")
#    testdata = pd.read_csv(r"C:\Users\rwadams\Documents\GitHub_Files\Stocking-on-Data\MSFT_test_data.csv")

    traindata = pd.read_csv("MSFT_train_data.csv")
    testdata = pd.read_csv("MSFT_test_data.csv")

    properties = list(traindata.columns.values)
    #properties.remove("Date")
    #properties.remove("Volume")
    #properties.remove("Dividends")
    #properties.remove("Stock Splits")
    #properties.remove("Actual")
    #properties.remove("Average")
    properties.remove("Up_or_Down")
    trainX = traindata[properties]
    trainY = traindata["Up_or_Down"]
    testX = testdata[properties]
    testY = testdata["Up_or_Down"]

    #X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

   
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

    print(predictions)
    #print(predProbs)

    # add the column to the test data set
    testdata['Predictions'] = predictions
#    testdata.style.apply(highlight, axis=1)
    testdata.to_csv("MSFT_output_data.csv")

if __name__ == "__main__":
    main()


