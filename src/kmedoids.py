#A template for the implementation of K-Medoids.
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
    return math.sqrt( ((a[0]-b[0])**2)+((a[1]-b[1])**2) )

# Accepts a list of data points D, and a list of centers
# Returns a dictionary of lists called "clusters", such that
# clusters[c] is a list of every data point in D that is closest
#  to center c.
def assignClusters(D, medoids):
	clusters = {}
	for dataPoint in D:
		distances = []
		#compare each data point to all 3 centroids stored in an array distances[]
		for medoid in medoids:
			distances.append(Distance(dataPoint, medoid))

		#find the minimum distance and keep track of its index
		minIndex = distances.index(min(distances))

		#index i of minimum distance = ith cluster in clusters[i]
		clusters.setdefault(minIndex, []).append(dataPoint)
		
	return clusters


# Accepts a list of data points.
# Returns the medoid of the points.
def findClusterMedoid(centers, clusters):
    
     for c in centers:
            for cand in clusters[centers.index(c)]:
                dist_c = 0
                dist_cand = 0
                for point in clusters[centers.index(c)]:
                    dist_c += Distance(c, point)
                    dist_cand += Distance(cand, point)
                    
                if dist_cand < dist_c:
                    c = cand
                    
                return clusters
    
    
# Accepts a list of data points, and a number of clusters.
# Produces a set of lists representing a K-Medoids clustering
#  of D.
def KMedoids(D, k):
    centers = D[0:k]
    oldCenters = [None] * k
    #initialize means and oldMeans to size k
    #medoids = D[0:k]oldMedoids = [None] * k

    #generate k number of centroids
    #initialize centroids with first k amount of points in D
        
    while centers != oldCenters:
        oldCenters = centers
        clusters = assignClusters(D, centers)
        
        for center in centers:
            for cand in clusters[centers.index(center)]:
                dist_c = 0
                dist_cand = 0
                for point in clusters[centers.index(center)]:
                    dist_c += Distance(center, point)
                    dist_cand += Distance(cand, point)
                    
                if dist_cand < dist_c:
                    center = cand
                    
                return clusters

def visualize(clusters):
	colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
	i = 0
	
	#Assign different colors to each cluster
	for cluster in clusters.values():
		for point in cluster:	
			plt.scatter(point[0], point[1], color=colors[i])
		i+=1

def main():
    myMedoids = KMedoids(points, 2)
    visualize(myMedoids)

if __name__ == '__main__':
    main()
    

