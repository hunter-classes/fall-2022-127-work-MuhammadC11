# used matplotlib to create graphs for each of the following: car make, car style, car color, violation, fine amount, year, month, day, and hour.
# installed matplotlib using pip3 install matplotlib on mac
# installed pandas using pip3 install pandas on mac

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
csvData = pd.read_csv('parking_citations.csv')
print(csvData.astype("str"))
csv_dict = csvData.to_dict()

print("------------------------------------------")
# This returns the number of times each car make appears in the data set, The most popular car makes are at the top of the data set.
carMake = csvData["Data.Car.Make"].value_counts()
print(carMake)
print("------------------------------------------")
# This returns the number of times each car color appears in the data set, The most popular car colors are at the top of the data set.
colorData = csvData["Data.Car.Color"].value_counts()
print(colorData)
print("------------------------------------------")
# This returns the number of times each year appears in the data set, The most frequent years are at the top of the data set.
yearData = csvData["Date.Year"].value_counts()
print(yearData)
print("------------------------------------------")
# This returns the number of times each month appears in the data set, The most frequent months are at the top of the data set. 1 is January, 2 is February, etc.
monthData = csvData["Date.Month"].value_counts()
print(monthData)
print("------------------------------------------")
# This returns the number of times each day appears in the data set, The most frequent days are at the top of the data set.
dayData = csvData["Date.Day"].value_counts()
print(dayData)
print("------------------------------------------")
# This returns the number of times each hour appears in the data set, The most frequent hours are at the top of the data set.
hourData = csvData["Date.Time.Hour"].value_counts()
print(hourData)
print("------------------------------------------")
# This returns the number of times each car style appears in the data set, The most popular car styles are at the top of the data set.
carStyle = csvData["Data.Car.Style"].value_counts()
print(carStyle)
print("------------------------------------------")
# This returns the number of times each violation appears in the data set, The most frequent violations are at the top of the data set.
violation = csvData["Data.Violation"].value_counts()
print(violation)
print("------------------------------------------")
# This returns the number of times each fine amount appears in the data set, The most frequent fine amounts are at the top of the data set.
fineAmount = csvData["Data.Fine"].value_counts()
print(fineAmount)
print("------------------------------------------")

makeGraph = plt.figure(1)
carMake.plot(kind='bar', xlabel='Car Make', ylabel='Frequency Of Citations',
             title='Frequency of Parking Citations by Car Make')
makeGraph.show()

styleGraph = plt.figure(2)
carStyle.plot(kind='bar', xlabel='Car Style', ylabel='Frequency Of Citations',
              title='Frequency of Parking Citations by Car Style')
styleGraph.show()

colorGraph = plt.figure(3)
colorData.plot(kind='bar', xlabel='Car Color', ylabel='Frequency Of Citations',
               title='Frequency of Parking Citations by Car Color')
colorGraph.show()

violationGraph = plt.figure(4)
violation.plot(kind='bar', xlabel='Violation', ylabel='Frequency Of Citations',
               title='Frequency of Parking Citations by Violation')
violationGraph.show()

fineGraph = plt.figure(5)
fineAmount.plot(kind='bar', xlabel='Fine Amount', ylabel='Frequency Of Citations',
                title='Frequency of Parking Citations by Fine Amount')
fineGraph.show()

yearGraph = plt.figure(6)
yearData.plot(kind='bar', xlabel='Year', ylabel='Frequency Of Citations',
              title='Frequency of Parking Citations by Year')
yearGraph.show()

monthGraph = plt.figure(7)
monthData.plot(kind='bar', xlabel='Months', ylabel='Frequency',
               title='Frequency of Parking Citations by Month')
monthGraph.show()

dayGraph = plt.figure(8)
dayData.plot(kind='bar', xlabel='Day', ylabel='Frequency Of Citations',
             title='Frequency of Parking Citations by Day')
dayGraph.show()

hourGraph = plt.figure(9)
hourData.plot(kind='bar', xlabel='Hour', ylabel='Frequency Of Citations',
              title='Frequency of Parking Citations by Hour')
hourGraph.show()

input()
