# A program to perform analysis on the iris data set

import pandas as pd # needed to read in data set
import matplotlib.pyplot as plt # will need for histogram
import numpy as np # with view to my own analysis

iris_data = pd.read_csv('iris_csv.csv') # referenced in readme

# first instruction
# program should output a summary of each variable to a single text file

summary = iris_data.describe() #uses describe() to get the summary, referenced in readme

# Write the summary statistics to a text file
#with open('iris_summary.txt', 'w') as file:
#    file.write(summary)  # got an error that argument must be string

#with open ('iris_summary.txt', 'w') as file:
    #file.write(summary.to_string())

#second instruction
#saves a histogram of each variable to png files

for col in iris_data.columns[0:4]:
    plt.hist(iris_data[col])
    plt.title(col)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()