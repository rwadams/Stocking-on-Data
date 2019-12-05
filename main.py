#!/usr/bin/env python3

import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

def main():
    data = pd.read_csv(r"C:\Users\rwadams\Documents\GitHub_Files\Stocking-on-Data\y_finance_test_output.csv")
    properties = list(data.columns.values)
    properties.remove("Date")
    properties.remove("Volume")
    properties.remove("Dividends")
    properties.remove("Stock Splits")
    properties.remove("Actual")
    properties.remove("Average")
    X = data[properties]
    Y = data["Actual"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

   
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(4,)),
        keras.layers.Dense(16, activation=tf.nn.relu),
	keras.layers.Dense(16, activation=tf.nn.relu),
        keras.layers.Dense(1, activation=tf.nn.sigmoid),
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    hist = model.fit(X_train, Y_train, epochs=50, batch_size=1)

    print(hist.history)

    test_loss, test_acc = model.evaluate(X_test, Y_test)
    print('Test accuracy:', test_acc)
    print('Test loss: ' , test_loss)

    predictions = model.predict_classes(X_test)
    predProbs = model.predict(X_test)
    #rounded = [round(x[0]) for x in predictions]
    #print(predictions)
    #print(predProbs)

if __name__ == "__main__":
    main()
