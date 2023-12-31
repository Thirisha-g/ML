# -*- coding: utf-8 -*-
"""kMeans_IRIS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bgaHJZzwuKRVCJQW_DtRzoAoYyfEjJp_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

import plotly as py
import plotly.graph_objs as go

from sklearn.cluster import KMeans

import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('/content/Iris.csv')

df.info()

df.shape

df.isnull().sum()

df.head()

x=df.iloc[:,[3,4]].values
x

from sklearn.cluster import KMeans
cen=[]

for i in range(1,11):
    kmeans = KMeans(n_clusters= i, init='k-means++', random_state=0)
    kmeans.fit(x)
    cen.append(kmeans.inertia_)

plt.plot(range(1,11), cen)
plt.title('The Elbow Method')
plt.xlabel('no of clusters')
plt.ylabel('cen')
plt.show()

kmeansmodel = KMeans(n_clusters= 3, init='k-means++', random_state=0)
y_kmeans= kmeansmodel.fit_predict(x)

#Visualizing all the clusters

plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('SepalLengthCm')
plt.ylabel('PetalLengthCm')
plt.legend()
plt.show()

