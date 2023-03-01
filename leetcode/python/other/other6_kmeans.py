

import pandas as pd
import numpy as np

# 计算欧拉距离
def calcDis(dataSet, centroids, k):
    clalist=[]  # 保存每个点到k个中心点的距离
    for data in dataSet:
        squaredDiff = (np.array(data) - centroids) ** 2  # 相减，再平方
        squaredDist = np.sum(squaredDiff, axis=1)   # 求和
        distance = squaredDist ** 0.5  # 开根号
        clalist.append(distance)
    return clalist

# 计算质心
def classify(dataSet, centroids, k):
    clalist = calcDis(dataSet, centroids, k)        # 计算样本到质心的距离
    # 分组并计算新的质心
    minDistIndices = np.argmin(clalist, axis=1)     # axis=1 表示求出每行的最小值的下标
    newCentroids = pd.DataFrame(dataSet).groupby(minDistIndices).mean() #DataFramte(dataSet)对DataSet分组，groupby(min)按照min进行统计分类，mean()对分类结果求均值
    newCentroids = newCentroids.values
 
    # 计算变化量
    changed = newCentroids - centroids
 
    return changed, newCentroids

# 使用k-means分类
def kmeans(dataSet, k):
    # centroids = np.array(random.sample(dataSet, k))       # 随机取质心
    centroids = dataSet[:k, :]      # 或者选取前k个当作质心，保证输出的一致性
    
    # 更新质心, 直到变化量全为0
    changed, newCentroids = classify(dataSet, centroids, k)
    while np.any(changed != 0):
        changed, newCentroids = classify(dataSet, newCentroids, k)

    centroids = np.array(sorted(newCentroids.tolist()))

    # 根据质心计算每个集群
    cluster = []
    clalist = calcDis(dataSet, centroids, k) # 调用欧拉距离
    minDistIndices = np.argmin(clalist, axis=1)  
    # for i in range(k):
    #     cluster.append([])
    # for i, j in enumerate(minDistIndices):   # enymerate()可同时遍历索引和遍历元素
    #     cluster[j].append(dataSet[i])
        
    # return centroids, cluster
    return minDistIndices
 
# 创建数据集
def createDataSet():
    return np.array([[1.5, 2.1], [0.8, 2.1], [1.3, 2.1], [110.5, 260.6], 
                    [21.7, 32.8], [130.9, 150.8], [32.6, 40.7], [41.5, 24.7]])

if __name__=='__main__':
    dataset = createDataSet()
    k = 3
    minDistIndices = kmeans(dataset, k)
    print(minDistIndices)       # [0 0 0 2 1 2 1 1]
    # for i in range(len(dataset)):
    #   plt.scatter(dataset[i][0],dataset[i][1], marker = 'o',color = 'green', s = 40 ,label = '原始点')
    #                                                 #  记号形状       颜色      点的大小      设置标签
    #   for j in range(len(centroids)):
    #     plt.scatter(centroids[j][0],centroids[j][1],marker='x',color='red',s=50,label='质心')
    #     plt.show()

