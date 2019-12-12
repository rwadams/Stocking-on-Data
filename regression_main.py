#!/usr/bin/env python3

import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def main():
    traindata = pd.read_csv(r"C:\Users\rwadams\Documents\GitHub_Files\Stocking-on-Data\AAPL_train_data.csv")
    testdata = pd.read_csv(r"C:\Users\rwadams\Documents\GitHub_Files\Stocking-on-Data\AAPL_test_data.csv")
    properties = list(traindata.columns.values)
    properties.remove("Value")
    trainX = traindata[properties]
    trainY = traindata["Value"]
    testX = testdata[properties]
    testY = testdata["Value"]
   
    model = keras.Sequential()
    model.add(keras.layers.Dense(16, input_dim=13, activation='relu'))
    model.add(keras.layers.Dense(16, activation='relu'))
    model.add(keras.layers.Dense(1, activation='linear'))

    model.compile(optimizer='adam', loss='mse')
    
    hist = model.fit(trainX, trainY, epochs=50, batch_size=1)

    #print(hist.history)

    ypreds = model.predict(testX)
    #print(testY)

    x = np.linspace(1, len(testX), len(testX))

    plt.plot(x, testY, label='Actual prices')
    plt.plot(x, ypreds, label='Predicted prices')
    plt.title('Actual and Predicted Stock Prices over days')
    plt.legend()
    plt.show()

    aveDist = 0
    count = 0
    differences = []
    for actual in testY:
        predicted = ypreds[count]
        differences.append(abs(actual - predicted))
        count += 1
    aveDist = float(sum(differences)/len(differences))

    print("Average difference between prediction and actual: $" + str(aveDist))

if __name__ == "__main__":
    main()
