# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:02:22 2019

@author: Christopher
"""
import yfinance as yf
import math

def main():
    # variables to be changed as we go
    days_recorded = 10            # number of days for each batch of stock data
    days_start_creation = 100     # number of days since stock was first offered removed
    days_skipped_between = 15     # number of days between any two batches of stock data
    days_end_creation = 100       # number of days before current day removed
    percentage_for_testing = 3    # Percentage of data to be moved to test data
    tickers = ["MSFT"]
    
    for x in tickers:
        # gets the stock data for a given ticker
        ticker = yf.Ticker(x)
        hist = ticker.history(period="max")
        price_history = hist["Close"].tolist()
        # calculates the number of batches that will be created
        number_of_batches = math.floor((len(hist)-days_start_creation-days_end_creation)/days_skipped_between)
        data = list()
        # iterates through stock data to create unique training data
        for i in range (0,number_of_batches):
            days_of_data = list()
            start_day = days_start_creation + i*days_skipped_between
            for j in range (0, days_recorded):
                days_of_data.append(price_history[start_day+j])
                # At end of batch records average, max and min
                if j == days_recorded-1:
                    days_of_data.append(sum(days_of_data)/days_recorded)
                    days_of_data.append(max(days_of_data))
                    days_of_data.append(min(days_of_data))
                    # adds next day, if it went up as a 1, if it went down or stayed the same 0
                    days_of_data.append(price_history[start_day+j+1])
            data.append(days_of_data)
            
        # writes data to a csv
        f = open(x+"_test_data"+".csv","w+")
        f2 = open(x+"_train_data"+".csv","w+")
        for j in range (0,len(data)):
            # Formats headers of csv files
            if j == 0:
                for k in range (0,days_recorded):
                    f.write("day{},".format(k))
                f.write("Average,Max,Min,Value\n")
                
                for k in range (0,days_recorded):
                    f2.write("day{},".format(k))
                f2.write("Average,Max,Min,Value\n")
            
            if j%percentage_for_testing == 1:
                for k in range (0,days_recorded+4):
                    if k < days_recorded+3:
                        f.write("{},".format(data[j][k]))
                    else:
                        f.write("{}\n".format(data[j][k]))    
            else:
                for k in range (0,days_recorded+4):
                    if k < days_recorded+3:
                        f2.write("{},".format(data[j][k]))
                    else:
                        f2.write("{}\n".format(data[j][k]))
        f.close()
                
    
    

if __name__ == '__main__':
    main()
