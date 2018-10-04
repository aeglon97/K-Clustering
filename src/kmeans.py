#A template for the implementation of K-Means.
import math #sqrt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

#Importing Dataset
dataset = pd.read_csv('../data/movehubjoin.csv')


#Purchase Power
X = dataset.iloc[:,8]
rand_x = random.uniform(1, np.max(X)-10)
#Cappuccino
Y = dataset.iloc[:,1]
rand_y = random.uniform(1, np.max(Y))

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
	print('-----------')
	means = []
	oldMeans = [None] * k
	
	#generate k number of centroids
	centroids = []
	for i in range(k):
		#centroids.insert(i, [random.uniform(1, rand_x), random.uniform(1, rand_y)])
		
		centroids.insert(i, points[i])
	
	
	print('Centroids: ', centroids)
	
	#assign clusters to centroids
	clusters = assignClusters(D, centroids)
	for cluster in clusters:
		print('Cluster ' , cluster , ' size: ', len(clusters[cluster]))
	#print(clusters)
	
	
	
	for i in range(k):
		meanPoint = findClusterMean(clusters[i])
		means.append(meanPoint)
	
	print("Means: " , means)
	
	while means != oldMeans:
		print('--------------')
		#readjust centroids according to mean
		for i in range(k):
			new_c = findClusterMean(clusters[i])
			centroids[i] = new_c
			
		print("New centroids: ", centroids)
		
		#reassign data points
		clusters = assignClusters(D, centroids)
		for cluster in clusters:
			print('Cluster ' , cluster , ' size: ', len(clusters[cluster]))
		
		for i in range(k):
			oldMeans[i] = means[i]
			meanPoint = findClusterMean(clusters[i])
			means[i] = (meanPoint)
		
		print(oldMeans)
		print('New means: ' , means)
	
	
	colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
	i = 0
	
	for cluster in clusters.values():
		for point in cluster:
			plt.scatter(point[0], point[1], color=colors[i])
		
		i+=1
	
	
	#Visualization
	'''for cluster in clusters:
		color = colors[i]
		print(color)
		if (currentCluster != cluster):
			currentCluster +=1
			print('current cluster: ' , currentCluster)
			i+=1
			color = colors[i]
		
		for point in clusters[cluster]:
			print('color: ' , color)
			plt.scatter(point[0], point[1], color=color)'''
	
	
	
	
KMeans(points, 3)
	

