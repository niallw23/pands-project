# A program to perform analysis on the iris data set

import pandas as pd # needed to read in data set
import matplotlib.pyplot as plt # will need for histogram
import numpy as np # with view to my own analysis
import seaborn as sns

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
'''
for col in iris_data.columns[:-1]: #leaves out the last column (class) which is not numerical
    plt.hist(iris_data[col])
    plt.title(col) #uses the column title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig (f'{col}.png') #names each png file with the column title
    
    plt.show()
'''
#third instruction
#outputs a scatter plot of each pair of variables
'''
for i, column1 in enumerate(iris_data.columns[:-1]): #runs enumerate function over data set columns, but not the last one as referenced earlier
    for j, column2 in enumerate(iris_data.columns[:-1]):
        if i < j:  # skip duplicate plots, if i >= j it won't go again. initially produced plots of petallength on petallength for example.
            x = iris_data[column1]
            y = iris_data[column2]
            plt.scatter(x, y)
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.show()
'''
# some additional analysis
sns.boxplot(data = iris_data, x= 'class', y= 'sepallength')
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.title('Box Plot of Sepal Length across Iris species')
plt.show() 


color_palette = {'Iris-setosa': 'yellow', 'Iris-versicolor': 'green', 'Iris-virginica': 'red'}
sns.boxplot(data= iris_data, x= 'class', y= 'sepalwidth', palette= color_palette)
plt.xlabel('Species')
plt.ylabel('Sepal Width')
plt.title('Box Plot of Sepal Width across Iris species')
plt.show()

color_palette = {'Iris-setosa': 'orange', 'Iris-versicolor': 'blue', 'Iris-virginica': 'purple'}
sns.boxplot(data= iris_data, x= 'class', y= 'petallength', palette= color_palette)
plt.xlabel('Species')
plt.ylabel('Petal Length')
plt.title('Box Plot of Petal Length across Iris species')
plt.show()


color_palette = {'Iris-setosa': 'pink', 'Iris-versicolor': 'red', 'Iris-virginica': 'black'}
sns.boxplot(data= iris_data, x= 'class', y= 'petalwidth', palette= color_palette)
plt.xlabel('Species')
plt.ylabel('Petal Width')
plt.title('Box Plot of Petal Width across Iris species')
plt.show()