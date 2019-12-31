import random as rn
import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt
from matplotlib.pyplot import scatter
data = []
##############################################################################################
def loadData(file_name):
    with open(file_name, 'r') as csvFile:
        lines = csv.reader(csvFile)
        data_set = list(lines)
        data_set.pop(0)
        for column in range(len(data_set)):
            for row in range(len(data_set[0])):
                data_set[column][row] = float(data_set[column][row])
    return data_set

for i in range(200):
    x = list(np.random.randint(0,1000,2))
    data.append(x)

################################################################3
def initialK(data,K):
    lst = []
    a = np.random.randint(0,len(data))
    lst.append(data[a])
    dis = np.zeros(len(data))
    for j in range(K-1):
        for i in range(len(data)):
            dis[i]+= distance(lst[len(lst)-1],data[i])
        a = np.argmax(dis)
        lst.append(data[a])
    return lst

##################################################################################33
def distance(x,y):
    d = 0
    for i in range(len(x)):
        d += (x[i] - y[i])**2
    d = np.sqrt(d)
    return d
##################################################################3
def cal_mean(X,c):
    n = len(c)
    s = [0]*len(X[0])
    for i in range(n):
        for j in range(len(X[0])):
            s[j]+=X[c[i]][j]
    for j in range(len(X[0])):
        s[j]/=n
    return s
########################################2020
def kmeans(X,k,maxiter=100):
    lst = initialK(X,k)
    for lp in range(maxiter):
        cluster = []
        for i in range(k):
            cluster.append([])
        for i in range(len(X)):
            min_idx = 0
            min_dis=999999
            for j in range(k):
                d = distance(lst[j],X[i])
                if d<min_dis:
                    min_idx = j
                    min_dis = d
            cluster[min_idx].append(i)
        for i in range(k):
            if(len(cluster[i])!=0):
                lst[i] = cal_mean(X,cluster[i])
    return cluster
res = kmeans(data,6,maxiter=10)
color = ['b','g','r','y','c','k','m']
fig = plt.figure()
ax  = fig.add_subplot(111)

for i in range(len(res)):
    lst = []
    col = color[i]
    for j in range(len(res[i])):
        lst.append(data[res[i][j]])
    lst = pd.DataFrame(lst)
    ax.scatter(lst[0],lst[1],c=col)
plt.show()