#A template for the implementation of hclust
import math #sqrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage  
import pandas as pd

#Importing Dataset
dataset = pd.read_csv('../data/movehubjoin.csv')

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

#draws dendogram visualization of all points
def visualize(points):
    numPyPoints = np.array(points[10:50])
    #DENDOGRAM
    linked = linkage(numPyPoints, 'single')
    plt.figure(figsize=(10, 7)) 
    dendrogram(linked,  
                orientation='top',
                #labels=labelList,
                distance_sort='descending',
                show_leaf_counts=True)
    plt.show() 

# Accepts two data points a and b.
# Returns the distance between a and b.
# Note that this might be specific to your data.
def Distance(a,b):
    return math.sqrt( ((a[0]-b[0])**2)+((a[1]-b[1])**2) )

# Accepts two data points a and b.
# Produces a point that is the average of a and b.
def merge(a,b):
    return [(a[0] + b[0])/2 , (a[1] + b[1])/2]

# Accepts a list of data points.
# Returns the pair of points that are closest
def findClosestPair(D):
    if (len(D) <= 2):
        return D
    
    closestPair = [None] * 2
    minDistance = Distance(D[0], D[1])
    
    for dataPoint in D:
        c = D.index(dataPoint)
        for otherPoint in (D[:c]+D[c+1:]):
            if (Distance(dataPoint, otherPoint) < minDistance):
                minDistance = Distance(dataPoint, otherPoint)
                closestPair = [dataPoint, otherPoint]
                
    return closestPair

# Accepts a list of data points.
# Produces a tree structure corresponding to a
# Agglomerative Hierarchal clustering of D.
def HClust(D):
    centers = D[10:15]
    splits = {}
    
    while (len(centers) > 1):
        # find closest pair [x, y] in D
        closestPair = findClosestPair(centers)
        
        # remove y from centers
        centers.remove(closestPair[1])
        
        #replace centers[x] with merge(x, y)
        for i in range(len(centers)):
            if centers[i] == closestPair[0]:
                centers[i] = merge(closestPair[0], closestPair[1])
        
                #key i in splits{} is the ith depth of tree
                splits.setdefault(i, []).append(closestPair)
                print(splits)
                
def main():
    myPoints = HClust(points)
    print(myPoints)
    visualize(points[10:15])
    
if __name__ == '__main__':
    main()