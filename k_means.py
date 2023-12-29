# -*- coding: utf-8 -*-
"""k_means.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nDAkJ2r9b1upjdGCUY8xisU34a8knDWG
"""

import numpy as np
import matplotlib.pyplot as plt

def initalize_centroids(x,k):
  indices=np.random.choice(len(x),k,replace=False)
  return x[indices]

def assign_to_cluster(x,centroids):
  distance=np.linalg.norm(x[:,np.newaxis]-centroids,axis=2)
  return np.argmin(distance,axis=1)

def update_centroids(x,labels,k):
  centroids=np.array([x[labels==i].mean(axis=0) for i in range(k)])
  return centroids

def k_means(x,k,max_iters=100):
  centroids=initalize_centroids(x, k)

  for _ in range(max_iters):
    labels=assign_to_cluster(x , centroids)
    new_centroids=update_centroids(x,labels,k)

    if np.all(centroids==new_centroids):
      break

    centroids=new_centroids
  return labels,centroids

np.random.seed(42)
x=np.concatenate([np.random.normal(loc=i,scale=1,size=(50,2))for i in range(5)])

x

k=5
labels,centroids=k_means(x,k)

plt.scatter(x[:,0],x[:,1],c=labels,cmap='viridis')
plt.scatter(centroids[:,0],centroids[:,1],marker='x',s=200,c='red',label='centroid')

plt.title('k means')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()

