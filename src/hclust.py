#A template for the implementation of hclust
import math #sqrt
import matplotlib.pyplot as plt
import pandas as pd

#Importing Dataset
dataset = pd.read_csv('../data/movehubjoin.csv')

#Purchase Power -- X-axis
X = dataset.iloc[:,8]
#Cappuccino 	   -- Y-axis
Y = dataset.iloc[:,1]

#Puts all datapoints in points[] array
#Each x- and y-coordinate stored in an array [x, y]
points = []
for i in range(sum(1 for line in open('../data/movehubjoin.csv'))):
	if (i < X.size) and (i < Y.size):
		point = [X[i], Y[i]]
		points.append(point)	

# Accepts two data points a and b.
# Returns the distance between a and b.
# Note that this might be specific to your data.
def Distance(a,b):

# Accepts two data points a and b.
# Produces a point that is the average of a and b.
def merge(a,b)

# Accepts a list of data points.
# Returns the pair of points that are closest
def findClosestPair(D):

	
	
# Accepts a list of data points.
# Produces a tree structure corresponding to a
# Agglomerative Hierarchal clustering of D.
def HClust(D):
