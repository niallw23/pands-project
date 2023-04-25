# pands-project
Repository for end of year project on Iris data set.

# The Iris Data Set

## What exactly is it?

As the name suggests, the Iris data set is a set of data. It is well known in computer science as an example data set to conduct analysis on. It was introduced by a British statistician and biologist by the name of Ronald Fisher all the way back in 1936. [^1]
There are three iris species in the data set Iris setosa, Iris virginica, and Iris versicolor. The dataset consists of 150 samples, with 50 samples from each of three iris species. For each sample, four features are recorded: the length and width of the sepals (the green leaf-like structures that protect the flower bud) and the length and width of the petals (the colorful parts of the flower). This was all new to me as I don't think I've ever actually seen an iris flower.
The data was collected by a man called Dr. Edgar Anderson in Canada. [^2]

## Downloading the data set
To use the data set, the first step was to download it. I looked at some examples where it was fed in through a URL but after watching the lecture videos and doing some more research (googling), I decided to save it locally as a csv file and work from there. I used this link and some helpful code to know it was working. [^3]

## The first task - Output a summary of each variable to a single text file
My approach to the project was to carry out the recommended tasks first before trying to potentially perform any of my own analyses.
To do this my research and our earlier lectures pointed me to the describe()[^4] function in pandas as opposed to trying to do my own summaries. As my data is numeric, when we get the summary it produces the count, mean, standard deviation, minimum value, 25/50/75 percentile marks and the maximum value. The example reading I looked at used the Californian housing market as a big data set - so it seemed like the best way for me to write a summary of my large data set. [^5]
Having just had to correct some of my weekly tasks for not using 'with' I was better able to apply it to the project. I encountered an error when I tested though and realised I needed to change the argument to a string. A quick google search was thankfully enough to correct this quickly and it then wrote the summary file. [^6]

## The second task - Saves a histogram of each variable
For this part of the project, the actual plotting of the histogram was code that I found useful during our week 08 lectures. The issue I was uncertain of was how to plot each variable or read each column. Using a for loop was something that came up frequently when I researched this part, and making use of the .columns function of analysing a data frame.

[^1] https://en.wikipedia.org/wiki/Iris_flower_data_set

[^2] https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5

[^3] https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/

[^4] https://www.w3schools.com/python/pandas/ref_df_describe.asp

[^5] https://www.askpython.com/python/examples/calculate-summary-statistics

[^5] https://www.w3schools.com/python/pandas/pandas_dataframes.asp

[^6] https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/