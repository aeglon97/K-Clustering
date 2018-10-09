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
def findClusterMedoid(cluster):
    minDistance = 100
    for point in cluster:
        for comparePoint in cluster:
            if Distance(point, comparePoint) < minDistance:
                minDistance = Distance(point,comparePoint)
                medoid = point
                
    return medoid

# Accepts a list of data points, and a number of clusters.
# Produces a set of lists representing a K-Medoids clustering
#  of D.
def KMedoids(D, k):
    #initialize medoids and oldMedoidss to size k
    medoids = D[0:k]
    oldMedoids = [None] * k
 
    #initialize centroids with first k amount of points in D
    centroids = D[0:k]
        
    while medoids != oldMedoids:
        clusters = assignClusters(D, centroids)
        
        for i in range(k):
            #find mean point of each cluster
            #reassign oldMedoids before assigning new means
            oldMedoids[i] = medoids[i]
            medoid = findClusterMedoid(clusters[i])
            medoids[i] = medoid
            
            #readjust data points according to means
            newCentroid = findClusterMedoid(clusters[i])
            centroids[i] = newCentroid	
            
            '''Uncomment below for troubleshooting
            print('Old medoids: ', oldMedoids)
            print('medoids: ', medoids)
            print('new centroids: ', centroids)
            '''
		      
    return clusters

def visualize(clusters):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    i = 0
    
    for cluster in clusters.values():
        for point in cluster:
            plt.scatter(point[0], point[1], color = colors[i])
        i +=1 
        
    #label axes
    plt.xlabel('Purchase Power')
    plt.ylabel('Cappuccino')
    #save visualization to a .png file
    plt.savefig('../visualizations/kmedoids.png')
    plt.show()
   
def main():
    myMedoids = KMedoids(points, 2)
    visualize(myMedoids)
    
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
    

