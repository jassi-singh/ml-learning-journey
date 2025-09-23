import numpy as np
import matplotlib.pyplot as plt


def plot_all_features(X,y,features,ax,*,c="tab:blue"):    
    for j in range(len(ax)):
        for i in range(len(ax[j])):
            k = 4 * j + i
            ax[j][i].scatter(X[:,k],y,c=c)
            ax[j][i].set_xlabel(features[k])
        ax[j][0].set_ylabel("Price")
        