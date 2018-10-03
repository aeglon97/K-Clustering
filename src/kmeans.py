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
	colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
	
	#readjust centroids according to mean
	for i in range(k):
		new_c = findClusterMean(clusters[i])
		centroids[i] = new_c
	print("New centroids: ", centroids)
	
	#reassign data points
	clusters = assignClusters(D, centroids)
	for cluster in clusters:
		print('Cluster ' , cluster , ' size: ', len(clusters[cluster]))
		
	
	#print('Means: ' , means)
	
	'''print(means)
	while means != oldMeans:
		print("---------------")
		oldMeans = means
		print('old means: ', oldMeans, '\t' , 'means: ', means)
		clusters = {}
		for point in D:
			nearest = means[0]
			for m in means:
				if euclideanDistance(point, m) < euclideanDistance(nearest, point):
					nearest = m
					clusters[nearest].append(point) '''
	
	
	#print(clusters)
	
	
	
	#Visualization
	for cluster in clusters:
		i = 0
		color = colors[i]
		currentCluster = 0
		
		if (currentCluster != cluster):
			currentCluster +=1
			i+=1
			color = colors[i]
		
		for point in clusters[cluster]:
			plt.scatter(point[0], point[1], color=color)
	
	#print(clusters)
	
	myCluster = clusters[1]
	meanPoint = findClusterMean(myCluster)
	plt.scatter(meanPoint[0], meanPoint[1], color='red')
	
	
	
	
KMeans(points[10:30], 2)
	
'''means = D[1:k]
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
	

