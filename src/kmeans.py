#A template for the implementation of K-Means.
import math #sqrt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

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
	
def assignClusters(D, centers):
	clusters = {}
	for data_point in D:
		distances = []
		for center in centers:
			#Find minimum euclidean distance from current data_point to each center
			distances.append(euclideanDistance(data_point, center))

		min_index = distances.index(min(distances))
		clusters.setdefault(min_index, []).append(data_point)
	return clusters

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
	
	return [meanX, meanY]	
	
# Accepts a list of data points, and a number of clusters.
# Produces a set of lists representing a K-Means clustering
#  of D.
def KMeans(D, k):
	#initialize means and oldMeans to size k
	means = D[0:k]
	oldMeans = [None] * k

	#generate k number of centroids
	#random x- and y-coordinate initially assigned to centroids
	centroids = []
	for i in range(k):
		randX = random.uniform(1, np.max(X))
		randY = random.uniform(1, np.max(Y))
		centroids.insert(i, [randX, randY])
	print('centroids: ' , centroids)

	#iterate until the values of the means stop changing (stabilizes)
	while means != oldMeans:
		#assign clusters to centroids
		clusters = assignClusters(D, centroids)	
		
		#find mean point of each cluster
		#reassign oldMeans before assigning new means
		for i in range(k):
			oldMeans[i] = means[i]
			meanPoint = findClusterMean(clusters[i])
			means[i] = meanPoint
		
			#readjust centroids according to mean
			newCentroid = findClusterMean(clusters[i])
			centroids[i] = newCentroid		
			
		print('Old means: ', oldMeans)
		print('Means: ' , means)
		print("New centroids: ", centroids)
		
	#Visualization
	colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
	i = 0
	
	#Assign different colors to each cluster
	for cluster in myMeans.values():
		for point in cluster:	
			plt.scatter(point[0], point[1], color=colors[i])
		i+=1
	return clusters	
		
#returns a dictionary with each key i being the ith cluster
#values mapped to each key i being the list of data points in cluster i
myMeans = KMeans(points, 3)
	


	

