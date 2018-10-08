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
    numPyPoints = np.array(points)
    #DENDOGRAM
    linked = linkage(numPyPoints, 'single')
    plt.figure(figsize=(10, 7)) 
    dendrogram(linked,  
                orientation='top',
                #labels=labelList,
                distance_sort='descending',
                show_leaf_counts=True)
    return plt

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
    centers = D
    splits = []
    
    while len(centers) > 1:
        # find closest pair [x, y] in D
        closestPair = findClosestPair(centers)
        
        #indexes i and (i+1)%2==1 in splits[] is the ith depth of dendogram
        #append closestPair according to ith depth of dendogram
        splits.append(closestPair[0])
        splits.append(closestPair[1])
        
        index = 0
        while index < len(centers):
            if centers[index] == closestPair[0]:
                #replace the element containing closestPair[x] in centers with the
                #mean point between the closestPair of points
                centers[index] = merge(closestPair[0], closestPair[1])
                
            elif centers[index] == closestPair[1]:
                #remove y-coordinate of closestPair from centers
                centers.remove(centers[index])
                
            index += 1
    
    dendoGram = visualize(splits)
    return dendoGram
    
'''def HClust(D):
    centers = D[10:15]
    
    #there will be n-1 splits for size of list n, so total number of "splits"
    #in the dendogram will be n-1
    splits = []
    
        while (len(centers) > 1):
        print('--------------------')
        print('len(centers): ' , len(centers))
        print('centers: ', centers)
        
        # find closest pair [x, y] in D
        closestPair = findClosestPair(centers)
        #print('closest pair of points: ' , closestPair)
        
        splits.append(closestPair[0])
        splits.append(closestPair[1])
        print(splits)
        
        index = 0
        
        while index < len(centers):
            if centers[index] == closestPair[0]:
                #replace the element containing closestPair[x] in centers with the
                #mean point between the closestPair of points
                #print(closestPair)
                centers[index] = merge(closestPair[0], closestPair[1])
            elif centers[index] == closestPair[1]:
                # remove y-coordinate of closestPair from centers
                centers.remove(centers[index])
                #print('centers after removing closest pair[y]: ', centers)
                
            index += 1
            
    
    
    
    print(splits)      
    #visualize(splits)
    #return splits
                    
        #key i in splits{} is the ith depth of tree
        #append closestPair according to ith iteration'''
               
                
def main():
    myPlot = HClust(points)
    myPlot.show()
    
if __name__ == '__main__':
    main()