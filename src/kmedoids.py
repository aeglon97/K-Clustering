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

# Accepts a list of data points.
# Returns the medoid of the points.
def findClusterMedoid(cluster):

# Accepts a list of data points, and a number of clusters.
# Produces a set of lists representing a K-Medoids clustering
#  of D.
def KMedoids(D, k):


