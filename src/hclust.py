#A template for the implementation of hclust
import math #sqrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage  
import pandas as pd

#Importing Dataset
dataset = pd.read_csv('../data/movehubjoin.csv')

#dataset.plot(kind='scatter', x='Purchase Power', y='Cappuccino')

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
    
#converts points array 

#draws dendogram visualization of all points
def visualize(points):
    numPyPoints = np.array(points[10:50])
    #DENDOGRAM
    linked = linkage(numPyPoints, 'single')
    
    #labelList = range(1, 5) 
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
    if (len(D) <= 1):
        return D

        
                    
# Accepts a list of data points.
# Produces a tree structure corresponding to a
# Agglomerative Hierarchal clustering of D.
def HClust(D):
    centers = D[10:15]
    splits = [None] * len(centers)
    
    while (len(centers) > 0):
        minDistance = Distance(centers[0],centers[1])
        location = [centers[0], centers[1]]
        
        for c in range(len(centers)):
            for d in (centers[:c]+centers[c+1:]):
                print('-------------------------------')
                print(d)
                minDistance = Distance(centers[c], d)
                location = [centers[c],d]    
                print('location:' , location)
        
        print(centers)
        centers.remove(location[1])
        print(centers)
        
        #print('centers[c]: ' , centers[c])
        print(merge(location[0], location[1]))
        #centers[c] = merge(location[0], location[1])
        
        #splits[centers[c]] = location
       
    return centers
        
        
def main():
    myPoints = HClust(points)
    visualize(myPoints)
    
if __name__ == '__main__':
    main()