#A template for the implementation of K-Means.
import math #sqrt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import distance

#Importing Dataset
dataset = pd.read_csv('../data/movehubjoin.csv')

#dataset.plot()
dataset.plot(kind='scatter', x='Purchase Power', y='Cappuccino')

#Purchase Power
X = dataset.iloc[:,8]
#Cappuccino
Y = dataset.iloc[:,1]

#Puts all datapoints in points[] array
points = []
for i in range(sum(1 for line in open('../data/movehubjoin.csv'))):
	if (i < X.size) and (i < Y.size):
		point = [X[i], Y[i]]
		points.append(point)	

# Accepts two data points a and b.
# Returns the euclidian distance
# between a and b.
def euclideanDistance(a,b):
	left = (b[0] - a[0])**2
	right = (b[1] - a[1])**2
	return math.sqrt(left + right)

# Accepts a list of data points D, and a list of centers
# Returns a dictionary of lists called "clusters", such that
# clusters[c] is a list of every data point in D that is closest
#  to center c.
k = 2
centroids = []

#initialize centroids randomly
for i in range(k):
	centroids.insert(i, points[i])
	
def assignClusters(D, centers):
	clusters = {}
	for data_point in D:
		distances = []
		for center in centroids:
			#Find minimum euclidean distance from current data_point to each center
			distances.append(euclideanDistance(data_point, center))

		min_index = distances.index(min(distances))
		clusters.setdefault(min_index, []).append(data_point)
	return clusters
	
print(assignClusters(points[10:30], centroids))
	
# Accepts a list of data points.
# Returns the mean of the points.
def findClusterMean(cluster):
	sumX = 0
	sumY = 0
	for point in cluster:
		sumX += point[0]
		sumY += point[1]
	
	meanX = sumX/len(cluster)
	meanY = sumY/len(cluster)
	
	return [[meanX, meanY]]
	
	
# Accepts a list of data points, and a number of clusters.
# Produces a set of lists representing a K-Means clustering
#  of D.
'''def KMeans(D, k):
	means = D[1:k]
	do:
		oldMeans = means
		clusters = []
		foreach point in dataset:
			nearest = means[0]
			foreach m in means:
				if dist(m,point) < dist(nearest, point):
					nearest = m
				clusters[nearest].append(point)
			
		
while means != oldMeans'''
	

