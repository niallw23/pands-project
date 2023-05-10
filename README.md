# pands-project
Repository for end of year project on Iris data set.

# The Iris Data Set

## What exactly is it?

As the name suggests, the Iris data set is a set of data. It is well known in computer science as an example data set to conduct analysis on. It was introduced by a British statistician and biologist by the name of Ronald Fisher all the way back in 1936. [^1]
There are three iris species in the data set Iris setosa, Iris virginica, and Iris versicolor. The dataset consists of 150 samples, with 50 samples from each of three iris species. For each sample, four features are recorded: the length and width of the sepals (the green leaf-like structures that protect the flower bud) and the length and width of the petals (the colorful parts of the flower). This was all new to me as I don't think I've ever actually seen an iris flower that wasn't painted by Van Gogh.
The data was collected by a man called Dr. Edgar Anderson in Canada. [^2]

## Downloading the data set
To use the data set, the first step was to download it. I looked at some examples where it was fed in through a URL but after watching the lecture videos and doing some more research (googling), I decided to save it locally as a csv file and work from there. I used this link and some helpful code to know it was working. [^3]

## The first task - Output a summary of each variable to a single text file
My approach to the project was to carry out the recommended tasks first before trying to potentially perform any of my own analyses.
To do this my research and our earlier lectures pointed me to the describe()[^4] function in pandas as opposed to trying to do my own summaries. As my data is numeric, when we get the summary it produces the count, mean, standard deviation, minimum value, 25/50/75 percentile marks and the maximum value. The example reading I looked at used the Californian housing market as a big data set - so it seemed like the best way for me to write a summary of my large data set. [^5]
Having just had to correct some of my weekly tasks for not using 'with' I was better able to apply it to the project. I encountered an error when I tested though and realised I needed to change the argument to a string. A quick google search was thankfully enough to correct this quickly and it then wrote the summary file. [^6]

## The second task - Saves a histogram of each variable
For this part of the project, the actual plotting of the histogram was code that I found useful during our week 08 lectures. The issue I was uncertain of was how to plot each variable or read each column. Using a for loop was something that came up frequently when I researched this part, and making use of the .columns function of analysing a data frame. I initially was working through the columns 0-5 but realised that the last column obviously didn't have numbers to display. This was where I stumbled upon an extension of some of the slicing we had had to do for the weekly tasks. Some googling and a quick read had me testing out ways to set it to iterate over the columns but not the last one and I tried it that way. When it ran successfully (from what I could tell) I kept it as [:-1] [^7] Labelling the axes and giving the histogram a title were relatively straightforward as I remebered quite a bit from the lectures on plotting and histograms. I was having difficult saving each histogram as a separate png file and this sent me off researching again as I could only save an image of the first one. It turned out to be a matter of moving the savefig into the for loop as I had initially left it on its own line but I didn't come to this realisation on my own and found this [^8] very useful for a number of aspects of this task. I understand I'm not the first person to try to analyse data but it really was eye-opening, and obviously very helpful, to have so many sources so easily accessible online for solving problems. While I did waste some time reading bits that ended up not being relevant, I found having too much to be preferable to too little.

## The third task
The next analysis outlined in the project was to output a scatter plot of each pair of variables. Using a for loop and the columns function was the way I decided to approach this. I was able to find a very helpful site that coincidentally used the iris data set as its example when going through the use of for loops and columns to iterate over columns in a dataframe. [^9] There were also some useful snippets on Geeks for Geeks that helped and gave me a starting point to work off when trying to iterate over each of the columns. [^10]
The enumerate function was another thing I learned more about and was then able to use for this task. It is a built in function that lets you get the index of an element while iterating over a list [^11]. So using this, and the fact we wanted to work on each pair of variables for the task I assigned the index i to each column and then the column itself be 'column 1' and ran it against j and 'column 2'. I then put in an if statement that stopped me creating scatterplots of the same columns which I did the first time. By putting in the statement, it meant that if the index of the first column was less than the second it created the plot but then it wouldn't create duplicates.
After that, assigning the x, y values and doing the scatter and labelling parts were bits I could look back on and execute from previous tasks/lectures.
It brought me to the end of what I considered the assigned part of the tasks before beginning any further analysis of my own from some of the reading I had done.

## Additional analysis - some boxplots.
One of the first things I wanted to try was some plotting using seaborn. I watched some videos on it earlier in the term and heard it referenced. It also cropped up frequently in a lot of exploratory analysis of the data set. For me, this represented a perfect storm. I was going to be able to research and use the seaborn library (I had to go back and import it first) and it was going to help me produce some meaningful analysis.
One of the plots I frequently saw mentioned was a box plot. When I set about trying to write some of the code myself, I encountered a couple of different versions of the analysis. Some had used boxplots to compare each category (sepal length, width, petal length, width) and others compared a single category across the different species or 'classes'.
I found that one to be more useful as I had already done quite a bit of analysis across the four categories. The chance to focus in on an analysis of a particular one was an interesting opportunity to use the box plot. So having looked at some examples, I decided to plot the sepal length and compare them across the three species - setosa, versicolor, virginica.
Using the seaborn website [^12] helped me perform this initial box plot on the sepal length and explained exactly what the plot was showing, including explaining any outliers.
When I got this to work I wanted to do another one for the sepal width but this time change the colors. I tried using a color= instruction but quickly returned an error. This brought me to learning about palettes and I was able to modify the examples I looked at to change the colour of the plots for my own one. [^13]
When I got this functioning, I then completed box plots for the last two classes - this time visualising the difference across species in petal length and width. I think it was useful to be able to see the species compared by each class.

## Frequency of different values
One of the example analyses I looked at on the iris data set [^14] had some interesting frequency histograms of different features and values. I initially tried to recreate one for the classes in the set using a bar chart (as opposed to repeating earlier histogram code) but it obviously returned a fairly simple 50-50-50 result. So I decided to use this code to look at the petal length instead and see were there many results of the same length. I used the value.counts code and assigned it to the petal length column. It returned a bar chart with the values in descneding order and showed that 1.5 was the most common value. It was a more interesting use of the code in this case as opposed to showing something we would be familiar with from the raw data.


## Pairplot
Another visualisation that I found interesting was the use of pairplot as explored in this data analysis [^15]. It plotted all of the columns relationships against each other and I thought it was a really good summary visualisation. It also makes it possible for easy comparisons and to identify any patterns or insights by seeing the data laid out in such a manner. It was also very easy code to understand and include - the only real alteration I had to make was to the title of the column I wanted to analyse.

## Heatmap


### References

[^1] https://en.wikipedia.org/wiki/Iris_flower_data_set

[^2] https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5

[^3] https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/

[^4] https://www.w3schools.com/python/pandas/ref_df_describe.asp

[^5] https://www.askpython.com/python/examples/calculate-summary-statistics

[^5] https://www.w3schools.com/python/pandas/pandas_dataframes.asp

[^6] https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/

[^7] https://www.tutorialspoint.com/what-is-a-negative-indexing-in-python#

[^8] https://education.molssi.org/python_scripting_cms/05-plotting/index.html

[^9] https://www.datacamp.com/tutorial/for-loops-in-python

[^10] https://www.geeksforgeeks.org/iterating-over-rows-and-columns-in-pandas-dataframe/

[^11] https://pythonbasics.org/enumerate/

[^12] https://seaborn.pydata.org/generated/seaborn.boxplot.html

[^13] https://www.geeksforgeeks.org/seaborn-coloring-boxplots-with-palettes/

[^14] https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset

[^15] https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/