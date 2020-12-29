# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:03:51 2018

@author: Pinnacle
"""
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#input
rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
#pca
pca = PCA(n_components=2)
pca.fit(X)
print(pca.components_) #
print(pca.explained_variance_)

#input

#dimensionality reduction
X_pca = pca.transform(X)
print("original shape:   ", X.shape)
print("transformed shape:", X_pca.shape)
'''
#
pca = PCA(2)  # project from 64 to 2 dimensions
projected = pca.fit_transform(digits.data)
print(digits.data.shape)
print(projected.shape)
'''
pca = PCA(2)  # project from 64 to 2 dimensions
projected = pca.fit_transform(digits.data)
print(digits.data.shape)
print(projected.shape)

plt.scatter(projected[:, 0], projected[:, 1],
            c=digits.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('spectral', 10))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar();
