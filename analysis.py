# A program to perform analysis on the iris data set

import pandas as pd # needed to read in data set
import matplotlib.pyplot as plt # will need for histogram
import numpy as np # with view to my own analysis

data = pd.read_csv('iris_csv.csv') # referenced in readme

# first instruction
# program should output a summary of each variable to a single text file

summary = data.describe() #uses describe() to get the summary, referenced in readme
 

