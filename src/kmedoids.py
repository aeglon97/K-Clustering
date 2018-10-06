#A template for the implementation of K-Medoids.
import math #sqrt


# Accepts two data points a and b.
# Returns the distance between a and b.
# Note that this might be specific to your data.
def Distance(a,b):
	
	
	

# Accepts a list of data points D, and a list of centers
# Returns a dictionary of lists called "clusters", such that
# clusters[c] is a list of every data point in D that is closest
#  to center c.
# Note: This can be identical to the K-Means function of the same name.
def assignClusters(D, centers):
	clusters = {}
	for data_point in D:
		distances = []
		#compare each data point to all 3 centroids stored in an array distances[]
		for center in centers:
			distances.append(euclideanDistance(data_point, center))

		#find the minimum distance and keep track of its index
		min_index = distances.index(min(distances))
		
		#index i of minimum distance = ith cluster in clusters[i]
		clusters.setdefault(min_index, []).append(data_point)
		
	return clusters

# Accepts a list of data points.
# Returns the medoid of the points.
def findClusterMedoid(cluster):

# Accepts a list of data points, and a number of clusters.
# Produces a set of lists representing a K-Medoids clustering
#  of D.
def KMedoids(D, k):


