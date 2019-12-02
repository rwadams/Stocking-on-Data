#!/usr/bin/env python3

import csv
import random

storeOpenVals = []
guessUp = .5
first = True
prediction = 0 #1 for up, 0 for down
numCorrect = 0

with open(r'C:\Users\rwadams\Documents\Fall 2019\CS 437 Project\y_finance_test_output.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    lineCount = 1
    for row in csv_reader:
        if lineCount < 7769:
            lineCount += 1
        else:
            storeOpenVals.append(row[1])

prevVal = storeOpenVals.pop(0)

for val in storeOpenVals:
    randomVal = random.uniform(0, 1)
    if randomVal < guessUp: #Ex: guessUp = .8, value can be between 0 and .8 out of 1 (80%)
        prediction = 1
    else:
        prediction = 0
    if val >= prevVal:
        if prediction == 1:
            numCorrect += 1
        if guessUp < 1:
            guessUp += .05
    else:
        if prediction == 0:
            numCorrect += 1
        if guessUp > 0:
            guessUp -= .05
    prevVal = val

accuracy = numCorrect/(len(storeOpenVals) - 1)

print(accuracy)
            
    
